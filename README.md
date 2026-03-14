# Indian Stock Screener 📈

A premium Streamlit dashboard that screens **120+ NSE-listed Indian stocks** on fundamental parameters in real-time, powered by Yahoo Finance data.

![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.55+-red?logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-green)

## ✨ Features

- **Real-time Data** — Live fundamentals from Yahoo Finance via `yfinance`
- **9 Filters** — P/E, P/B, ROE, Debt/Equity, Revenue Growth, Profit Margin, Dividend Yield, Market Cap, Sector
- **Color-coded Table** — Green = strong, Red = caution; sortable by any column
- **4 Interactive Charts** — P/E vs ROE scatter, Sector donut, Top ROE bar, Top Revenue Growth bar
- **CSV Export** — Download filtered results with one click
- **Smart Caching** — 30-minute data cache for fast reloads

## 🚀 Quick Start

```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/indian-stock-screener.git
cd indian-stock-screener

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

Open `http://localhost:8501` in your browser.

## 📁 Project Structure

```
├── app.py              # Streamlit dashboard (UI + charts)
├── data_fetcher.py     # yfinance data layer with caching
├── screener.py         # Fundamental filter logic
├── nse_stocks.py       # Curated list of 120+ NSE tickers
└── requirements.txt    # Python dependencies
```

## 📊 Filters Available

| Filter | Description |
|--------|-------------|
| P/E Ratio | Price-to-Earnings (lower = potentially undervalued) |
| P/B Ratio | Price-to-Book value |
| ROE (%) | Return on Equity — profitability measure |
| Debt/Equity | Leverage ratio (lower = less debt) |
| Revenue Growth (%) | Year-over-year top-line growth |
| Profit Margin (%) | Net income as % of revenue |
| Dividend Yield (%) | Annual dividends as % of price |
| Market Cap (₹ Cr) | Minimum market capitalization |
| Sector | Multi-select industry filter |

## ⚠️ Disclaimer

This tool is for **educational and informational purposes only**. It is not financial advice. Always do your own research before making investment decisions.

## 📄 License

MIT License — feel free to use and modify.
