import pandas as pd
import sqlite3
import os
import time
import sys

BASE = os.path.expanduser("~/mnt/Documents/airline-delay-sql-project/data")
DB_PATH = os.path.join(BASE, "flights.db")
PROGRESS_PATH = os.path.join(BASE, ".flights_progress")

FLIGHTS_DTYPES = {
    "YEAR": "Int32", "MONTH": "Int32", "DAY": "Int32", "DAY_OF_WEEK": "Int32",
    "AIRLINE": "object", "FLIGHT_NUMBER": "Int32", "TAIL_NUMBER": "object",
    "ORIGIN_AIRPORT": "object", "DESTINATION_AIRPORT": "object",
    "SCHEDULED_DEPARTURE": "Int32", "DEPARTURE_TIME": "Int32", "DEPARTURE_DELAY": "Int32",
    "TAXI_OUT": "Int32", "WHEELS_OFF": "Int32", "SCHEDULED_TIME": "Int32",
    "ELAPSED_TIME": "Int32", "AIR_TIME": "Int32", "DISTANCE": "Int32",
    "WHEELS_ON": "Int32", "TAXI_IN": "Int32", "SCHEDULED_ARRIVAL": "Int32",
    "ARRIVAL_TIME": "Int32", "ARRIVAL_DELAY": "Int32", "DIVERTED": "Int32",
    "CANCELLED": "Int32", "CANCELLATION_REASON": "object",
    "AIR_SYSTEM_DELAY": "Int32", "SECURITY_DELAY": "Int32", "AIRLINE_DELAY": "Int32",
    "LATE_AIRCRAFT_DELAY": "Int32", "WEATHER_DELAY": "Int32",
}

CHUNK_SIZE = 500_000
TIME_BUDGET = 140  # seconds, leaving margin under the 180s call cap

def setup_small_tables(conn):
    airlines = pd.read_csv(os.path.join(BASE, "airlines.csv"))
    airlines.to_sql("airlines", conn, if_exists="replace", index=False)
    airports = pd.read_csv(os.path.join(BASE, "airports.csv"))
    airports.to_sql("airports", conn, if_exists="replace", index=False)
    print(f"airlines: {len(airlines)} rows, airports: {len(airports)} rows", flush=True)

def get_start_row():
    if os.path.exists(PROGRESS_PATH):
        with open(PROGRESS_PATH) as f:
            return int(f.read().strip())
    return 0

def save_progress(n):
    with open(PROGRESS_PATH, "w") as f:
        f.write(str(n))

def main():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA journal_mode=OFF")
    conn.execute("PRAGMA synchronous=OFF")

    start_row = get_start_row()
    if start_row == 0:
        setup_small_tables(conn)

    t0 = time.time()
    reader = pd.read_csv(
        os.path.join(BASE, "flights.csv"),
        dtype=FLIGHTS_DTYPES,
        skiprows=range(1, start_row + 1) if start_row > 0 else None,
        chunksize=CHUNK_SIZE,
    )

    rows_this_call = 0
    for chunk in reader:
        chunk.to_sql("flights", conn, if_exists="append", index=False)
        rows_this_call += len(chunk)
        start_row += len(chunk)
        save_progress(start_row)
        elapsed = time.time() - t0
        print(f"flights: +{rows_this_call:,} this call, {start_row:,} total, {elapsed:.1f}s elapsed", flush=True)
        if elapsed > TIME_BUDGET:
            print("TIME_BUDGET_HIT", flush=True)
            conn.close()
            sys.exit(0)

    conn.close()
    print("FLIGHTS_LOAD_COMPLETE", flush=True)

if __name__ == "__main__":
    main()
