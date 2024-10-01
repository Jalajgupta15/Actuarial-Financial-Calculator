import streamlit as st
import pandas as pd
from utils import risk_assessment, financial_modeling, business_valuation, market_trends

st.set_page_config(page_title="Actuarial Financial Calculator", layout="wide")
st.title("Actuarial Financial Calculator")

uploaded_file = st.file_uploader("Upload your financial data (CSV or Excel)", type=['csv', 'xlsx'])

if uploaded_file is not None:
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    elif uploaded_file.name.endswith('.xlsx'):
        df = pd.read_excel(uploaded_file)
    
    st.subheader("Uploaded Data")
    st.dataframe(df.head())
    
    # Tabs for different features
    tabs = st.tabs(["Risk Assessment", "Financial Modeling", "Investment Scope", "Business Valuation", "Market Trends"])

    with tabs[0]:
        risk_assessment.show(df)
    with tabs[1]:
        financial_modeling.show(df)
    with tabs[2]:
        st.write("Investment Scope coming soon!")
    with tabs[3]:
        business_valuation.show(df)
    with tabs[4]:
        market_trends.show()

else:
    st.info("Please upload a CSV or Excel file to continue.")
