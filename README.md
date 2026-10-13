E-Commerce Sales & Customer Analytics

Project Overview

This project focuses on analyzing e-commerce sales and customer data to understand business performance, revenue trends, product performance, and customer behavior.

The project follows an end-to-end data analytics workflow, starting with data cleaning and exploratory data analysis in Python, storing the cleaned data in PostgreSQL, and presenting key metrics through an interactive Power BI dashboard.

The goal is to transform raw sales data into meaningful business insights that support data-driven decision-making.

Objectives

Clean and prepare raw e-commerce data for analysis.

Handle missing values, duplicate records, invalid values, and inconsistent text.

Calculate revenue and key business metrics.

Analyze monthly revenue trends.

Compare revenue across product categories and cities.

Identify the top five products by revenue.

Analyze orders by payment mode and order status.

Compare new and returning customer groups.

Build an interactive Power BI dashboard with KPI cards and slicers.

Tools and Technologies

Tool

Purpose

Python

Data preparation and analysis

Pandas

Data cleaning and manipulation

NumPy

Numerical operations

Matplotlib

Data visualization

Seaborn

Exploratory data visualization

PostgreSQL

Data storage and SQL analysis

Power BI

Interactive dashboard development

Dataset Description

The dataset contains information about e-commerce orders, customers, products, payments, discounts, and shipping.

Important columns include:

Order_ID — Order identifier

Order_Date — Order date

Customer_ID — Customer identifier

Gender and Age — Customer demographic information

City — City associated with the transaction

Category and Product — Product category and name

Quantity — Number of units ordered

Unit_Price — Price per unit

Discount — Discount applied

Payment_Mode — Payment method

Order_Status — Order status

Customer_Type — New or returning customer

Rating — Customer rating

Shipping_Days — Shipping duration

Revenue — Calculated revenue measure

After cleaning, the analysis dataset contains 7,478 rows and 17 columns, including the calculated Revenue column.

Project Workflow

1. Data Cleaning with Python

The dataset was inspected and prepared for analysis. The cleaning process included:

Checking missing values and duplicate records.

Removing duplicate rows.

Handling missing values using appropriate imputation rules.

Standardizing inconsistent text values.

Converting date and numeric columns to appropriate data types.

Removing records with zero or negative quantities or unit prices.

Calculating revenue using quantity, unit price, and discount.

2. Revenue Calculation

Revenue was calculated using the following formula:

Revenue = Quantity × Unit_Price × (1 - Discount)

This formula assumes that the discount is stored as a decimal fraction, such as 0.10 for a 10% discount.

3. Exploratory Data Analysis (EDA)

Exploratory analysis was used to examine revenue trends, category performance, city-level sales, product performance, payment methods, order statuses, and customer types.

4. SQL Analysis with PostgreSQL

The cleaned dataset was loaded into PostgreSQL for structured querying and business analysis.

SQL can be used to aggregate revenue, count distinct orders and customers, compare categories, and answer business questions.

5. Power BI Dashboard

An interactive dashboard was developed to make the analysis easier to understand and explore.

Dashboard Highlights

Key Performance Indicators (KPIs)

Total Revenue

Total Orders

Average Order Value

Total Customers

Visualizations

Monthly Revenue Trend — Tracks revenue over time.

Revenue by Category — Compares category contributions using a treemap.

Revenue by City — Compares revenue across cities using a bar chart.

Orders by Payment Mode — Compares order counts by payment method.

Orders by Status — Shows the distribution of order statuses using a donut chart.

New vs Returning Customers — Compares customer groups using a 100% stacked column chart.

Top 5 Products by Revenue — Highlights the products generating the most revenue.

Interactive slicers allow users to filter the dashboard and explore the data from different perspectives.

Key Metrics

The following metrics were calculated from the available dataset:

Metric

Value

Cleaned Records

7,478

Distinct Orders

7,478

Distinct Customers

2,129

Total Revenue

₹22,668,496.90

Average Order Value

₹3,031.36

Metric definitions:

Total Revenue: Sum of calculated revenue.

Total Orders: Distinct count of order IDs.

Total Customers: Distinct count of customer IDs.

Average Order Value: Total revenue divided by distinct order count.

These figures should be validated against the final cleaned dataset and Power BI measures before being used in a formal presentation.

Business Value

This project demonstrates how data analytics can help a business:

Monitor overall sales performance.

Identify high-revenue products and categories.

Compare revenue across cities.

Understand order and payment distributions.

Explore differences between new and returning customers.

Investigate revenue changes using interactive filters.

The results are descriptive and can guide further investigation. Additional information, such as costs, profit margins, and customer purchase history, would be needed for deeper profitability and retention analysis.

Skills Demonstrated

Data cleaning and preprocessing

Exploratory data analysis

Data aggregation and KPI calculation

SQL querying and database integration

Data visualization

Power BI dashboard development

Business-focused data storytelling

Conclusion

The E-Commerce Sales & Customer Analytics project demonstrates an end-to-end data analytics workflow using Python, PostgreSQL, and Power BI.

It combines data preparation, exploratory analysis, SQL-based investigation, and interactive visualization to turn raw e-commerce data into information that is easier to understand and use for business decisions.

The project also provides practical experience in data quality, metric definitions, dashboard design, and communicating analytical results.

Project Type: Data Analyticsrn, PostgreSQL, Power BI
