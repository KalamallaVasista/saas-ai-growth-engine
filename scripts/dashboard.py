import streamlit as st
import duckdb
import pandas as pd
import os

# Set up the page
st.set_page_config(page_title="SaaS Growth Engine", layout="wide")
st.title("🚀 SaaS AI Growth Engine Dashboard")
st.markdown("Real-time telemetry analytics and churn prediction.")

# Load data directly from your DuckDB pipeline
@st.cache_data
def load_data():
    # Shift working directory so DuckDB finds the CSV files correctly
    if os.path.exists('telemetry_analytics'):
        os.chdir('telemetry_analytics')
        
    con = duckdb.connect(database='dev.duckdb', read_only=True)
    df = con.execute("SELECT * FROM main.user_summary").df()
    return df

df = load_data()

# Calculate Key Metrics
total_users = len(df)
churn_risk = len(df[df['user_segment'] == 'Churn Risk'])
high_value = len(df[df['user_segment'] == 'High Value'])

# Display Metrics in columns
col1, col2, col3 = st.columns(3)
col1.metric("Total Users", total_users)
col2.metric("⚠️ Churn Risk", churn_risk)
col3.metric("⭐ High Value", high_value)

st.divider()

# Create visual charts
st.subheader("User Segmentation Breakdown")
segment_counts = df['user_segment'].value_counts().reset_index()
segment_counts.columns = ['Segment', 'Users']
st.bar_chart(segment_counts.set_index('Segment'))

st.subheader("Raw Telemetry Data (Sample)")
st.dataframe(df.head(100))