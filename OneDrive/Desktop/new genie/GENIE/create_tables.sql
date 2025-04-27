CREATE TABLE IF NOT EXISTS trade_logs (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP,
    broker TEXT,
    symbol TEXT,
    side TEXT,
    qty INTEGER,
    price NUMERIC,
    status TEXT,
    latency NUMERIC
);