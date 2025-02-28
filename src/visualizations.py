import plotly.graph_objects as go
import plotly.express as px

def create_candlestick_chart(data, ticker):
    """
    Builds an interactive candlestick chart.
    """
    fig = go.Figure(data=[go.Candlestick(
        x=data['Date'],
        open=data['Open'],
        high=data['High'],
        low=data['Low'],
        close=data['Close'],
        name=ticker
    )])
    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Price (USD)",
        title=f"{ticker} Candlestick Chart"
    )
    return fig

def create_moving_average_chart(data, ticker, ma_window):
    """
    Creates a line chart showing the closing price and its moving average.
    """
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'],
                             mode='lines', name="Close"))
    fig.add_trace(go.Scatter(x=data['Date'], y=data['MA'],
                             mode='lines', name=f"{ma_window}-Day MA"))
    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Price (USD)",
        title=f"{ticker} Closing Price with {ma_window}-Day Moving Average"
    )
    return fig

def create_daily_returns_histogram(data):
    """
    Generates a histogram for the daily returns.
    """
    fig = px.histogram(data, x="Daily Return", nbins=50,
                       title="Daily Returns Distribution")
    return fig

def create_volume_vs_close_scatter(data):
    """
    Creates a scatter plot of trading volume versus closing price.
    """
    fig = px.scatter(data, x="Volume", y="Close",
                     title="Volume vs. Closing Price",
                     hover_data=['Date'])
    return fig

def create_high_low_chart(data):
    """
    Produces a line chart displaying high and low prices over time.
    """
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['Date'], y=data['High'],
                             mode='lines', name="High"))
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Low'],
                             mode='lines', name="Low"))
    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Price (USD)",
        title="High and Low Prices Over Time"
    )
    return fig
