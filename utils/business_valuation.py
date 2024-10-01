import streamlit as st
import numpy as np

def discounted_cash_flow(cash_flows, discount_rate):
    return np.sum([cf / (1 + discount_rate)**i for i, cf in enumerate(cash_flows)])

def show(df):
    st.subheader("Business Valuation")
    if 'CashFlows' in df.columns:
        dcf_value = discounted_cash_flow(df['CashFlows'], discount_rate=0.1)
        st.metric(label="Business Valuation (DCF)", value=f"${dcf_value:.2f}")
    else:
        st.warning("Please make sure your data contains 'CashFlows' column.")
