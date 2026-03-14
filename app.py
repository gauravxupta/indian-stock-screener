"""
Indian Stock Screener — Streamlit Dashboard
A premium, dark-themed fundamental screener for NSE-listed stocks.
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from data_fetcher import fetch_fundamentals
from screener import apply_filters
from nse_stocks import SECTORS

# ─── Page Config ──────────────────────────────────────────
st.set_page_config(
    page_title="Indian Stock Screener",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─── Custom CSS for premium dark UI ──────────────────────
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');

    /* ── Global ── */
    .stApp {
        font-family: 'Inter', sans-serif;
    }

    /* ── Header ── */
    .hero-header {
        background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
        border-radius: 16px;
        padding: 2rem 2.5rem;
        margin-bottom: 1.5rem;
        border: 1px solid rgba(255,255,255,0.08);
        box-shadow: 0 8px 32px rgba(0,0,0,0.3);
    }
    .hero-header h1 {
        font-size: 2.2rem;
        font-weight: 800;
        background: linear-gradient(90deg, #00f5a0, #00d9f5);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0 0 0.3rem 0;
        letter-spacing: -0.5px;
    }
    .hero-header p {
        color: rgba(255,255,255,0.6);
        font-size: 0.95rem;
        margin: 0;
        font-weight: 400;
    }

    /* ── KPI Cards ── */
    .kpi-container {
        display: flex;
        gap: 1rem;
        margin-bottom: 1.5rem;
        flex-wrap: wrap;
    }
    .kpi-card {
        flex: 1;
        min-width: 180px;
        background: linear-gradient(145deg, rgba(30,30,50,0.9), rgba(20,20,40,0.95));
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 14px;
        padding: 1.3rem 1.5rem;
        box-shadow: 0 4px 20px rgba(0,0,0,0.2);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    .kpi-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 30px rgba(0,0,0,0.35);
    }
    .kpi-label {
        font-size: 0.75rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1px;
        color: rgba(255,255,255,0.45);
        margin-bottom: 0.4rem;
    }
    .kpi-value {
        font-size: 1.75rem;
        font-weight: 800;
        letter-spacing: -0.5px;
    }
    .kpi-green { color: #00f5a0; }
    .kpi-blue { color: #00d9f5; }
    .kpi-purple { color: #c084fc; }
    .kpi-amber { color: #fbbf24; }

    /* ── Section Headers ── */
    .section-header {
        font-size: 1.15rem;
        font-weight: 700;
        color: rgba(255,255,255,0.9);
        margin: 1.5rem 0 0.8rem 0;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid rgba(0,245,160,0.3);
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }

    /* ── Sidebar ── */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0f0c29 0%, #1a1a3e 100%);
    }
    section[data-testid="stSidebar"] .stMarkdown h2 {
        font-size: 1rem;
        font-weight: 700;
        color: #00f5a0;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        margin-top: 1rem;
    }

    /* ── Table styling ── */
    .dataframe {
        font-size: 0.85rem !important;
    }

    /* ── Footer ── */
    .footer-text {
        text-align: center;
        color: rgba(255,255,255,0.3);
        font-size: 0.75rem;
        margin-top: 2rem;
        padding: 1rem;
    }

    /* hide streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)


# ─── Header ──────────────────────────────────────────────
st.markdown("""
<div class="hero-header">
    <h1>📈 Indian Stock Screener</h1>
    <p>Real-time fundamental analysis of 120+ NSE-listed stocks · Powered by Yahoo Finance</p>
</div>
""", unsafe_allow_html=True)


# ─── Load Data ───────────────────────────────────────────
with st.spinner("🔄 Fetching live market data... (first load may take 2-3 minutes)"):
    df_all = fetch_fundamentals()

if df_all.empty:
    st.error("❌ Could not fetch any stock data. Check your internet connection and try again.")
    st.stop()


# ─── Sidebar Filters ────────────────────────────────────
with st.sidebar:
    st.markdown("## 🎯 Filters")

    st.markdown("## Valuation")
    pe_range = st.slider(
        "P/E Ratio",
        min_value=0.0,
        max_value=200.0,
        value=(0.0, 200.0),
        step=1.0,
        help="Price-to-Earnings ratio. Lower = potentially undervalued."
    )
    pb_range = st.slider(
        "P/B Ratio",
        min_value=0.0,
        max_value=50.0,
        value=(0.0, 50.0),
        step=0.5,
        help="Price-to-Book ratio. Lower = potentially undervalued."
    )

    st.markdown("## Profitability")
    roe_min = st.slider(
        "Min ROE (%)",
        min_value=0.0,
        max_value=60.0,
        value=0.0,
        step=1.0,
        help="Return on Equity. Higher = more efficient at generating profits."
    )
    profit_margin_min = st.slider(
        "Min Profit Margin (%)",
        min_value=-50.0,
        max_value=60.0,
        value=-50.0,
        step=1.0,
        help="Net Profit Margin. Higher = more profitable."
    )

    st.markdown("## Leverage")
    de_max = st.slider(
        "Max Debt/Equity",
        min_value=0.0,
        max_value=500.0,
        value=500.0,
        step=10.0,
        help="Debt-to-Equity ratio. Lower = less leveraged."
    )

    st.markdown("## Growth")
    rev_growth_min = st.slider(
        "Min Revenue Growth (%)",
        min_value=-100.0,
        max_value=100.0,
        value=-100.0,
        step=5.0,
        help="Year-over-year revenue growth."
    )

    st.markdown("## Dividends")
    div_yield_min = st.slider(
        "Min Dividend Yield (%)",
        min_value=0.0,
        max_value=15.0,
        value=0.0,
        step=0.5,
        help="Annual dividend yield."
    )

    st.markdown("## Market Cap")
    mcap_min = st.number_input(
        "Min Market Cap (₹ Cr)",
        min_value=0,
        max_value=2000000,
        value=0,
        step=5000,
        help="Minimum market capitalization in Crores."
    )

    st.markdown("## Sector")
    available_sectors = sorted(df_all["Sector"].dropna().unique().tolist())
    selected_sectors = st.multiselect(
        "Select Sectors",
        options=available_sectors,
        default=[],
        help="Leave empty to include all sectors."
    )

    st.markdown("---")
    if st.button("🔄 Refresh Data", use_container_width=True):
        st.cache_data.clear()
        st.rerun()


# ─── Apply Filters ───────────────────────────────────────
df_filtered = apply_filters(
    df_all,
    pe_range=pe_range if pe_range != (0.0, 200.0) else None,
    pb_range=pb_range if pb_range != (0.0, 50.0) else None,
    roe_min=roe_min,
    de_max=de_max,
    rev_growth_min=rev_growth_min,
    mcap_min=mcap_min,
    div_yield_min=div_yield_min,
    profit_margin_min=profit_margin_min if profit_margin_min > -50.0 else None,
    sectors=selected_sectors if selected_sectors else None,
)


# ─── KPI Cards ───────────────────────────────────────────
total_scanned = len(df_all)
total_matched = len(df_filtered)
avg_pe = df_filtered["P/E"].mean() if not df_filtered.empty else 0
avg_roe = df_filtered["ROE (%)"].mean() if not df_filtered.empty else 0

st.markdown(f"""
<div class="kpi-container">
    <div class="kpi-card">
        <div class="kpi-label">Stocks Scanned</div>
        <div class="kpi-value kpi-blue">{total_scanned}</div>
    </div>
    <div class="kpi-card">
        <div class="kpi-label">Matches Found</div>
        <div class="kpi-value kpi-green">{total_matched}</div>
    </div>
    <div class="kpi-card">
        <div class="kpi-label">Avg P/E Ratio</div>
        <div class="kpi-value kpi-purple">{avg_pe:.1f}</div>
    </div>
    <div class="kpi-card">
        <div class="kpi-label">Avg ROE</div>
        <div class="kpi-value kpi-amber">{avg_roe:.1f}%</div>
    </div>
</div>
""", unsafe_allow_html=True)


# ─── Results Table ───────────────────────────────────────
st.markdown('<div class="section-header">📋 Screener Results</div>', unsafe_allow_html=True)

if df_filtered.empty:
    st.warning("No stocks match your current filter criteria. Try relaxing some filters.")
else:
    # Column order for display
    display_cols = [
        "Ticker", "Company", "Sector", "Price (₹)", "Market Cap (Cr)",
        "P/E", "P/B", "ROE (%)", "Debt/Equity", "Revenue Growth (%)",
        "Profit Margin (%)", "Dividend Yield (%)", "EPS (₹)",
        "52W High (₹)", "52W Low (₹)", "Beta"
    ]
    display_cols = [c for c in display_cols if c in df_filtered.columns]

    # Sortable table
    sort_col = st.selectbox(
        "Sort by",
        options=display_cols,
        index=display_cols.index("Market Cap (Cr)") if "Market Cap (Cr)" in display_cols else 0,
    )
    sort_order = st.radio("Order", ["Descending", "Ascending"], horizontal=True)

    df_display = df_filtered[display_cols].sort_values(
        by=sort_col,
        ascending=(sort_order == "Ascending"),
        na_position="last",
    ).reset_index(drop=True)

    # Style the dataframe
    def color_value(val, good_threshold, bad_threshold, higher_is_better=True):
        """Return background color based on value."""
        if pd.isna(val):
            return ""
        if higher_is_better:
            if val >= good_threshold:
                return "background-color: rgba(0,245,160,0.15); color: #00f5a0;"
            elif val <= bad_threshold:
                return "background-color: rgba(239,68,68,0.15); color: #ef4444;"
        else:
            if val <= good_threshold:
                return "background-color: rgba(0,245,160,0.15); color: #00f5a0;"
            elif val >= bad_threshold:
                return "background-color: rgba(239,68,68,0.15); color: #ef4444;"
        return ""

    def style_table(row):
        styles = [""] * len(row)
        for i, col in enumerate(row.index):
            if col == "ROE (%)":
                styles[i] = color_value(row[col], 15, 5, higher_is_better=True)
            elif col == "P/E":
                styles[i] = color_value(row[col], 15, 40, higher_is_better=False)
            elif col == "Debt/Equity":
                styles[i] = color_value(row[col], 50, 150, higher_is_better=False)
            elif col == "Revenue Growth (%)":
                styles[i] = color_value(row[col], 10, 0, higher_is_better=True)
            elif col == "Profit Margin (%)":
                styles[i] = color_value(row[col], 15, 5, higher_is_better=True)
            elif col == "Dividend Yield (%)":
                styles[i] = color_value(row[col], 2, 0, higher_is_better=True)
        return styles

    styled_df = df_display.style.apply(style_table, axis=1)
    st.dataframe(styled_df, use_container_width=True, height=500)

    # Download button
    csv = df_display.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="⬇️ Download as CSV",
        data=csv,
        file_name="screened_stocks.csv",
        mime="text/csv",
        use_container_width=True,
    )


# ─── Charts Section ──────────────────────────────────────
if not df_filtered.empty and len(df_filtered) >= 2:
    st.markdown('<div class="section-header">📊 Visual Analytics</div>', unsafe_allow_html=True)

    chart_col1, chart_col2 = st.columns(2)

    # ── Scatter: P/E vs ROE ──
    with chart_col1:
        scatter_data = df_filtered.dropna(subset=["P/E", "ROE (%)"]).copy()
        if not scatter_data.empty:
            fig_scatter = px.scatter(
                scatter_data,
                x="P/E",
                y="ROE (%)",
                size="Market Cap (Cr)",
                color="Sector",
                hover_name="Company",
                hover_data={"P/E": ":.1f", "ROE (%)": ":.1f", "Market Cap (Cr)": ":,.0f"},
                title="P/E vs ROE (bubble = Market Cap)",
                color_discrete_sequence=px.colors.qualitative.Set2,
            )
            fig_scatter.update_layout(
                template="plotly_dark",
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(15,12,41,0.8)",
                font=dict(family="Inter"),
                title_font_size=14,
                height=420,
                margin=dict(l=40, r=20, t=50, b=40),
            )
            fig_scatter.update_xaxes(gridcolor="rgba(255,255,255,0.05)")
            fig_scatter.update_yaxes(gridcolor="rgba(255,255,255,0.05)")
            st.plotly_chart(fig_scatter, use_container_width=True)

    # ── Pie: Sector Distribution ──
    with chart_col2:
        sector_counts = df_filtered["Sector"].value_counts().reset_index()
        sector_counts.columns = ["Sector", "Count"]
        fig_pie = px.pie(
            sector_counts,
            values="Count",
            names="Sector",
            title="Sector Distribution",
            color_discrete_sequence=px.colors.qualitative.Pastel,
            hole=0.45,
        )
        fig_pie.update_layout(
            template="plotly_dark",
            paper_bgcolor="rgba(0,0,0,0)",
            font=dict(family="Inter"),
            title_font_size=14,
            height=420,
            margin=dict(l=20, r=20, t=50, b=20),
            showlegend=True,
            legend=dict(font=dict(size=10)),
        )
        fig_pie.update_traces(textposition="inside", textinfo="percent+label")
        st.plotly_chart(fig_pie, use_container_width=True)

    # ── Bar: Top 10 by ROE ──
    top_roe = df_filtered.dropna(subset=["ROE (%)"]).nlargest(10, "ROE (%)")
    if not top_roe.empty:
        fig_bar = px.bar(
            top_roe,
            x="ROE (%)",
            y="Company",
            orientation="h",
            color="ROE (%)",
            color_continuous_scale=["#302b63", "#00f5a0"],
            title="🏆 Top 10 Stocks by ROE",
            hover_data={"P/E": ":.1f", "Debt/Equity": ":.1f"},
        )
        fig_bar.update_layout(
            template="plotly_dark",
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(15,12,41,0.8)",
            font=dict(family="Inter"),
            title_font_size=14,
            height=400,
            margin=dict(l=150, r=20, t=50, b=40),
            yaxis=dict(autorange="reversed"),
            coloraxis_showscale=False,
        )
        fig_bar.update_xaxes(gridcolor="rgba(255,255,255,0.05)")
        fig_bar.update_yaxes(gridcolor="rgba(255,255,255,0.05)")
        st.plotly_chart(fig_bar, use_container_width=True)

    # ── Bar: Top 10 by Revenue Growth ──
    top_rev = df_filtered.dropna(subset=["Revenue Growth (%)"]).nlargest(10, "Revenue Growth (%)")
    if not top_rev.empty:
        fig_rev = px.bar(
            top_rev,
            x="Revenue Growth (%)",
            y="Company",
            orientation="h",
            color="Revenue Growth (%)",
            color_continuous_scale=["#24243e", "#00d9f5"],
            title="🚀 Top 10 Stocks by Revenue Growth",
            hover_data={"P/E": ":.1f", "Market Cap (Cr)": ":,.0f"},
        )
        fig_rev.update_layout(
            template="plotly_dark",
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(15,12,41,0.8)",
            font=dict(family="Inter"),
            title_font_size=14,
            height=400,
            margin=dict(l=150, r=20, t=50, b=40),
            yaxis=dict(autorange="reversed"),
            coloraxis_showscale=False,
        )
        fig_rev.update_xaxes(gridcolor="rgba(255,255,255,0.05)")
        fig_rev.update_yaxes(gridcolor="rgba(255,255,255,0.05)")
        st.plotly_chart(fig_rev, use_container_width=True)


# ─── Data Quality Note ───────────────────────────────────
with st.expander("ℹ️ About This Screener"):
    st.markdown("""
    **Data Source**: Yahoo Finance via `yfinance` library.

    **Fundamental Metrics**:
    | Metric | Description |
    |--------|-------------|
    | **P/E** | Price-to-Earnings — lower may indicate undervaluation |
    | **P/B** | Price-to-Book — compares market price to book value |
    | **ROE** | Return on Equity — measures profitability vs shareholder equity |
    | **Debt/Equity** | Leverage ratio — lower means less debt-dependent |
    | **Revenue Growth** | Year-over-year top-line growth |
    | **Profit Margin** | Net income as % of revenue |
    | **Dividend Yield** | Annual dividends as % of stock price |

    **Color Coding**:
    - 🟢 **Green** = Fundamentally strong (high ROE, low D/E, good margins)
    - 🔴 **Red** = Needs caution (high P/E, high debt, low margins)

    **Refresh**: Data is cached for 30 minutes. Click "Refresh Data" in the sidebar to fetch latest.

    **Disclaimer**: This tool is for educational and informational purposes only. Not financial advice.
    """)


# ─── Footer ──────────────────────────────────────────────
st.markdown("""
<div class="footer-text">
    Built with ❤️ using Streamlit & yfinance · Data from Yahoo Finance · For educational purposes only
</div>
""", unsafe_allow_html=True)
