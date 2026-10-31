# Research tracks

Start each track from the buyer's deciding factors. Cast wide first: list every option, including types the user did not mention, and do not drop a contender quietly.

Each track writes one note to `notes/<track>.md`, using the format at the end of this file. At Quick, keep one combined `notes/research.md`.

**When a source is blocked:** many retailer and review sites refuse automated fetches. Do not retry the same page. Try the same maker's document hosts, another seller, a price tracker, or a search result, label how it was read, and list the failure under What we could not read. If a key fact can only be found through a weak source, the pick may still rest on it, at Low confidence, and the report must say so.

**PDFs:** fetch tools may return binary or save the file. If so, use `pdftotext` where installed, or read the saved PDF directly. Label a document from another region or an older date as such.

## Official

Read the maker's own pages, set to the buyer's real city where the site allows it. Some makers have no findable site, and some show no selling price. If so, say that and use the best seller listing.

Bring back, per model and variant:
- price breakup, where it has one, and what is left out of the price
- warranty fine print: parts, labour and consumables separately, limits, exclusions, who decides a claim, what voids it. Read both standard and promotional terms, and note any scheme end date
- specs that bear on the deciding factors, and any model-suffix differences
- FAQs, which often hold the real conditions
- things that are announced but not on sale

Compare with what the buyer must really buy. If they need an extended warranty, an accessory or installation, add it to the price of every option. Price any later purchase the plan depends on, such as an upgrade or replacement part. Check that add-on plans apply to this exact product line.

## Price

Find the real price from official sellers first and then large retailers, in the buyer's city where prices vary by place. Note the date, seller, and whether delivery, installation or exchange is included. Aggregators can mislead: the same site may include different add-ons per brand, so prefer the official breakup.

Stock and price on some sites appear only after a location or pincode is set, so set one before concluding anything is unavailable, and record which sellers were set. If it will not stick, record that and move on. A search result's "starting price" may be a different build, so open the maker's family page before calling a price gap real. Report any location you changed, as it stays saved in the buyer's browser.

Offers count only if a dated offer was found. Otherwise say none was found, and do not tell the buyer to rush. Ignore countdown timers with no date or terms, and do not count card-only offers for a buyer paying another way. Report a dated price rise the same way. If the buyer has no working product today, stock now can outweigh a small saving.

## Finance

Run only if they may borrow.

- Read the lender's own offer screen or schedule of charges.
- Record flat or reducing, processing fee, longest tenure, and prepayment charge.
- Confirm with `scripts/loan.py check`, then compute the true rate with `true-rate`.
- Compare with at least one bank.
- Check "no-cost" and very low rates for what they require: down payment, short tenure, lost discounts.
- A personal offer belongs to that buyer. The user types their own details and you read the result only with their go-ahead. Label it `[Offer]`, and never apply it to anyone else.
- Where it applies, check that the loan does not outlast the warranty, so they never pay an EMI and a major repair bill together.

## Owners and independent tests

**Independent tests:** look for consumer bodies and testing labs, and label results `[Test]`. Many are paywalled. Use a buyer's own membership only with their consent. Otherwise, list the unread score as a gap, since it may be the one check that settles the pick.

**Owners:** look as widely as possible: review sites, Reddit, forums, app store reviews, complaint boards, YouTube transcripts and comments.

- Prioritise heavy users, long-term owners, and people in the buyer's city or climate.
- For each account, record usage, age, what happened, and cost. Say that none of it is verified.
- Tell the same person's accounts apart from separate people, and do not count one owner twice.
- Note when reports concern an older design. They may not transfer to the current model.

For cheap goods and fast-changing electronics, long-term accounts are often missing. Say so, do not spend long hunting, and walk back to earlier generations of the same design, stating what carries over. Label tests of a related model `[Test, sibling]`. Treat review counts as a minimum, not as coverage.

**Reddit:** often refused by browser and search tools. Try once, then list it as not read.

**YouTube:** check for speech first, since many short reviews are music only. In Chrome, open the video's description and click "Show transcript" with a real mouse click, as scripted clicks may leave the panel hidden. Then read the panel's text in slices, as tools may cut long output. If that fails or Chrome is unavailable, if `yt-dlp` is already installed, try `yt-dlp --skip-download --write-auto-subs --sub-langs "en.*,hi.*" --ignore-no-formats-error <url>`, adding the buyer's language. It may fail with HTTP 429. If so, stop trying and record the videos as not read. Never install anything. Mark auto-captions, since numbers can be garbled.

## Instagram and Facebook

Run only with consent for that site. Read about 25 posts per site at most, counting each tile, card or opened post as one. Stick to public posts and public groups, and never join a group.

**Stop early** if 10 posts in a row show no real owner. This track helps most for vehicles and goods with owner communities, and in the test laptop run, results were almost all sellers, so it changed nothing. Short queries work better on Instagram, and longer ones may return nothing.

Yield is often short complaints, so read for patterns. Tag each item owner, dealer, creator, paid or unclear. Record what you could not see, such as speech inside reels and comments that did not load. Say plainly when this track changed nothing.

## Local shops

Read map listings for showrooms and service centres near the buyer, with ratings, counts and review text. Sort by lowest and by newest. Without Chrome, this usually fails. Say so, and in Before paying, tell the buyer exactly which listings to read and what to look for.

- A listing named "<brand> service centre" may not be authorised, and look-alikes often rate higher than real centres. Compare with the brand's own service finder. Say "not on the finder today", not "fake". Tell the buyer to book service through the brand.
- A centre can pool reviews across products and brands, so check they concern this product. If the warranty is on-site, walk-in ratings matter less.
- Weigh service ratings over sales ratings.
- Treat delivery-day five-star reviews as weak evidence, as set out in the evidence rules.
- Read the text under the number, including recent low-star reviews.
- Say which listings were rating only.
- Name businesses in the user's private report only, and describe complaints as what reviewers report.

## Other options

Ask separately: does anything beat these? Include other types, other brands, used or refurbished where sensible, and keeping what they own or how they manage today. Judge used or refurbished by who backs the warranty and how much cover remains against the years kept. For each option, give a one-line reason it is in or out. At Quick, a short sweep is enough.

## Note format

Use this structure, and add a table where comparing many models, listings or finance routes reads better.

```markdown
# <Track>: <item> (read <date>)

How this was read: <Chrome, fetch or search; city setting; logged in or not>

## <Topic>
### Takeaway
<1-3 lines>
### Cited Findings
<facts with source links, tagged by fact type>
### Inferences
<what you conclude, labelled as yours>
### Gaps
<what could not be read, and why>
```
