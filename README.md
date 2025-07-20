# SQL-PROJECT
# 🛍️ Retail Sales Insights Dashboard (SQLite + Streamlit)

Welcome to the **Retail Sales Insights Dashboard** – an interactive data analytics project that combines the power of SQL with modern data visualization using **Streamlit**. This project showcases your ability to extract insights from sales data and present them through a dynamic dashboard.

---

## 📌 Project Overview

**🎯 Goal**:  
To explore and analyze Superstore sales data using SQL and present key business insights through a visually interactive dashboard.

**👨‍💻 Tools & Technologies**:
- **SQLite** – for database storage and querying
- **SQL** – to extract and analyze business metrics
- **Python (Pandas, SQLAlchemy)** – for data handling and backend logic
- **Streamlit** – to build an interactive and shareable dashboard
- **GitHub** – for version control and showcasing your project

---

## 🧾 Data Description

The dataset used is derived from the popular **"Superstore"** retail dataset, originally in CSV format and converted to SQLite for structured querying.

**Database Table: `sales`**  
Contains columns such as:
- `Order ID`, `Order Date`, `Ship Mode`
- `Customer ID`, `Customer Name`
- `Segment`, `State`, `Region`
- `Product Name`, `Category`, `Sub-Category`
- `Sales`, `Profit`, `Discount`, etc.

---

## ✅ Key Features & SQL Insights

### 🔍 Step 1: Data Validation
```sql
SELECT * FROM sales LIMIT 5;

