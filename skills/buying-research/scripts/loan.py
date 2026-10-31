#!/usr/bin/env python3
"""Loan arithmetic for comparing purchase finance. Standard library only.

    loan.py emi --principal 100000 --rate 12 --months 12
    loan.py check --principal 100000 --rate 10 --months 36 --emi 3611
    loan.py true-rate --principal 100000 --emi 3611 --months 36 --fee 2000
    loan.py no-cost --price 85000 --rate 16 --months 6 --fee 299 --discount-lost 3000

Amounts are in any one currency. Rates are percent a year. True rate is the
monthly rate x 12, which can differ slightly from a lender's APR. This does
arithmetic on the numbers given. It is not a quote and not financial advice.
"""
import argparse
import json


def reducing_emi(principal, annual_rate, months):
    """Monthly payment on a reducing-balance loan."""
    if principal <= 0 or months <= 0 or annual_rate < 0:
        raise ValueError("principal and months must be positive, rate not negative")
    r = annual_rate / 1200
    if r == 0:
        return principal / months
    return principal * r * (1 + r) ** months / ((1 + r) ** months - 1)


def flat_emi(principal, annual_rate, months):
    """Monthly payment when interest is charged on the full amount for the whole term."""
    if principal <= 0 or months <= 0 or annual_rate < 0:
        raise ValueError("principal and months must be positive, rate not negative")
    return principal * (1 + annual_rate / 100 * months / 12) / months


def rate_type(principal, annual_rate, months, emi, tolerance=None):
    """Say whether a quoted EMI matches reducing or flat maths at the stated rate."""
    if tolerance is None:
        tolerance = max(2.0, emi * 0.001)
    reducing = reducing_emi(principal, annual_rate, months)
    flat = flat_emi(principal, annual_rate, months)
    if abs(emi - reducing) <= tolerance:
        kind = "reducing"
    elif abs(emi - flat) <= tolerance:
        kind = "flat"
    else:
        kind = "neither"
    return {"type": kind, "reducing_emi": round(reducing, 2), "flat_emi": round(flat, 2)}


def true_rate(principal, emi, months, fee=0.0):
    """Annual rate (monthly rate x 12) on the money actually received after the fee."""
    received = principal - fee
    if received <= 0:
        raise ValueError("fee must be smaller than the principal")
    if emi * months < received:
        raise ValueError("payments do not repay the amount received")

    def present_value(annual):
        r = annual / 1200
        if r == 0:
            return emi * months
        return emi * (1 - (1 + r) ** -months) / r

    low, high = 0.0, 1000.0
    for _ in range(200):
        mid = (low + high) / 2
        if present_value(mid) > received:
            low = mid
        else:
            high = mid
    return (low + high) / 2


def loan_cost(principal, emi, months, fee=0.0):
    """Everything paid beyond the principal: interest plus fee."""
    return emi * months - principal + fee


def no_cost_emi(price, annual_rate, months, fee=0.0, gst=18.0, discount_lost=0.0):
    """Real cost of a "no-cost" EMI: the seller's discount cancels the interest, not the tax on it.

    fee is before tax. discount_lost is any cash discount given up by choosing EMI.
    Tax on interest is spread evenly across months, which slightly understates the rate.
    """
    if discount_lost < 0 or discount_lost >= price:
        raise ValueError("discount lost must be between zero and the price")
    r = annual_rate / 1200
    emi = price / months
    financed = price if r == 0 else emi * (1 - (1 + r) ** -months) / r
    interest = price - financed
    tax_on_interest = interest * gst / 100
    fee_with_tax = fee * (1 + gst / 100)
    extra = tax_on_interest + fee_with_tax + discount_lost
    cash_price = price - discount_lost
    rate = true_rate(cash_price, emi + tax_on_interest / months, months, fee_with_tax)
    return {
        "interest_handed_back": round(interest, 2),
        "tax_on_interest": round(tax_on_interest, 2),
        "total_extra": round(extra, 2),
        "extra_percent_of_cash_price": round(extra / cash_price * 100, 2),
        "true_rate_percent": round(rate, 2),
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description="Loan arithmetic for purchase comparisons.")
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("emi", help="monthly payment, reducing and flat")
    p.add_argument("--principal", type=float, required=True)
    p.add_argument("--rate", type=float, required=True)
    p.add_argument("--months", type=int, required=True)

    p = sub.add_parser("check", help="does a quoted EMI match reducing or flat maths?")
    p.add_argument("--principal", type=float, required=True)
    p.add_argument("--rate", type=float, required=True)
    p.add_argument("--months", type=int, required=True)
    p.add_argument("--emi", type=float, required=True)

    p = sub.add_parser("true-rate", help="true annual rate and total cost, including fees")
    p.add_argument("--principal", type=float, required=True)
    p.add_argument("--emi", type=float, required=True)
    p.add_argument("--months", type=int, required=True)
    p.add_argument("--fee", type=float, default=0.0)

    p = sub.add_parser("no-cost", help="real cost of a no-cost EMI, with tax on interest")
    p.add_argument("--price", type=float, required=True)
    p.add_argument("--rate", type=float, required=True, help="the bank's underlying rate")
    p.add_argument("--months", type=int, required=True)
    p.add_argument("--fee", type=float, default=0.0, help="processing fee before tax")
    p.add_argument("--gst", type=float, default=18.0, help="tax percent on interest and fee")
    p.add_argument("--discount-lost", type=float, default=0.0)

    args = parser.parse_args(argv)
    try:
        if args.command == "emi":
            result = {
                "reducing_emi": round(reducing_emi(args.principal, args.rate, args.months), 2),
                "flat_emi": round(flat_emi(args.principal, args.rate, args.months), 2),
            }
        elif args.command == "check":
            result = rate_type(args.principal, args.rate, args.months, args.emi)
        elif args.command == "no-cost":
            result = no_cost_emi(args.price, args.rate, args.months, args.fee, args.gst, args.discount_lost)
        else:
            result = {
                "true_rate_percent": round(true_rate(args.principal, args.emi, args.months, args.fee), 2),
                "interest_plus_fee": round(loan_cost(args.principal, args.emi, args.months, args.fee), 2),
            }
    except ValueError as error:
        parser.error(str(error))
    print(json.dumps(result))


if __name__ == "__main__":
    main()
