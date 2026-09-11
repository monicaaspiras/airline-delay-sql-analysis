# Airline Delay Analysis — Root Cause & Ops Efficiency (SQL Portfolio Project)

**Author:** Monica "Nica" Aspiras | [LinkedIn](www.linkedin.com/in/monicaaspiras)

## The business question

U.S. domestic flight delays cost airlines billions annually in crew overtime, missed connections, and
gate/rebooking costs. This project asks: **which carriers, airports, and time windows drive the most
delay, and is the root cause weather, carrier operations, or air-traffic/system congestion?**

That framing matters — it's the same kind of root-cause-before-solution question I ask on the operations
side at Starbucks (why is a shift running behind — short-staffed, slow equipment, or demand spike?) and
the kind Boeing's Methods & Process Analysts ask on the production floor. This project is that same
discipline applied to a public dataset.

## Dataset

[2015 Flight Delays and Cancellations](https://www.kaggle.com/datasets/usdot/flight-delays) — U.S.
Department of Transportation, via Kaggle. Three relational tables:

| Table | Rows | Description |
|---|---|---|
| `flights.csv` | ~5.8M | One row per flight: carrier, origin/dest airport, scheduled vs. actual times, delay reason codes |
| `airlines.csv` | 14 | Carrier code → carrier name lookup |
| `airports.csv` | ~320 | Airport code → name, city, state, lat/long |

Chosen deliberately over a single flat CSV — it forces real `JOIN` logic across carrier and airport
codes, which is what most "portfolio" datasets (Titanic, Iris) don't require.

## Tools

SQL (SQLite for local dev — portable, zero setup), Python (pandas, for the CSV → DB load step),
Tableau (for the visual layer, TBD).

## Project structure

```
airline-delay-sql-project/
├── data/            # raw CSVs (not committed — see .gitignore) + a data dictionary
├── sql/             # .sql files, one per analysis question, numbered in build order
├── notebooks/        # Python notebook: load CSVs into SQLite, sanity-check row counts
├── images/          # exported chart screenshots for the README/writeup
└── README.md
```

## Key questions this project answers

*(filled in as the analysis is built — see `sql/` for the queries and `ANALYSIS.md` for the write-up)*

1. Which carriers have the worst on-time performance, and does that hold after controlling for which
   airports they fly out of? (a carrier flying mostly out of O'Hare *should* look worse — is it the
   carrier or the airport?)
2. What share of total delay-minutes is weather vs. carrier vs. NAS (system/congestion) vs. security vs.
   late-aircraft, and does that split change by season?
3. Which specific routes (origin→destination pairs) are the most consistently delayed — worth flagging
   as candidates for schedule padding?
4. Is there a meaningful day-of-week or time-of-day pattern, and does it match the "cascading delay"
   pattern (late-aircraft delay compounding later in the day)?
5. Which airports have the worst *taxi-out* time specifically (a proxy for ground congestion, distinct
   from weather or carrier issues)?

## Findings

*(TBD — written up after the SQL analysis is complete, with supporting numbers and a chart per finding)*

## How to reproduce

1. Download the three CSVs from the [Kaggle dataset page](https://www.kaggle.com/datasets/usdot/flight-delays)
   into `data/`.
2. Run `notebooks/load_to_sqlite.ipynb` to build `flights.db`.
3. Run the queries in `sql/` in order against `flights.db`.
