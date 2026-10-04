# Executive Summary & Recommendations

**Project:** Olist E-Commerce Sales Analysis


## Overview

This project consist of two years of Brazilian e-commerce data (2016–2018) to understand how the business is doing on sales, delivery, and customer behavior. The full details and methodology are in the EDA report, this page is the short version of what stood out, and what to do about it.

## What I Found

The business pulled in $13,591,644 across 96,478 delivered orders, averaging $137.04 per order. That's the headline number, but a few things underneath it stand out more.

First, almost all of that revenue is coming from one place. Sao Paulo alone accounts for 38.32% of total revenue, nearly three times as much as the next state, Rio de Janeiro. That's a lot of eggs in one basket.

Second, there isn't really one "best" product category, it depends on what you're looking at. health_beauty brings in the most total revenue, bed_bath_table gets the most individual orders, and computers has by far the highest price per order, even though it barely shows up when you rank by total revenue. So the answer to "what's our top category?" genuinely changes depending on the question being asked.

On the operations side, delivery is a real strength. Orders arrive early more often than not, 93.23% show up on time or ahead of schedule, and the average order beats its estimated delivery date by almost 12 days. That's worth protecting.

Where things get concerning is repeat business. Only 3.00% of customers ever placed a second order. The vast majority buy once and never come back. And there's a clue as to why that might matter: orders that arrive late get noticeably worse reviews (2.57 stars on average) than orders that arrive on time or early (4.28 stars). That doesn't prove late delivery is driving people away for good, but it's a strong enough pattern to take seriously.

One more thing worth flagging: revenue spiked hard on a single day, November 24, 2017, Black Friday in Brazil, outselling every other day that month by a wide margin. That kind of demand spike is worth planning around.


## What I'd Recommend

**Spread revenue beyond Sao Paulo.** With over a third of the business riding on one state, it's worth understanding why other states lag behind, is it shipping cost, product availability, marketing reach, something else? Testing a targeted push in the next couple of states (RJ, MG) seems like a reasonable next step.

**Be specific about what "top category" means.** Since revenue, order volume, and price per order each tell a different story, any decision about where to invest, ad spend, inventory, promotions, should say clearly which of those it's actually optimizing for.

**Don't let delivery speed slip.** It's one of the clearest strengths in the data, and it's tied to better reviews. Any changes to shipping or fulfillment should be tested carefully so this doesn't quietly get worse.

**Look harder at why customers don't come back.** A 3% repeat rate is low enough to be a real problem. The delivery-to-review link is a reasonable place to start investigating, but it's not the whole story this data doesn't show what actually drives someone to never order again, so it's worth following up with something more direct, like customer surveys or a look at what happens after a bad review.

**Plan for demand spikes like Black Friday.** If revenue can jump that hard in a single day, it's worth making sure inventory, staffing, and delivery capacity can keep up, a spike like that is exactly the kind of thing that could turn into a wave of late deliveries (and the bad reviews that come with them) if it's not planned for.