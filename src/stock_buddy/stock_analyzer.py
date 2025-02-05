"""
Stock Analysis Tool
A comprehensive stock market analysis tool providing technical indicators and financial metrics.
"""

import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime, timedelta

class StockBuddy:
    """Stock analysis tool providing technical indicators and market metrics"""
    
    def __init__(self):
        """Get ready to explore stocks!"""
        self.stock_data = None
        self.symbol = None
    
    def learn_about_stock(self, symbol: str) -> dict:
        """
        Learn about a stock by its symbol (like 'AAPL' for Apple)!
        
        Args:
            symbol: The stock symbol (e.g., 'AAPL', 'MSFT', 'GOOGL')
            
        Returns:
            A dictionary with fun facts about the stock
        """
        self.symbol = symbol.upper()
        stock = yf.Ticker(self.symbol)
        
        # Get basic info about the company
        info = stock.info
        
        return {
            "company_name": info.get("longName", "Unknown"),
            "what_they_do": info.get("longBusinessSummary", "No information available"),
            "current_price": info.get("currentPrice", 0),
            "currency": info.get("currency", "USD"),
            "country": info.get("country", "Unknown"),
            "number_of_employees": info.get("fullTimeEmployees", 0)
        }
    
    def get_stock_history(self, days: int = 30) -> None:
        """
        Get the stock's price history for the last few days.
        
        Args:
            days: Number of days to look back (default is 30 days)
        """
        if not self.symbol:
            raise ValueError("Please use learn_about_stock() first!")
            
        end_date = datetime.now()
        start_date = end_date - timedelta(days=days)
        
        self.stock_data = yf.download(
            self.symbol,
            start=start_date,
            end=end_date,
            progress=False
        )
    
    def calculate_metrics(self) -> dict:
        """Calculate key technical indicators and market metrics"""
        if self.stock_data is None or self.stock_data.empty:
            raise ValueError("No stock data available! Use get_stock_history() first!")
        
        if self.stock_data is None or self.stock_data.empty:
            raise ValueError("No stock data available! Use get_stock_history() first!")

        # Calculate basic price metrics
        current_price = self.stock_data['Close'].iloc[-1]
        start_price = self.stock_data['Close'].iloc[0]
        price_change = ((current_price - start_price) / start_price) * 100
        
        # Calculate Moving Averages
        self.stock_data['SMA_20'] = self.stock_data['Close'].rolling(window=20).mean()
        self.stock_data['SMA_50'] = self.stock_data['Close'].rolling(window=50).mean()
        
        # Calculate RSI (Relative Strength Index)
        delta = self.stock_data['Close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
        rs = gain / loss
        rsi = 100 - (100 / (1 + rs))
        
        # Calculate Volatility (20-day standard deviation)
        volatility = self.stock_data['Close'].rolling(window=20).std()
        
        # Calculate MACD
        exp1 = self.stock_data['Close'].ewm(span=12, adjust=False).mean()
        exp2 = self.stock_data['Close'].ewm(span=26, adjust=False).mean()
        macd = exp1 - exp2
        signal = macd.ewm(span=9, adjust=False).mean()
        
        return {
            "current_price": round(current_price, 2),
            "price_change_percent": round(price_change, 2),
            "sma_20": round(self.stock_data['SMA_20'].iloc[-1], 2),
            "sma_50": round(self.stock_data['SMA_50'].iloc[-1], 2),
            "rsi": round(rsi.iloc[-1], 2),
            "volatility": round(volatility.iloc[-1], 2),
            "macd": round(macd.iloc[-1], 2),
            "macd_signal": round(signal.iloc[-1], 2),
            "volume": int(self.stock_data['Volume'].iloc[-1]),
            "avg_volume": int(self.stock_data['Volume'].mean()),
            "total_days": len(self.stock_data)
        }
    
    def create_technical_chart(self) -> go.Figure:
        """Create a technical analysis chart with multiple indicators"""
        if self.stock_data is None or self.stock_data.empty:
            raise ValueError("No stock data available! Use get_stock_history() first!")
        
        fig = go.Figure()
        
        # Calculate indicators if not already calculated
        if 'SMA_20' not in self.stock_data.columns:
            self.calculate_metrics()

        # Create subplots for price and volume
        fig = go.Figure()

        # Add candlestick chart
        fig.add_trace(go.Candlestick(
            x=self.stock_data.index,
            open=self.stock_data['Open'],
            high=self.stock_data['High'],
            low=self.stock_data['Low'],
            close=self.stock_data['Close'],
            name='OHLC'
        ))

        # Add Moving Averages
        fig.add_trace(go.Scatter(
            x=self.stock_data.index,
            y=self.stock_data['SMA_20'],
            name='20-day SMA',
            line=dict(color='blue', width=1)
        ))

        fig.add_trace(go.Scatter(
            x=self.stock_data.index,
            y=self.stock_data['SMA_50'],
            name='50-day SMA',
            line=dict(color='orange', width=1)
        ))

        # Update layout
        fig.update_layout(
            title=f"{self.symbol} Technical Analysis",
            xaxis_title="Date",
            yaxis_title="Price",
            template="plotly_white",
            showlegend=True,
            hovermode='x unified',
            xaxis_rangeslider_visible=False
        )
        
        return fig
    
    def simulate_investment(self, amount: float) -> dict:
        """
        Simulate an investment with detailed performance metrics
        
        Args:
            amount: Initial investment amount
            
        Returns:
            Dictionary containing investment performance metrics
        """
        if self.stock_data is None or self.stock_data.empty:
            raise ValueError("No stock data available! Use get_stock_history() first!")
        
        start_price = self.stock_data['Close'].iloc[0]
        end_price = self.stock_data['Close'].iloc[-1]
        
        shares = amount / start_price
        end_value = shares * end_price
        profit_loss = end_value - amount
        
        # Calculate returns and metrics
        roi = (profit_loss / amount) * 100
        daily_returns = self.stock_data['Close'].pct_change()
        annualized_return = ((1 + (profit_loss / amount)) ** (365 / len(self.stock_data)) - 1) * 100
        volatility = daily_returns.std() * (252 ** 0.5) * 100  # Annualized volatility
        sharpe_ratio = (annualized_return - 2) / volatility  # Assuming 2% risk-free rate
        
        return {
            "shares": round(shares, 4),
            "initial_investment": round(amount, 2),
            "final_value": round(end_value, 2),
            "absolute_return": round(profit_loss, 2),
            "roi_percent": round(roi, 2),
            "annualized_return": round(annualized_return, 2),
            "volatility": round(volatility, 2),
            "sharpe_ratio": round(sharpe_ratio, 2),
            "holding_period_days": len(self.stock_data)
        }
