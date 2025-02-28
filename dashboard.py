import streamlit as st
import pandas as pd

# Import our modules from the src folder
from src import data_fetcher, data_processing, visualizations

# App title and description
st.title("Enhanced Financial Data Dashboard")
st.write("This dashboard lets you explore full historical stock data with interactive charts. Use the sidebar to filter data and adjust settings.")

# Sidebar: Stock ticker input
ticker = st.sidebar.text_input("Enter Stock Ticker", value="AAPL")

if ticker:
    # Fetch the complete historical data
    data = data_fetcher.fetch_stock_data(ticker)
    
    if data.empty:
        st.error("No data found for the provided ticker. Double-check the symbol and try again.")
    else:
        # Convert the Date column to datetime and remove timezone info for consistency.
        data['Date'] = pd.to_datetime(data['Date']).dt.tz_localize(None)
        
        # Sidebar: Date range filter based on the data's min and max dates
        min_date = data['Date'].min().date()
        max_date = data['Date'].max().date()
        start_date, end_date = st.sidebar.date_input(
            "Select Date Range", 
            value=[min_date, max_date],
            min_value=min_date, 
            max_value=max_date
        )
        
        # Filter the data based on the selected date range
        mask = (data['Date'] >= pd.to_datetime(start_date)) & (data['Date'] <= pd.to_datetime(end_date))
        data = data.loc[mask].copy()
        
        # Sidebar: Moving average window slider
        ma_window = st.sidebar.slider("Moving Average Window", min_value=5, max_value=200, value=50, step=1)
        
        # Process the data to add daily returns and moving average
        data = data_processing.process_data(data, ma_window)
        
        st.subheader(f"{ticker} Stock Data from {start_date} to {end_date}")
        
        # Display interactive candlestick chart
        st.markdown("### Candlestick Chart")
        fig_candle = visualizations.create_candlestick_chart(data, ticker)
        st.plotly_chart(fig_candle, use_container_width=True)
        
        # Display closing price along with moving average line chart
        st.markdown("### Closing Price with Moving Average")
        fig_ma = visualizations.create_moving_average_chart(data, ticker, ma_window)
        st.plotly_chart(fig_ma, use_container_width=True)
        
        # Display histogram of daily returns
        st.markdown("### Daily Returns Distribution")
        fig_hist = visualizations.create_daily_returns_histogram(data)
        st.plotly_chart(fig_hist, use_container_width=True)
        
        # Display scatter plot of Volume vs. Closing Price
        st.markdown("### Volume vs. Closing Price")
        fig_scatter = visualizations.create_volume_vs_close_scatter(data)
        st.plotly_chart(fig_scatter, use_container_width=True)
        
        # Display line chart for High and Low prices
        st.markdown("### High and Low Prices Over Time")
        fig_high_low = visualizations.create_high_low_chart(data)
        st.plotly_chart(fig_high_low, use_container_width=True)
        
        # Show a snapshot of the raw data
        st.markdown("### Data Snapshot")
        st.dataframe(data.head())
