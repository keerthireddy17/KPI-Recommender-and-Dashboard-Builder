# app.py

import streamlit as st
import pandas as pd
import openpyxl


st.title("Smart KPI Recommender")

# --- File Uploader ---
uploaded_file = st.file_uploader("Upload a CSV or Excel file", type=['csv', 'xlsx'])

if uploaded_file is not None:
    # --- Try reading file ---
    try:
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        else:
            # For Excel: read first sheet by default
            df = pd.read_excel(uploaded_file)
        
        st.success("File successfully loaded!")
        st.write("### Data Preview", df.head())

    except Exception as e:
        st.error(f" Oops! Cannot read file: {e}")

else:
    st.info("👆 Please upload a file to get started.")

