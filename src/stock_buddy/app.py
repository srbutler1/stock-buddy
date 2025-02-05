"""
Stock Buddy Web App - Learn about stocks in a fun way! 🎮
"""

import streamlit as st
from stock_analyzer import StockBuddy
import plotly.graph_objects as go

def main():
    st.set_page_config(
        page_title="Stock Buddy - Learn About Stocks! 📈",
        page_icon="🤖",
        layout="wide"
    )
    
    # Header
    st.title("Stock Buddy - Your Stock Market Friend! 🤖")
    st.markdown("""
    Welcome to Stock Buddy! Let's learn about stocks together! 
    Type in a stock symbol (like AAPL for Apple) and let's explore! 🚀
    """)
    
    # Create a Stock Buddy instance
    buddy = StockBuddy()
    
    # Input section
    col1, col2 = st.columns([2, 1])
    with col1:
        symbol = st.text_input(
            "Enter a stock symbol (Example: AAPL, MSFT, GOOGL)",
            value="AAPL"
        ).upper()
    
    with col2:
        days = st.slider(
            "How many days should we look at?",
            min_value=7,
            max_value=365,
            value=30,
            step=1
        )
    
    if symbol:
        try:
            # Get basic company info
            with st.spinner("Learning about the company... 🔍"):
                company_info = buddy.learn_about_stock(symbol)
            
            # Display company information
            st.header(f"Let's Learn About {company_info['company_name']}! 🏢")
            
            # Company description in an expandable section
            with st.expander("What does this company do? 🤔"):
                st.write(company_info['what_they_do'])
            
            # Quick facts
            st.subheader("Quick Facts! 📝")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Current Price", f"${company_info['current_price']:.2f}")
            with col2:
                st.metric("Country", company_info['country'])
            with col3:
                st.metric("Number of Employees", f"{company_info['number_of_employees']:,}")
            
            # Get stock history and create chart
            with st.spinner("Creating your chart... 📊"):
                buddy.get_stock_history(days)
                fig = buddy.create_fun_chart()
                st.plotly_chart(fig, use_container_width=True)
            
            # Calculate and display fun facts
            facts = buddy.calculate_fun_facts()
            st.subheader("Fun Facts About the Stock! 🎯")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Highest Price", f"${facts['highest_price']}")
            with col2:
                st.metric("Lowest Price", f"${facts['lowest_price']}")
            with col3:
                st.metric(
                    "Price Change",
                    f"{facts['price_change_percent']}%",
                    delta=f"{facts['price_change_percent']}%"
                )
            
            # Investment simulator
            st.subheader("Let's Pretend to Invest! 💰")
            investment = st.number_input(
                "How much money would you like to pretend to invest?",
                min_value=10.0,
                max_value=10000.0,
                value=100.0,
                step=10.0
            )
            
            if investment > 0:
                lesson = buddy.get_investment_lesson(investment)
                
                # Display investment results
                col1, col2 = st.columns(2)
                with col1:
                    st.metric(
                        "Starting Investment",
                        f"${lesson['starting_investment']:.2f}"
                    )
                    st.metric(
                        "Shares You Could Buy",
                        f"{lesson['shares_you_could_buy']:.2f}"
                    )
                
                with col2:
                    st.metric(
                        "Ending Value",
                        f"${lesson['ending_value']:.2f}",
                        delta=f"${lesson['profit_or_loss']:.2f}"
                    )
                
                # Display the lesson message
                st.info(lesson['lesson'])
            
        except Exception as e:
            st.error(f"Oops! Something went wrong: {str(e)} 😕")
            st.info(
                "Try another stock symbol or check if you typed it correctly! "
                "Remember, stock symbols are like AAPL, MSFT, or GOOGL."
            )
    
    # Footer with educational tips
    st.markdown("---")
    with st.expander("Stock Market Tips for Kids! 💡"):
        st.markdown("""
        * 📈 Stocks are tiny pieces of a company that you can own
        * 💰 When the company does well, your stock usually goes up in value
        * 🎯 It's important to learn before investing real money
        * 📚 Always ask a grown-up for help with real investments
        * 🌟 Investing is about being patient and thinking long-term
        * 🎮 Keep learning and have fun exploring different companies!
        """)

if __name__ == "__main__":
    main()
