import pandas as pd

def process_data(data: pd.DataFrame, ma_window: int = 50) -> pd.DataFrame:
    """
    Processes the raw stock data by adding daily returns and a moving average.
    
    Parameters:
        data (pd.DataFrame): The raw stock data with a 'Close' column.
        ma_window (int): The window size for the moving average (default is 50 days).
    
    Returns:
        pd.DataFrame: The data with new columns 'Daily Return' and 'MA'.
    """
    # Calculate daily percentage change in the closing price
    data['Daily Return'] = data['Close'].pct_change()
    # Calculate the moving average on the closing price
    data['MA'] = data['Close'].rolling(window=ma_window).mean()
    return data
