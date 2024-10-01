import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import yfinance as yf
from io import StringIO

# Function to calculate Value at Risk
def calculate_var(data, confidence_level=0.95):
    sorted_data = np.sort(data)
    var_index = int((1 - confidence_level) * len(sorted_data))
    return sorted_data[var_index]

# Function to calculate discounted cash flow
def discounted_cash_flow(cash_flows, discount_rate):
    return np.sum([cf / (1 + discount_rate)**i for i, cf in enumerate(cash_flows)])

# Streamlit app layout
st.set_page_config(page_title="Actuarial Financial Calculator", layout="wide")
st.title("Actuarial Financial Calculator")

# Background image (optional, you will need an external CSS trick)
st.markdown("""
    <style>
    .stApp {
        background-image: url("https://euromed-economists.org/wp-content/uploads/2018/01/moneyfinance-1.jpg");
        background-size: cover;
    }
    </style>
    """, unsafe_allow_html=True)

# File upload
uploaded_file = st.file_uploader("Upload your financial data (CSV or Excel)", type=['csv', 'xlsx'])

if uploaded_file is not None:
    # Read file
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    elif uploaded_file.name.endswith('.xlsx'):
        df = pd.read_excel(uploaded_file)
    
    st.subheader("Uploaded Data")
    st.dataframe(df.head())
    
    # Add Tabs for different features
    tabs = st.tabs(["Risk Assessment", "Financial Modeling", "Investment Scope", "Business Valuation", "Market Trends"])

    # Feature 1: Risk Assessment
    with tabs[0]:
        st.subheader("Risk Assessment")
        # Assuming 'returns' is a column in your dataset
        if 'returns' in df.columns:
            risk = calculate_var(df['returns'])
            st.metric(label="Value-at-Risk", value=f"{risk:.2f}")
        else:
            st.warning("Please make sure your data contains a 'returns' column.")

    # Feature 2: Financial Modeling and Analysis
    with tabs[1]:
        st.subheader("Financial Modeling & Analysis")
        if 'Date' in df.columns and 'Profit' in df.columns:
            fig = px.line(df, x='Date', y='Profit', title="Profit Trend Over Time")
            st.plotly_chart(fig)
        else:
            st.warning("Please make sure your data contains 'Date' and 'Profit' columns.")

    # Feature 3: Scope of Investment
    with tabs[2]:
        st.subheader("Scope of Investment")
        if 'Revenue' in df.columns and 'Expenses' in df.columns:
            investment_scope = df['Revenue'] - df['Expenses']
            st.write(f"Scope of Investment: Areas with higher profit margins are {investment_scope.idxmax()}")
        else:
            st.warning("Please make sure your data contains 'Revenue' and 'Expenses' columns.")

    # Feature 4: Business Valuation
    with tabs[3]:
        st.subheader("Business Valuation")
        if 'CashFlows' in df.columns:
            dcf_value = discounted_cash_flow(df['CashFlows'], discount_rate=0.1)
            st.metric(label="Business Valuation (DCF)", value=f"${dcf_value:.2f}")
        else:
            st.warning("Please make sure your data contains 'CashFlows' column.")

    # Feature 5: Market Trends Estimation
    with tabs[4]:
        st.subheader("Market Trends Estimation")
        ticker = st.text_input("Enter stock ticker (e.g., AAPL, GOOG):")
        if ticker:
            data = yf.download(ticker, period='1y')
            fig = px.line(data, x=data.index, y='Close', title=f"{ticker} Market Trend")
            st.plotly_chart(fig)

else:
    st.info("Please upload a CSV or Excel file to continue.")
