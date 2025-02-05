# Stock Buddy 🤖📈

A fun and educational stock analysis tool designed to help kids learn about the stock market! Stock Buddy makes it easy to explore companies, understand stock prices, and learn about investing in a safe, kid-friendly environment.

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
[![Code Style](https://img.shields.io/badge/code%20style-black-black)](https://github.com/psf/black)

## Features 🌟

- 📊 Real-time stock data visualization
- 🎯 Kid-friendly explanations of companies and stocks
- 💰 Investment simulator for practice
- 📈 Interactive charts and graphs
- 🎮 Fun facts about companies
- 🌈 Colorful, easy-to-understand interface

## Quick Start 🚀

1. **Clone the repository**
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

3. **Run Stock Buddy**
   ```bash
   cd src/stock_buddy
   streamlit run app.py
   ```

4. **Open your browser**
   - Stock Buddy will automatically open in your default web browser
   - If it doesn't, visit: http://localhost:8501

## How to Use Stock Buddy 🎮

1. **Enter a Stock Symbol**
   - Type in a stock symbol (like AAPL for Apple)
   - Don't know any symbols? Try these:
     - AAPL (Apple)
     - MSFT (Microsoft)
     - GOOGL (Google)
     - DIS (Disney)

2. **Explore the Company**
   - Learn what the company does
   - See important facts and numbers
   - Watch how the stock price changes

3. **Try the Investment Simulator**
   - Practice investing with pretend money
   - Learn about profits and losses
   - Get friendly tips about investing

## For Parents and Teachers 👨‍👩‍👧‍👦

Stock Buddy is designed to be:
- 🔒 Safe and educational
- 📚 Easy to understand
- 🎯 Focused on learning
- 💡 Encouraging responsible habits
- 🌟 Fun and engaging

## Contributing 🤝

We love help from the community! Want to make Stock Buddy better?

1. Read our [Contributing Guidelines](CONTRIBUTING.md)
2. Check out our [Code of Conduct](CODE_OF_CONDUCT.md)
3. Fork the repository
4. Make your changes
5. Submit a pull request

## Development Setup 🛠️

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

## Project Structure 📁

```
stock-buddy/
├── src/
│   └── stock_buddy/
│       ├── app.py           # Main Streamlit web application
│       └── stock_analyzer.py # Core analysis functionality
├── tests/                   # Test files
├── sample_data/            # Example data files
├── requirements.txt        # Project dependencies
├── LICENSE                 # MIT License
├── README.md              # This file
├── CONTRIBUTING.md        # Contribution guidelines
└── CODE_OF_CONDUCT.md     # Community guidelines
```

## License 📜

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments 🙏

- Built with [Streamlit](https://streamlit.io/)
- Stock data from [Yahoo Finance](https://finance.yahoo.com/)
- Charts powered by [Plotly](https://plotly.com/)

## Safety Note 🔒

Stock Buddy is for educational purposes only. Always consult with parents/guardians and financial advisors before making real investments.

---

Made with ❤️ for young learners everywhere!
