# E-Commerce Sales Analysis (EDA Report)

**Dataset:** Olist Brazilian E-Commerce (2016–2018)
**Tools used:** Python (pandas, NumPy, Matplotlib), SQL, Tableau Public
**Note:** All figures below are for orders with status "delivered." Currency is shown with a $ sign.


## Summary

- Total revenue was $13,591,644 from 96,478 delivered orders. The average order value was $137.04.
- Sao Paulo(SP) brought in more revenue than any other state, $5,067,633 from 46,448 orders. That's 38.32% of all revenue, almost 3 times more than the next state, Rio de Janeiro.
- The top category depends on how you measure it: health_beauty has the most total revenue, bed_bath_table has the most orders, and computers has the highest average price per order.
- Deliveries are usually early. On average, orders arrive 11.88 days before the estimated date, and only 6.77% of orders are late.
- Very few customers buy more than once, only 3.00% (2,801 out of 93,358) placed a second order.
- Orders that arrive on time or early get better reviews (4.28 stars on average) than late orders (2.57 stars). The correlation between delay and review score is -0.327.
- Revenue spiked on November 24, 2017, Black Friday in Brazil, reaching $152,653.74 in a single day, about 2.5 times the next-highest day that month.


## 1. How the analysis was done

- Looked through all 9 raw data tables and checked for missing values, duplicates, and data types.
- Cleaned the data: converted date columns properly, handled missing values, and removed duplicate geolocation rows (went from about 1 million rows down to about 19,000).
- Most of this report only looks at orders marked "delivered," since that's also how the Tableau dashboard numbers are calculated.
- Every main number was double-checked two more times, once in SQL and once in Tableau, to make sure everything matched.


## 2. Revenue Over Time

 Total Revenue: $13,591,644 
 Total Delivered Orders: 96,478
 Average Order Value: $137.04

Revenue grew steadily from late 2016 through 2018. There's one clear spike in November 2017.

**What happened:** On November 24, 2017, revenue hit $152,653.74 in a single day about 2.5 times higher than the next highest day that month (Nov 25, $60,923.48), and 3–4 times a normal November day. That date is Black Friday in Brazil, which explains the spike.


## 3. Product Categories

No single category wins on every measure it depends on what you're counting.

**Top 10 by revenue:**
1. health_beauty
2. watches_gifts
3. bed_bath_table
4. sports_leisure
5. computers_accessories
6. furniture_decor
7. housewares
8. cool_stuff
9. auto
10. toys

**Top 10 by number of orders:**
1. bed_bath_table
2. health_beauty
3. sports_leisure
4. furniture_decor
5. computers_accessories
6. housewares
7. watches_gifts
8. telephony
9. garden_tools
10. auto

**Top 10 by average price per order:**
1. computers 
2. small_appliances_home_oven_and_coffee
3. home_appliances_2
4. agro_industry_and_commerce
5. musical_instruments
6. small_appliances
7. fixed_telephony
8. construction_tools_safety
9. watches_gifts 
10. furniture_bedroom

**What this means:** computers has the highest average order value by far over 5 times higher than watches_gifts, the 9th highest. But computers doesn't even show up in the top 10 by total revenue, since it sells in low volume. So bed_bath_table wins on order count, health_beauty wins on total revenue, and computers wins on price per order, three different categories depending on what you're measuring.


## 4. Revenue by State

Top 10 states by revenue, in order: SP, RJ, MG, RS, PR, SC, BA, DF, GO, ES

| State | Revenue | Orders |
|---|---|---|
| SP (São Paulo) | $5,067,633 | 46,448 |
| RJ (Rio de Janeiro) | $1,758,651 | 14,143 |

**What this means:** Sao Paulo brings in far more revenue and orders than any other state, almost 3 times more than Rio de Janeiro, the second-highest. SP alone makes up 38.32% of total revenue.


## 5. Delivery Times

 Average delay vs. estimated date: -11.88 days (delivered 11.88 days early, on average)
 Average time from purchase to delivery: about 12 days
 Orders delivered late: 6.77%
 Orders delivered on time or early: 93.23%
 Earliest delivery: 147 days before estimate
 Latest delivery: 188 days after estimate

**What this means:** Most orders arrive well before the estimated delivery date. Only about 1 in 15 orders (6.77%) are late. A few orders in the data are extreme outliers, some 188 days late, some 147 days early.


## 6. Customer Behavior

 Total unique customers: 93,358
 Customers who ordered more than once: 2,801 
 Repeat purchase rate: 3.00%
 Average order value: $137.04

**What this means:** Almost all customers only buy once. Just 3.00% of customers placed a second order.


## 7. Reviews

Review scores form a pattern where most customers leave either a very high or very low score, and fewer leave a score in the middle.

 5 stars: ~57,000
 4 stars: ~19,000
 3 stars: fewer
 2 stars: fewer
 1 star: ~11,000

**What this means:** 5-star reviews are the most common, followed by 4-star. There's also a smaller spike at 1-star. Orders delivered on time or early got an average review score of 4.28, while late orders averaged 2.57. The correlation between delay and review score is -0.327, meaning later deliveries tend to go along with lower scores.


## Data & Tools

- **Data:** Olist Brazilian E-Commerce dataset, orders, order items, payments, reviews, customers, products, sellers, geolocation, and product category tables.
- **Tools:** Python (pandas, NumPy, Matplotlib) for the analysis, SQL for double-checking the numbers, Tableau Public for the dashboard.
- **Filter used throughout:** only orders with status "delivered," unless stated otherwise.