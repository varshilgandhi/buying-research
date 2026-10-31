import unittest

from loan import flat_emi, loan_cost, no_cost_emi, rate_type, reducing_emi, true_rate


class ReducingEmi(unittest.TestCase):
    def test_known_value(self):
        self.assertAlmostEqual(reducing_emi(100000, 12, 12), 8884.88, places=2)

    def test_zero_rate_splits_evenly(self):
        self.assertEqual(reducing_emi(12000, 0, 12), 1000)

    def test_rejects_bad_input(self):
        with self.assertRaises(ValueError):
            reducing_emi(0, 10, 12)
        with self.assertRaises(ValueError):
            reducing_emi(1000, 10, 0)


class FlatEmi(unittest.TestCase):
    def test_interest_on_full_amount(self):
        self.assertAlmostEqual(flat_emi(100000, 10, 36), 3611.11, places=2)


class RateType(unittest.TestCase):
    def test_reducing(self):
        self.assertEqual(rate_type(100000, 12, 12, 8885)["type"], "reducing")

    def test_flat(self):
        self.assertEqual(rate_type(100000, 10, 36, 3611)["type"], "flat")

    def test_neither(self):
        self.assertEqual(rate_type(100000, 10, 36, 4000)["type"], "neither")


class TrueRate(unittest.TestCase):
    def test_no_fee_returns_stated_rate(self):
        emi = reducing_emi(100000, 12, 24)
        self.assertAlmostEqual(true_rate(100000, emi, 24), 12, places=4)

    def test_fee_raises_the_rate(self):
        emi = reducing_emi(100000, 12, 24)
        self.assertGreater(true_rate(100000, emi, 24, fee=2000), 12)

    def test_flat_rate_costs_far_more_than_it_sounds(self):
        emi = flat_emi(100000, 10, 36)
        self.assertGreater(true_rate(100000, emi, 36), 17)

    def test_zero_interest_with_fee_is_not_free(self):
        self.assertGreater(true_rate(12000, 1000, 12, fee=240), 3)

    def test_rejects_impossible_loans(self):
        with self.assertRaises(ValueError):
            true_rate(1000, 100, 12, fee=1000)
        with self.assertRaises(ValueError):
            true_rate(100000, 100, 12)


class LoanCost(unittest.TestCase):
    def test_interest_plus_fee(self):
        self.assertEqual(loan_cost(10000, 1000, 12, fee=200), 2200)


class NoCostEmi(unittest.TestCase):
    def test_tax_on_interest_is_not_free(self):
        result = no_cost_emi(85000, 16, 6, fee=299)
        self.assertAlmostEqual(result["total_extra"], 1045, delta=10)
        self.assertAlmostEqual(result["true_rate_percent"], 4.2, delta=0.2)

    def test_lost_discount_makes_it_expensive(self):
        result = no_cost_emi(85000, 16, 6, fee=299, discount_lost=3000)
        self.assertAlmostEqual(result["true_rate_percent"], 16.8, delta=0.3)

    def test_zero_rate_with_no_fee_really_is_free(self):
        result = no_cost_emi(60000, 0, 6)
        self.assertEqual(result["total_extra"], 0)

    def test_rejects_bad_discount(self):
        with self.assertRaises(ValueError):
            no_cost_emi(1000, 10, 6, discount_lost=1000)


if __name__ == "__main__":
    unittest.main()
