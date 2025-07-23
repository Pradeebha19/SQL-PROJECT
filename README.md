# Sales Analytics Dashboard for a Retail Store (SQLite + Streamlit)

Welcome to the **Sales Analytics Dashboard for a Retail Store** – an interactive data analytics project that combines the power of SQL with modern data visualization using **Streamlit**. This project showcases your ability to extract insights from sales data and present them through a dynamic dashboard.

---

## Project Overview

**🎯 Goal**:  
To explore and analyze Superstore sales data using SQL and present key business insights through a visually interactive dashboard.

**👨‍💻 Tools & Technologies**:
- **SQLite** – for database storage and querying
- **SQL** – to extract and analyze business metrics
- **Python (Pandas, SQLAlchemy)** – for data handling and backend logic
- **Streamlit** – to build an interactive and shareable dashboard
- **GitHub** – for version control and showcasing your project

---

##  Data Description

The dataset used is derived from the popular **"Superstore"** retail dataset, originally in CSV format and converted to SQLite for structured querying.

**Database Table: `sales`**  
Contains columns such as:
- `Order ID`, `Order Date`, `Ship Mode`
- `Customer ID`, `Customer Name`
- `Segment`, `State`, `Region`
- `Product Name`, `Category`, `Sub-Category`
- `Sales`, `Profit`, `Discount`, etc.

---

##  Key Features & SQL Insights
### step 1:Data validation

SELECT * FROM sales LIMIT 5;

### Step 2: Missing Data Check

SELECT * FROM sales WHERE Sales IS NULL OR State IS NULL;

### Step 3: Metric-Based Analysis

Query	Description
SELECT SUM(Sales), SUM(Profit)	Total performance overview
GROUP BY State	Top 10 states by sales
GROUP BY Sub-Category	Top 5 most profitable sub-categories
WHERE Discount > 0.3 AND Profit < 0	High discount, low profit warning
GROUP BY Region	Sales by region
GROUP BY Category, Sub-Category	Performance by category & sub-category

### 📈 Dashboard Features (Built in Streamlit)
🔹 View entire dataset (scrollable table)

🔹 Visualizations of total sales by region

🔹 Highlight most/least profitable sub-categories

🔹 Flag products with discounts that hurt profits

🔹 Fast filtering, sorting, and interactive charts

### Deploy
pip install streamlit 
streamlit run app.py

Local URL: http://localhost:8501
Network URL: http://192.168.1.170:8501

# OUTPUT

<img width="1232" height="836" alt="image" src="https://github.com/user-attachments/assets/85bbd02d-668f-45f4-a961-9903453b25e3" />
<img width="1067" height="437" alt="image" src="https://github.com/user-attachments/assets/b0f596e7-1019-49b0-8dec-ad915443123c" />
<img width="1032" height="621" alt="image" src="https://github.com/user-attachments/assets/dc7856ef-f6d2-4058-9c59-888c9068115a" />
<img width="1017" height="530" alt="image" src="https://github.com/user-attachments/assets/79033186-04f9-4bce-8293-97f64398e9e0" />
<img width="1090" height="722" alt="image" src="https://github.com/user-attachments/assets/cd8ee966-2aa7-4012-92fe-c42e0dfdbe8a" />



