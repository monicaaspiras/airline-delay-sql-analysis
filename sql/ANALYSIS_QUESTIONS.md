# Query build order

Numbered so the .sql files in this folder build in a sensible order — each one somewhat more advanced
than the last. Do them in order; don't skip to window functions before the joins are solid.

## Tier 1 — Joins & filtering (foundation)

1. **Carrier name lookup** — join `flights` to `airlines` so every row shows the full carrier name, not
   just the 2-letter code. (Trivial on purpose — confirms your join keys match before anything harder.)
2. **Worst airports by average departure delay** — join `flights` to `airports` on origin airport code,
   `GROUP BY` airport, `AVG(departure_delay)`, filter to airports with a minimum flight count (a small
   airport with 3 flights and 2 delays will otherwise dominate a naive average — this is a real judgment
   call worth stating explicitly in your write-up).
3. **On-time percentage by carrier** — `CASE WHEN departure_delay <= 0 THEN 1 ELSE 0 END`, averaged per
   carrier. This is the headline "which airline is worst" number, but framed as a rate, not a raw count.

## Tier 2 — Aggregation depth

4. **Delay cause breakdown** — the dataset has separate delay-minute columns for weather, carrier,
   late-aircraft, NAS, security. Sum each by month to see if the cause mix shifts seasonally (hypothesis:
   weather delay share spikes in winter).
5. **Route-level consistency** — `GROUP BY` origin + destination, `AVG` and `STDDEV`-equivalent (SQLite
   lacks native STDDEV — either compute via `AVG((x-avg)^2)` subquery or note the limitation and do this
   part in pandas) of delay. A route that's *consistently* 20 min late is a different problem than one
   that's occasionally 3 hours late.

## Tier 3 — Window functions (this is what separates a portfolio piece from a homework assignment)

6. **Rank carriers within each airport** — `RANK() OVER (PARTITION BY origin_airport ORDER BY
   avg_delay)`. Answers "is Carrier X actually bad, or just unlucky to fly out of a bad airport" —
   directly extends question 2/3.
7. **Rolling delay trend by week** — window function over ordered dates to smooth day-to-day noise and
   show a real trend line, not a jagged daily chart.
8. **Cascading delay check** — for each aircraft tail number (if present in your chosen year's columns)
   or at minimum each carrier/day, check whether delay minutes increase later in the day (`LAG()`/`LEAD()`
   over flights ordered by scheduled departure time). This is the "late-aircraft delay compounds" story —
   a good one to be able to explain out loud in an interview because it shows systems thinking, not just
   SQL syntax.

## Framing reminder for the write-up

Every query should answer a stated business question, not just demonstrate a SQL feature. When you write
the README findings section, lead with the finding ("Carrier X has 2.3x the delay rate of Carrier Y even
after controlling for airport"), not the technique ("I used a window function to..."). Hiring managers
skim for the former.
