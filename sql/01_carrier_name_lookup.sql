-- Q1: Carrier name lookup
-- Business question: flight-level records only store the 2-letter carrier
-- code (e.g. "AA"), which means nothing to a non-aviation reader. Join to
-- the airlines lookup table so every row carries the full carrier name
-- alongside the code.
--
-- This is deliberately the simplest query in the project — it exists to
-- confirm the join key (flights.AIRLINE = airlines.IATA_CODE) actually
-- matches before building anything more complex on top of it.

SELECT f.AIRLINE AS carrier_code, a.AIRLINE AS carrier_name
FROM flights f
JOIN airlines a ON f.AIRLINE = a.IATA_CODE;
