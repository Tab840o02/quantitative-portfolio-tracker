import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# ==========================================
# ⚙️ CONFIGURATION (USER EDITABLE)
# ==========================================
# Path to your DEGIRO export file (CSV)
INPUT_FILE = 'data/Transactions.csv' 

# Benchmark Ticker (e.g., ^GSPC for S&P 500, URTH for MSCI World)
BENCHMARK_TICKER = '^GSPC' 

# Your Account Currency (for currency conversion)
BASE_CURRENCY = 'EUR'

# Plot Style
plt.style.use('seaborn-v0_8-darkgrid')
# ==========================================

def load_and_clean_data(filepath):
    """
    Ingests raw DEGIRO transaction logs and normalizes data types.
    Handles European decimal formatting (commas to dots).
    """
    try:
        df = pd.read_csv(filepath)
    except FileNotFoundError:
        print(f"❌ Error: File not found at {filepath}. Please check the path.")
        return None

    # Standardize Column Names (Adjust based on your specific export language)
    # DEGIRO exports often vary by language. This map standardizes them to English.
    column_map = {
        'Datum': 'Date', 'Date': 'Date',
        'Tijd': 'Time', 'Time': 'Time',
        'Product': 'Product',
        'ISIN': 'ISIN',
        'Aantal': 'Quantity', 'Quantity': 'Quantity',
        'Koers': 'Price', 'Price': 'Price',
        'Lokale waarde': 'Local Value', 'Local value': 'Local Value',
        'Waarde': 'Value', 'Value': 'Value',
        'Totaal': 'Total', 'Total': 'Total'
    }
    df = df.rename(columns=column_map)

    # Convert European numeric formats (e.g., "1.000,00" -> 1000.00)
    cols_to_fix = ['Quantity', 'Price', 'Local Value', 'Value', 'Total']
    for col in cols_to_fix:
        if col in df.columns:
            if df[col].dtype == 'object':
                df[col] = df[col].astype(str).str.replace('.', '', regex=False).str.replace(',', '.', regex=False)
                df[col] = pd.to_numeric(df[col], errors='coerce')

    # Parse Dates
    if 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)  # DEGIRO uses DD-MM-YYYY

    return df

def get_portfolio_snapshot(df):
    """
    Reconstructs current portfolio holdings from transaction history.
    """
    # Filter for Buy/Sell transactions
    trades = df.dropna(subset=['ISIN', 'Quantity'])
    
    # Group by ISIN to get current holdings
    holdings = trades.groupby(['Product', 'ISIN'])['Quantity'].sum().reset_index()
    holdings = holdings[holdings['Quantity'] > 0]  # Remove closed positions
    
    return holdings

def fetch_market_data(holdings, benchmark):
    """
    Downloads historical price data for holdings and benchmark using YFinance.
    Note: Requires mapping ISINs to Tickers (Manual step often required for proper YFinance mapping).
    """
    print(f"⬇️ Downloading market data for {len(holdings)} positions and benchmark...")
    
    # For demonstration, we assume 'Product' column contains Tickers or we use a placeholder.
    # In a real scenario, you need a dictionary to map ISIN -> Ticker (e.g., US0378331005 -> AAPL)
    # Here we simply download the Benchmark for comparison logic
    
    start_date = '2023-01-01' # Adjust dynamic based on your data
    market_data = yf.download(benchmark, start=start_date)['Adj Close']
    
    return market_data

def calculate_metrics(market_data):
    """
    Calculates returns, volatility and drawdown.
    """
    returns = market_data.pct_change().dropna()
    cumulative_returns = (1 + returns).cumprod()
    
    # Max Drawdown
    rolling_max = cumulative_returns.cummax()
    drawdown = cumulative_returns / rolling_max - 1
    max_drawdown = drawdown.min()
    
    return cumulative_returns, max_drawdown

def main():
    print("🚀 Starting Portfolio Analytics...")
    
    # 1. Load Data
    df = load_and_clean_data(INPUT_FILE)
    if df is None: return

    # 2. Get Holdings
    holdings = get_portfolio_snapshot(df)
    print(f"✅ Loaded {len(df)} transactions. Current positions: {len(holdings)}")
    print(holdings[['Product', 'Quantity']])

    # 3. Market Analysis (Benchmark)
    benchmark_data = fetch_market_data(holdings, BENCHMARK_TICKER)
    cum_returns, max_dd = calculate_metrics(benchmark_data)

    # 4. Visualize
    plt.figure(figsize=(12, 6))
    cum_returns.plot(title=f'Benchmark Performance ({BENCHMARK_TICKER})', label='Benchmark')
    plt.ylabel('Cumulative Return')
    plt.legend()
    plt.show()

    print(f"📊 Analysis Complete. Max Drawdown: {max_dd:.2%}")

if __name__ == "__main__":
    main()
