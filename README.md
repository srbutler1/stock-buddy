# Stock Market Analysis Platform

Arkansas 

A comprehensive technical analysis tool providing advanced market metrics, performance indicators, and investment simulation capabilities.

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
[![Code Style](https://img.shields.io/badge/code%20style-black-black)](https://github.com/psf/black)

## Features

- Advanced Technical Analysis
  - Moving Averages (20-day and 50-day SMA)
  - RSI (Relative Strength Index)
  - MACD (Moving Average Convergence Divergence)
  - Volume Analysis with Average Comparison
  - Volatility Metrics
- Professional-Grade Charts
  - Candlestick Patterns
  - Technical Indicators Overlay
  - Interactive Price Analysis
- Investment Performance Metrics
  - ROI and Annualized Returns
  - Sharpe Ratio Analysis
  - Risk-Adjusted Performance Metrics
- Comprehensive Market Data
  - Real-Time Stock Information
  - Company Fundamentals
  - Historical Price Analysis

## Quick Start

1. **Fork the repository**

   Go to the repository on GitHub and click the "Fork" button at the top right to create a copy of the repository under your own GitHub account.

2. **Clone your forked repository**
   ```bash
   git clone https://github.com/yourusername/stock-buddy.git
   cd stock-buddy
   ```

2. **Set up your environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Launch the application**
   ```bash
   cd src/stock_buddy
   streamlit run app.py
   ```

4. **Access the platform**
   - Application will be available at: http://localhost:8501

## Technical Analysis Tools

### Price Analysis
- Candlestick charts for price action analysis
- Multiple timeframe analysis (7-365 days)
- Moving averages for trend identification
- Volume analysis for trade activity

### Technical Indicators
- **RSI (Relative Strength Index)**
  - Momentum indicator (0-100 scale)
  - Overbought/Oversold identification
  - Divergence analysis capabilities

- **MACD (Moving Average Convergence Divergence)**
  - Trend-following momentum indicator
  - Signal line crossovers
  - Histogram analysis

- **Moving Averages**
  - 20-day SMA for short-term trends
  - 50-day SMA for medium-term trends
  - Crossover analysis

### Performance Metrics
- ROI (Return on Investment)
- Annualized Returns
- Volatility Analysis
- Sharpe Ratio Calculations

## Project Structure

```
stock-buddy/
├── src/
│   └── stock_buddy/
│       ├── app.py           # Streamlit web application
│       └── stock_analyzer.py # Technical analysis engine
├── tests/                   # Test suite
├── sample_data/            # Sample datasets
├── requirements.txt        # Dependencies
├── LICENSE                 # MIT License
├── README.md              # Documentation
├── CONTRIBUTING.md        # Contribution guidelines

```

## Development

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run tests**
   ```bash
   pytest tests/
   ```

3. **Code formatting**
   ```bash
   black .
   flake8
   ```

## Contributing

1. Review the [Contributing Guidelines](CONTRIBUTING.md)
2. Fork the repository
3. Create a feature branch
4. Implement your changes
5. Submit a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Technology Stack

- Built with [Streamlit](https://streamlit.io/)
- Market data from [Yahoo Finance](https://finance.yahoo.com/)
- Visualization powered by [Plotly](https://plotly.com/)

## Disclaimer

This platform is for educational and research purposes only. The technical analysis and investment simulations provided should not be considered as financial advice. Always conduct thorough research and consult with financial professionals before making investment decisions.

---

Developed for technical analysis and market research
