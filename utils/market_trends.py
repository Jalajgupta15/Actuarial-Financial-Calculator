import streamlit as st
import yfinance as yf
import plotly.express as px

def show():
    st.subheader("Market Trends Estimation")
    ticker = st.text_input("Enter stock ticker (e.g., AAPL, GOOG):")
    if ticker:
        data = yf.download(ticker, period='1y')
        fig = px.line(data, x=data.index, y='Close', title=f"{ticker} Market Trend")
        st.plotly_chart(fig)
