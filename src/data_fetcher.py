import yfinance as yf
import pandas as pd

def fetch_stock_data(ticker: str) -> pd.DataFrame:
    """
    Fetches the full historical data for a given ticker.
    I like to work with the entire dataset so I can let users filter later.
    
    Parameters:
        ticker (str): The stock ticker symbol.
    
    Returns:
        pd.DataFrame: A dataframe with the stock's historical data.
    """
    ticker_obj = yf.Ticker(ticker)
    data = ticker_obj.history(period="max")
    # Reset index so that 'Date' becomes a column
    data.reset_index(inplace=True)
    return data
