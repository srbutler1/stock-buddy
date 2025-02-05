
"""
Tests for the Stock Buddy analyzer module
"""

import pytest
from datetime import datetime, timedelta
import pandas as pd
from src.stock_buddy.stock_analyzer import StockBuddy

def test_stock_buddy_initialization():
    """Test that StockBuddy initializes with correct default values"""
    buddy = StockBuddy()
    assert buddy.stock_data is None
    assert buddy.symbol is None

def test_learn_about_stock_symbol_conversion():
    """Test that stock symbols are converted to uppercase"""
    buddy = StockBuddy()
    info = buddy.learn_about_stock('aapl')
    assert buddy.symbol == 'AAPL'

def test_get_stock_history_without_symbol():
    """Test that getting history without a symbol raises an error"""
    buddy = StockBuddy()
    with pytest.raises(ValueError) as exc_info:
        buddy.get_stock_history()
    assert "Please use learn_about_stock() first!" in str(exc_info.value)

def test_calculate_fun_facts_without_data():
    """Test that calculating facts without data raises an error"""
    buddy = StockBuddy()
    with pytest.raises(ValueError) as exc_info:
        buddy.calculate_fun_facts()
    assert "No stock data available!" in str(exc_info.value)

def test_create_fun_chart_without_data():
    """Test that creating chart without data raises an error"""
    buddy = StockBuddy()
    with pytest.raises(ValueError) as exc_info:
        buddy.create_fun_chart()
    assert "No stock data available!" in str(exc_info.value)

def test_get_investment_lesson_without_data():
    """Test that getting investment lesson without data raises an error"""
    buddy = StockBuddy()
    with pytest.raises(ValueError) as exc_info:
        buddy.get_investment_lesson(100)
    assert "No stock data available!" in str(exc_info.value)

def test_get_lesson_message_positive():
    """Test that positive profit generates encouraging message"""
    buddy = StockBuddy()
    message = buddy._get_lesson_message(100)
    assert "Great job!" in message
    assert "made money" in message

def test_get_lesson_message_negative():
    """Test that negative profit generates supportive message"""
    buddy = StockBuddy()
    message = buddy._get_lesson_message(-50)
    assert "Don't worry!" in message
    assert "sometimes stocks go down" in message.lower()

# Integration tests with mock data
@pytest.fixture
def mock_stock_data():
    """Create mock stock data for testing"""
    dates = pd.date_range(start='2024-01-01', end='2024-01-10', freq='D')
    data = {
        'Open': [100] * len(dates),
        'High': [110] * len(dates),
        'Low': [90] * len(dates),
        'Close': [105] * len(dates),
        'Volume': [1000000] * len(dates)
    }
    return pd.DataFrame(data, index=dates)

def test_calculate_fun_facts_with_mock_data(mock_stock_data):
    """Test fun facts calculation with mock data"""
    buddy = StockBuddy()
    buddy.symbol = 'TEST'
    buddy.stock_data = mock_stock_data
    
    facts = buddy.calculate_fun_facts()
    
    assert facts['highest_price'] == 110
    assert facts['lowest_price'] == 90
    assert facts['current_price'] == 105
    assert facts['total_days_analyzed'] == len(mock_stock_data)

def test_get_investment_lesson_with_mock_data(mock_stock_data):
    """Test investment lesson calculation with mock data"""
    buddy = StockBuddy()
    buddy.symbol = 'TEST'
    buddy.stock_data = mock_stock_data
    
    investment_amount = 1000
    lesson = buddy.get_investment_lesson(investment_amount)
    
    assert lesson['starting_investment'] == investment_amount
    assert lesson['shares_you_could_buy'] == investment_amount / mock_stock_data['Close'][0]
    assert 'lesson' in lesson
    assert isinstance(lesson['was_it_good'], bool)
