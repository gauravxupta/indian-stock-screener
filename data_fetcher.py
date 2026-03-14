"""
Data Fetcher — Pulls fundamental data for NSE stocks via yfinance.
Uses Streamlit's caching for performance.
"""

import pandas as pd
import yfinance as yf
import streamlit as st
from nse_stocks import TICKERS, STOCK_INFO


@st.cache_data(ttl=1800, show_spinner=False)  # Cache for 30 minutes
def fetch_fundamentals(tickers: list[str] | None = None) -> pd.DataFrame:
    """
    Fetch fundamental data for a list of NSE tickers.
    Returns a cleaned pandas DataFrame with one row per stock.
    """
    if tickers is None:
        tickers = TICKERS

    records = []
    for ticker_symbol in tickers:
        try:
            ticker = yf.Ticker(ticker_symbol)
            info = ticker.info

            if not info or info.get("regularMarketPrice") is None:
                continue

            name, sector = STOCK_INFO.get(ticker_symbol, (ticker_symbol, "Unknown"))

            records.append({
                "Ticker": ticker_symbol.replace(".NS", ""),
                "Company": name,
                "Sector": sector,
                "Price (₹)": _safe_get(info, "currentPrice", "regularMarketPrice"),
                "Market Cap (Cr)": _safe_divide(info.get("marketCap"), 1e7),
                "P/E": _safe_get(info, "trailingPE"),
                "Forward P/E": _safe_get(info, "forwardPE"),
                "P/B": _safe_get(info, "priceToBook"),
                "ROE (%)": _safe_multiply(info.get("returnOnEquity"), 100),
                "Debt/Equity": _safe_get(info, "debtToEquity"),
                "Revenue Growth (%)": _safe_multiply(info.get("revenueGrowth"), 100),
                "Earnings Growth (%)": _safe_multiply(info.get("earningsGrowth"), 100),
                "Dividend Yield (%)": _safe_multiply(info.get("dividendYield"), 100),
                "EPS (₹)": _safe_get(info, "trailingEps"),
                "Book Value (₹)": _safe_get(info, "bookValue"),
                "52W High (₹)": _safe_get(info, "fiftyTwoWeekHigh"),
                "52W Low (₹)": _safe_get(info, "fiftyTwoWeekLow"),
                "Beta": _safe_get(info, "beta"),
                "Profit Margin (%)": _safe_multiply(info.get("profitMargins"), 100),
                "Operating Margin (%)": _safe_multiply(info.get("operatingMargins"), 100),
            })

        except Exception:
            # Skip stocks that fail — network issues, delisted, etc.
            continue

    df = pd.DataFrame(records)

    # Round numeric columns
    numeric_cols = df.select_dtypes(include="number").columns
    df[numeric_cols] = df[numeric_cols].round(2)

    return df


# ─── Helper functions ──────────────────────────────────────

def _safe_get(info: dict, *keys):
    """Return the first non-None value from the given keys."""
    for key in keys:
        val = info.get(key)
        if val is not None:
            return val
    return None


def _safe_divide(value, divisor):
    """Safely divide, returning None on failure."""
    if value is not None:
        try:
            return value / divisor
        except (TypeError, ZeroDivisionError):
            return None
    return None


def _safe_multiply(value, multiplier):
    """Safely multiply (e.g. 0.15 → 15%), returning None on failure."""
    if value is not None:
        try:
            return value * multiplier
        except TypeError:
            return None
    return None
