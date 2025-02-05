"""
Stock Buddy - A fun way to learn about stocks! 📈
This module helps kids understand stock market basics through simple analysis.
"""

import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime, timedelta

class StockBuddy:
    """Your friendly stock market guide! 🤖"""
    
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
    
    def calculate_fun_facts(self) -> dict:
        """Calculate interesting facts about the stock! 🎯"""
        if self.stock_data is None or self.stock_data.empty:
            raise ValueError("No stock data available! Use get_stock_history() first!")
        
        highest_price = self.stock_data['High'].max()
        lowest_price = self.stock_data['Low'].min()
        current_price = self.stock_data['Close'][-1]
        
        # Calculate if the stock is going up or down (trend)
        start_price = self.stock_data['Close'][0]
        price_change = ((current_price - start_price) / start_price) * 100
        
        return {
            "highest_price": round(highest_price, 2),
            "lowest_price": round(lowest_price, 2),
            "current_price": round(current_price, 2),
            "price_change_percent": round(price_change, 2),
            "is_going_up": price_change > 0,
            "total_days_analyzed": len(self.stock_data)
        }
    
    def create_fun_chart(self) -> go.Figure:
        """Create a colorful, easy-to-understand chart! 📊"""
        if self.stock_data is None or self.stock_data.empty:
            raise ValueError("No stock data available! Use get_stock_history() first!")
        
        fig = go.Figure()
        
        # Add the main price line
        fig.add_trace(go.Scatter(
            x=self.stock_data.index,
            y=self.stock_data['Close'],
            name='Stock Price',
            line=dict(color='blue', width=3),
            mode='lines'
        ))
        
        # Make the chart kid-friendly
        fig.update_layout(
            title=f"{self.symbol} Stock Price Adventure! 🚀",
            xaxis_title="Date 📅",
            yaxis_title="Price 💰",
            template="simple_white",
            showlegend=True,
            hovermode='x unified'
        )
        
        return fig
    
    def get_investment_lesson(self, amount: float) -> dict:
        """
        Learn what would happen if you invested some money!
        
        Args:
            amount: How much money you want to pretend to invest
            
        Returns:
            A fun lesson about investing that amount
        """
        if self.stock_data is None or self.stock_data.empty:
            raise ValueError("No stock data available! Use get_stock_history() first!")
        
        start_price = self.stock_data['Close'][0]
        end_price = self.stock_data['Close'][-1]
        
        shares = amount / start_price
        end_value = shares * end_price
        profit_loss = end_value - amount
        
        return {
            "shares_you_could_buy": round(shares, 2),
            "starting_investment": round(amount, 2),
            "ending_value": round(end_value, 2),
            "profit_or_loss": round(profit_loss, 2),
            "was_it_good": profit_loss > 0,
            "lesson": self._get_lesson_message(profit_loss)
        }
    
    def _get_lesson_message(self, profit_loss: float) -> str:
        """Create a friendly message about the investment result."""
        if profit_loss > 0:
            return ("Great job! You made money! Remember, stocks can go up and down, "
                   "so it's important to invest wisely and for the long term! 🌟")
        else:
            return ("Don't worry! Sometimes stocks go down. That's why it's important "
                   "to learn and understand before investing real money! 📚")
