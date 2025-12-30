# 📈 Personal Portfolio Analytics Dashboard

A Python-based automated pipeline to track personal investment performance, specifically designed for **DEGIRO** transaction logs. This project ingests raw broker data to calculate risk-adjusted returns and benchmark performance against global indices.

## 🚀 Key Features
* **Automated ETL Pipeline:** Cleans and normalizes raw CSV exports (handling European date formats, currency conversion, and missing values).
* **Performance Metrics:** Calculates **Time-Weighted Returns (TWR)** to accurately track performance regardless of deposits/withdrawals.
* **Benchmarking:** Dynamic comparison against **S&P 500 (^GSPC)** and **MSCI World** via Yahoo Finance API.
* **Risk Analysis:** Computes Portfolio Beta, Volatility, and Drawdowns.

## 🛠️ Technologies
* **Python 3.10+**
* **Pandas & NumPy:** For vectorised data manipulation and time-series analysis.
* **Matplotlib & Seaborn:** For visualization of equity curves and exposure heatmaps.
* **YFinance:** API integration for real-time benchmark data.

## 📂 Project Structure
```text
portfolio-analytics/
├── data/
│   ├── example_transactions.csv  <-- Place your DEGIRO export here
├── notebooks/
│   └── portfolio_analysis.ipynb  <-- Main analysis script
├── .gitignore                    <-- Ensures private data is NOT uploaded
├── README.md
└── requirements.txt
