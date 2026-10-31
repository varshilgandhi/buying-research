# buying-research

A Claude skill for anything you want to buy. Say what you want, answer 3-5 useful questions, and get one honest pick.

It checks official sites, real prices, loan terms, independent tests and owner reviews. For bigger purchases, it also reads YouTube transcripts, local shops, Instagram and Facebook. You get:

- **One pick and one fallback**, with a High, Medium or Low confidence label
- **When to buy:** now, or wait for a named sale, using the model's past sale prices where it can find them
- **The pick's weaknesses**, and what would change the answer
- **What it could not read**, named plainly
- **A saved report** with its research notes

See a [worked example](skills/buying-research/references/worked-example/report.md). It shows the method, and it's not buying advice.

## Install

New to Claude Code? Follow the [official quickstart](https://code.claude.com/docs/en/quickstart) first. It needs a computer and a paid Claude plan or a Console account. A skill can't install Claude Code for you.

Then, in your terminal:

```
claude plugin marketplace add varshilgandhi/buying-research
claude plugin install buying-research@buying-research
```

Then ask, for example: `which AC should I buy for a small bedroom in Pune?`

## How much effort it spends

| Tier | For | Research |
|---|---|---|
| Quick | Small purchases | Official sites, price, owners and tests, a short look at alternatives |
| Standard | Mid-priced purchases | Adds YouTube, local shops and a full look at alternatives |
| Deep | Major purchases, sizeable loans | Adds Instagram and Facebook, using subagents |

Loan checks are added at any tier if you may borrow.

It tells you the tier before starting, and you can change it. A Deep run can use a lot of tokens and may hit your plan's limits. Notes are saved as it goes, so it can resume.

## What you need

- **Required:** Claude Code. Python 3 is used for loan arithmetic.
- **Recommended:** Claude in Chrome, for live stock, city-set prices, map reviews and personal loan screens. Without it, the skill uses web search and fetch and says what is lost. Many retailers block fetching, so expect more Low-confidence picks and little local evidence.
- **Optional:** `yt-dlp` for YouTube captions without Chrome, and `pdftotext` for PDF manuals.

The skill checks for these helper tools. If one is missing, it asks once and installs it with your system's package manager when you say yes. You type any admin password yourself, and you install Claude in Chrome yourself.

The skill files may also load on claude.ai, but that is untested.

## Limits to know about

- **Countries:** tuned and tested for India. Elsewhere it uses the same method and tells you no tested guide exists for your country.
- **Logged-in sites:** it asks per site before reading Instagram, Facebook or a lender in your logged-in browser. Automated reading from your own account may break a site's terms and carries some risk to that account, and its searches may stay in your recent searches. Saying no is fine, and the report lists what was skipped. Your own name may enter the Claude session if a page shows it, but stays out of the saved notes.
- **Your data:** you type your own OTP and personal details. The browser stays read-only, so it doesn't book, pay, like, join or message. Reports stay on your machine and may include your personal offer details.
- **Repeat runs:** the same buyer can get a different pick on another run, as prices, stock and estimates shift. In testing, one AC buyer got different brands with and without Chrome. Read the flip conditions as well as the pick.
- **Browser settings:** setting a pincode on a site stays saved in your browser. The skill tells you if it changed one.
- **Evidence:** owner reviews are unverified, and complaint counts are not failure rates. Prices change, so confirm them with the seller.
- **Finance:** comparison and arithmetic, not licensed financial advice.

## Licence

MIT. Sources quoted in the worked example belong to their publishers.
