import streamlit as st
import plotly.express as px

def show(df):
    st.subheader("Financial Modeling & Analysis")
    if 'Date' in df.columns and 'Profit' in df.columns:
        fig = px.line(df, x='Date', y='Profit', title="Profit Trend Over Time")
        st.plotly_chart(fig)
    else:
        st.warning("Please make sure your data contains 'Date' and 'Profit' columns.")
