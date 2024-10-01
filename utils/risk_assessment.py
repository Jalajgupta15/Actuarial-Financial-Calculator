import streamlit as st
import numpy as np

def calculate_var(data, confidence_level=0.95):
    sorted_data = np.sort(data)
    var_index = int((1 - confidence_level) * len(sorted_data))
    return sorted_data[var_index]

def show(df):
    st.subheader("Risk Assessment")
    if 'returns' in df.columns:
        risk = calculate_var(df['returns'])
        st.metric(label="Value-at-Risk", value=f"{risk:.2f}")
    else:
        st.warning("Please make sure your data contains a 'returns' column.")
