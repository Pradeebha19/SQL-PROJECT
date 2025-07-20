import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

# DB connection
db_file = 'retail_sales.db'  # make sure this file is in same folder
engine = create_engine(f'sqlite:///{db_file}')

# Set title
st.title("🛍️ Retail Sales Insights Dashboard")

st.markdown("### ✅ Total Sales and Profit")
total = pd.read_sql("SELECT SUM(Sales) AS Total_Sales, SUM(Profit) AS Total_Profit FROM sales", engine)
st.dataframe(total)

st.markdown("### 🗺️ Top 10 States by Sales")
state_sales = pd.read_sql("""
SELECT State, SUM(Sales) AS Total_Sales
FROM sales
GROUP BY State
ORDER BY Total_Sales DESC
LIMIT 10
""", engine)
st.dataframe(state_sales)

st.markdown("### 💰 Top 5 Most Profitable Sub-Categories")
profitable_subcats = pd.read_sql("""
SELECT [Sub-Category], SUM(Profit) AS Total_Profit
FROM sales
GROUP BY [Sub-Category]
ORDER BY Total_Profit DESC
LIMIT 5
""", engine)
st.dataframe(profitable_subcats)

st.markdown("### ⚠️ High Discount, Low Profit Products")
discount_loss = pd.read_sql("""
SELECT [Product Name], Discount, Profit
FROM sales
WHERE Discount > 0.3 AND Profit < 0
ORDER BY Discount DESC
""", engine)
st.dataframe(discount_loss)

st.markdown("### 🌍 Sales by Region")
region_sales = pd.read_sql("""
SELECT Region, SUM(Sales) AS Total_Sales
FROM sales
GROUP BY Region
ORDER BY Total_Sales DESC
""", engine)
st.bar_chart(region_sales.set_index("Region"))

st.markdown("### 📦 Sales by Category and Sub-Category")
category_sales = pd.read_sql("""
SELECT Category, [Sub-Category], SUM(Sales) AS Total_Sales
FROM sales
GROUP BY Category, [Sub-Category]
ORDER BY Total_Sales DESC
""", engine)
st.dataframe(category_sales)
