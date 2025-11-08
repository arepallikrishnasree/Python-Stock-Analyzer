import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Konni stock tickers: AAPL (Apple), GOOGL (Google), TCS.NS (TCS India)
# Ekkada mee ishtamaina valid ticker pettandi.
TICKER = 'AAPL' 

# Past 6 months data kosam start and end dates set cheyyali
start_date = pd.to_datetime('today') - pd.DateOffset(months=6)
end_date = pd.to_datetime('today')

# Function to get stock data from Yahoo Finance
def get_stock_data(ticker):
    """Yahoo Finance nunchi stock data ni download chestundhi."""
    print(f"[INFO] Downloading data for {ticker} from {start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}...")
    
    try:
        # yf.download() will fetch the data
        # Note: auto_adjust is True by default now
        data = yf.download(ticker, start=start_date, end=end_date)
        
        if data.empty:
            print(f"[ERROR] No data found for {ticker}. Check the ticker name.")
            return None
        
        print(f"[SUCCESS] Downloaded {len(data)} days of data.")
        return data
        
    except Exception as e:
        print(f"[ERROR] Data download failed: {e}")
        return None

# Function to analyze and plot the stock price data
def plot_analysis(df, ticker):
    """Stock price and 50-Day Moving Average ni graph lo chupinchadaniki."""
    
    # 1. Data Cleaning/Preparation
    # MultiIndex undhi (e.g., (Close, AAPL)). Daanini simple 'Close' column ga cheddam.
    # yfinance updated kaabatti, ippudu direct ga 'Close' ni access cheyochu.
    close_prices = df['Close']
    
    # 2. Key Analysis: 50-Day Simple Moving Average (SMA) calculation
    # Ee line data smoothing kosam mariyu trend chudatam kosam chala mukhyam.
    # 
    df['SMA_50'] = close_prices.rolling(window=50).mean()
    
    # 3. Visualization (Graph)
    plt.figure(figsize=(12, 7)) # Graph size set cheyyadam
    
    # a. Close Price plot cheyyadam
    plt.plot(close_prices, label='Closing Price', color='blue', linewidth=1.5)
    
    # b. 50-Day SMA plot cheyyadam
    plt.plot(df['SMA_50'], label='50-Day Moving Average (SMA)', color='red', linestyle='--', linewidth=2)
    
    # Labels and Title set cheyyadam
    plt.title(f'{ticker} Stock Price and 50-Day SMA', fontsize=16)
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Price (USD)', fontsize=12)
    
    # Grid and Legend add cheyyadam
    plt.legend()
    plt.grid(True, alpha=0.6)
    
    # Graph ni chupinchali
    plt.show()

# Main Execution
if __name__ == "__main__":
    
    stock_df = get_stock_data(TICKER)
    
    if stock_df is not None:
        print("\n--- Downloaded Data Summary ---")
        print(stock_df.tail())
        
        # Analysis and Visualization function ni call cheyyadam
        plot_analysis(stock_df, TICKER)