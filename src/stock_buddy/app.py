"""
Stock Market Analysis Platform
A comprehensive tool for technical analysis and investment simulation.
"""

import streamlit as st
from stock_analyzer import StockBuddy
import plotly.graph_objects as go

def main():
    st.set_page_config(
        page_title="Stock Market Analysis Platform",
        page_icon="📊",
        layout="wide"
    )
    
    # Header
    st.title("Stock Market Analysis Platform")
    st.markdown("""
    Comprehensive technical analysis and investment simulation platform.
    Enter a stock symbol to begin analysis.
    """)
    
    # Create a Stock Buddy instance
    buddy = StockBuddy()
    
    # Input section
    col1, col2 = st.columns([2, 1])
    with col1:
        symbol = st.text_input(
            "Stock Symbol",
            value="AAPL",
            help="Enter stock ticker symbol (e.g., AAPL, MSFT, GOOGL)"
        ).upper()
    
    with col2:
        days = st.slider(
            "Analysis Period (Days)",
            min_value=7,
            max_value=365,
            value=30,
            step=1,
            help="Select the number of days for historical analysis"
        )
    
    if symbol:
        try:
            # Get basic company info
            with st.spinner("Retrieving company data..."):
                company_info = buddy.learn_about_stock(symbol)
            
            # Display company information
            st.header(f"Analysis: {company_info['company_name']}")
            
            # Company description in an expandable section
            with st.expander("Company Overview"):
                st.write(company_info['what_they_do'])
            
            # Company metrics
            st.subheader("Company Metrics")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Market Price", f"${company_info['current_price']:.2f}")
            with col2:
                st.metric("Jurisdiction", company_info['country'])
            with col3:
                st.metric("Workforce", f"{company_info['number_of_employees']:,}")
            
            # Get stock history and create chart
            with st.spinner("Generating technical analysis..."):
                buddy.get_stock_history(days)
                fig = buddy.create_technical_chart()
                st.plotly_chart(fig, use_container_width=True)
            
            # Calculate and display technical metrics
            metrics = buddy.calculate_metrics()
            st.subheader("Technical Indicators")
            
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Current Price", f"${metrics['current_price']:.2f}")
                st.metric("20-day SMA", f"${metrics['sma_20']:.2f}")
            with col2:
                st.metric("RSI (14)", f"{metrics['rsi']:.2f}")
                st.metric("50-day SMA", f"${metrics['sma_50']:.2f}")
            with col3:
                st.metric("MACD", f"{metrics['macd']:.2f}")
                st.metric("Signal Line", f"{metrics['macd_signal']:.2f}")
            with col4:
                st.metric("Volatility", f"{metrics['volatility']:.2f}%")
                st.metric(
                    "Volume",
                    f"{metrics['volume']:,}",
                    delta=f"{((metrics['volume']/metrics['avg_volume'])-1)*100:.1f}% vs Avg"
                )
            
            # Investment simulation
            st.subheader("Investment Performance Simulation")
            investment = st.number_input(
                "Initial Investment Amount ($)",
                min_value=100.0,
                max_value=1000000.0,
                value=10000.0,
                step=100.0,
                help="Enter the amount to simulate investment performance"
            )
            
            if investment > 0:
                simulation = buddy.simulate_investment(investment)
                
                # Display simulation results
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Initial Investment", f"${simulation['initial_investment']:.2f}")
                    st.metric("Shares Acquired", f"{simulation['shares']:.4f}")
                with col2:
                    st.metric(
                        "Final Value",
                        f"${simulation['final_value']:.2f}",
                        delta=f"${simulation['absolute_return']:.2f}"
                    )
                    st.metric("ROI", f"{simulation['roi_percent']:.2f}%")
                with col3:
                    st.metric("Annualized Return", f"{simulation['annualized_return']:.2f}%")
                    st.metric("Sharpe Ratio", f"{simulation['sharpe_ratio']:.2f}")
            
        except Exception as e:
            st.error(f"Error: {str(e)}")
            st.info(
                "Please verify the stock symbol and try again. "
                "Valid examples: AAPL, MSFT, GOOGL"
            )
    
    # Footer with market insights
    st.markdown("---")
    with st.expander("Technical Analysis Guide"):
        st.markdown("""
        ### Key Technical Indicators
        
        * **Moving Averages (SMA)**: Trend indicators showing average price over 20 and 50 days
        * **RSI (Relative Strength Index)**: Momentum indicator measuring speed and magnitude of price movements
        * **MACD (Moving Average Convergence Divergence)**: Trend-following momentum indicator
        * **Volatility**: Standard deviation of returns, annualized
        * **Volume Analysis**: Trading volume compared to average
        
        ### Performance Metrics
        
        * **ROI (Return on Investment)**: Percentage return on initial investment
        * **Annualized Return**: Return normalized to a one-year period
        * **Sharpe Ratio**: Risk-adjusted return metric (higher is better)
        * **Volatility**: Measure of price variation and risk
        """)

if __name__ == "__main__":
    main()
