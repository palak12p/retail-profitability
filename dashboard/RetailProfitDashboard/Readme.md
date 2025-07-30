# 🛍️ Retail Profitability Dashboard (Tier-2 Cities)

## 🚀 Overview
This project analyzes retail sales data from stores in Tier-2 Indian cities to uncover profitability insights. Built using Python, Streamlit, and Pandas, it mimics a McKinsey-style business analysis dashboard.

## 📊 Features
- KPI cards: Total Revenue, Profit, Units Sold, Store Count
- Store-wise Profit bar chart
- Category-wise Revenue chart
- Daily Revenue Trend
- Deadstock detection (least-selling products)
- Interactive filters for City and Category

## 🧰 Tech Stack
- Python
- Pandas
- Streamlit
- Matplotlib / Seaborn

## 📁 Dataset
- `final_dashboard_data.csv` (sample dataset with revenue, cost, and quantity)

## ✅ How to Run
```bash
pip install streamlit pandas matplotlib seaborn
streamlit run streamlit_app.py
📈 Business Insights
Personal Care is the highest revenue category.

Store_18 is the lowest-performing store.

Deadstock products can be optimized or removed.