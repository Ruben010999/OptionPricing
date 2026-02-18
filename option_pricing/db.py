import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "data" / "option_pricing.db"


def get_connection():
    """
    Return a sqlite3.Connection to the option_pricing database.

    The connection uses sqlite3.Row as row factory so columns can be
    accessed by name.
    """
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


SCHEMA_SQL = """
CREATE TABLE IF NOT EXISTS assets (
    symbol TEXT PRIMARY KEY,
    name   TEXT,
    type   TEXT CHECK (type IN ('STOCK', 'INDEX', 'ETF')) NOT NULL
);

CREATE TABLE IF NOT EXISTS asset_prices (
    symbol TEXT NOT NULL,
    date   DATE NOT NULL,
    close  REAL NOT NULL,
    PRIMARY KEY (symbol, date),
    FOREIGN KEY (symbol) REFERENCES assets(symbol)
);

CREATE TABLE IF NOT EXISTS option_quotes (
    id                INTEGER PRIMARY KEY AUTOINCREMENT,
    underlying_symbol TEXT NOT NULL,
    quote_date        DATE NOT NULL,
    expiration_date   DATE NOT NULL,
    strike            REAL NOT NULL,
    option_type       TEXT CHECK (option_type IN ('CALL', 'PUT')) NOT NULL,
    bid               REAL,
    ask               REAL,
    mid               REAL,
    underlying_price  REAL NOT NULL,
    risk_free_rate    REAL NOT NULL,
    dividend_yield    REAL DEFAULT 0.0,
    source            TEXT,
    UNIQUE (underlying_symbol, quote_date, expiration_date, strike, option_type),
    FOREIGN KEY (underlying_symbol) REFERENCES assets(symbol)
);
"""


def ensure_schema():
    """Create all required tables if they do not exist yet."""
    conn = get_connection()
    try:
        conn.executescript(SCHEMA_SQL)
        conn.commit()
    finally:
        conn.close()

if __name__ == "__main__":
    from pprint import pprint

    print("DB_PATH =", DB_PATH)
    ensure_schema()
    print("Schema ensured.")
