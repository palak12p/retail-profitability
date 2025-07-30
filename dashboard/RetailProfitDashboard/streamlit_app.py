import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load and process data
df = pd.read_csv("final_dashboard_data.csv")
df['Date'] = pd.to_datetime(df['Date'])
df['Profit'] = df['Revenue'] - df['Cost']

# Title
st.title("🛍️ Retail Profitability Dashboard (Tier-2 Cities)")

# KPIs
st.header("📊 Key Metrics")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Revenue", f"₹{int(df['Revenue'].sum()):,}")
col2.metric("Total Profit", f"₹{int(df['Profit'].sum()):,}")
col3.metric("Units Sold", f"{int(df['Quantity'].sum()):,}")
col4.metric("No. of Stores", df['Store'].nunique())

# Sidebar filters
st.sidebar.header("📍 Filters")
selected_city = st.sidebar.multiselect("Select Cities", df['City'].unique(), default=df['City'].unique())
selected_category = st.sidebar.multiselect("Select Categories", df['Category'].unique(), default=df['Category'].unique())

filtered_df = df[(df['City'].isin(selected_city)) & (df['Category'].isin(selected_category))]

# Store-wise Profit
st.subheader("🏪 Store-wise Profit")
store_profit = filtered_df.groupby('Store')['Profit'].sum().sort_values()
st.bar_chart(store_profit)

# Category-wise Revenue
st.subheader("📦 Category-wise Revenue")
category_revenue = filtered_df.groupby('Category')['Revenue'].sum()
st.bar_chart(category_revenue)

# Revenue Trend
st.subheader("📈 Daily Revenue Trend")
revenue_trend = filtered_df.groupby('Date')['Revenue'].sum()
st.line_chart(revenue_trend)

# Deadstock Table
st.subheader("🛑 Deadstock: Least Sold Products")
deadstock = filtered_df.groupby('Product')['Quantity'].sum().sort_values().head(10)
st.dataframe(deadstock.reset_index())
