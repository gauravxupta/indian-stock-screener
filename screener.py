"""
Screener Logic — Applies fundamental filters to the stock DataFrame.
"""

import pandas as pd


def apply_filters(
    df: pd.DataFrame,
    pe_range: tuple[float, float] | None = None,
    pb_range: tuple[float, float] | None = None,
    roe_min: float | None = None,
    de_max: float | None = None,
    rev_growth_min: float | None = None,
    mcap_min: float | None = None,
    div_yield_min: float | None = None,
    profit_margin_min: float | None = None,
    sectors: list[str] | None = None,
) -> pd.DataFrame:
    """
    Filter the DataFrame based on fundamental parameters.
    Returns a new filtered DataFrame.
    """
    filtered = df.copy()

    # P/E range
    if pe_range is not None:
        filtered = filtered[
            (filtered["P/E"].notna())
            & (filtered["P/E"] >= pe_range[0])
            & (filtered["P/E"] <= pe_range[1])
        ]

    # P/B range
    if pb_range is not None:
        filtered = filtered[
            (filtered["P/B"].notna())
            & (filtered["P/B"] >= pb_range[0])
            & (filtered["P/B"] <= pb_range[1])
        ]

    # Minimum ROE
    if roe_min is not None and roe_min > 0:
        filtered = filtered[
            (filtered["ROE (%)"].notna()) & (filtered["ROE (%)"] >= roe_min)
        ]

    # Maximum Debt-to-Equity
    if de_max is not None and de_max < 500:
        filtered = filtered[
            (filtered["Debt/Equity"].notna()) & (filtered["Debt/Equity"] <= de_max)
        ]

    # Minimum Revenue Growth
    if rev_growth_min is not None and rev_growth_min > -100:
        filtered = filtered[
            (filtered["Revenue Growth (%)"].notna())
            & (filtered["Revenue Growth (%)"] >= rev_growth_min)
        ]

    # Minimum Market Cap (in Cr)
    if mcap_min is not None and mcap_min > 0:
        filtered = filtered[
            (filtered["Market Cap (Cr)"].notna())
            & (filtered["Market Cap (Cr)"] >= mcap_min)
        ]

    # Minimum Dividend Yield
    if div_yield_min is not None and div_yield_min > 0:
        filtered = filtered[
            (filtered["Dividend Yield (%)"].notna())
            & (filtered["Dividend Yield (%)"] >= div_yield_min)
        ]

    # Minimum Profit Margin
    if profit_margin_min is not None and profit_margin_min > -100:
        filtered = filtered[
            (filtered["Profit Margin (%)"].notna())
            & (filtered["Profit Margin (%)"] >= profit_margin_min)
        ]

    # Sector filter
    if sectors and len(sectors) > 0:
        filtered = filtered[filtered["Sector"].isin(sectors)]

    return filtered.reset_index(drop=True)
