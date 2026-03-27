# E-commerce Data Analysis Case Study

## Project Overview

This project simulates a real-world business scenario for an e-commerce company.
The objective is to clean, analyze, and model the data in order to generate business insights and support data-driven decision making.

The project covers the complete data analytics workflow:

* Data Cleaning
* Data Modeling
* Exploratory Data Analysis (EDA)
* SQL Analysis
* KPI Engineering
* Business Insights
* Dashboard Creation

The final result is an interactive dashboard that highlights key performance indicators and business insights.

---

# Dataset Description

The dataset simulates an e-commerce environment and contains five main tables:

### Customers

Information about customers including country, segment, and signup date.

### Products

Product catalog with product category and price.

### Orders

Orders placed by customers including order date and order status.

### Order Items

Details of products included in each order.

### Payments

Payment information including payment method and payment status.

The dataset intentionally includes real-world data issues such as:

* Missing values
* Duplicate records
* Returns and cancellations
* Failed payments

---

# Data Cleaning

Data cleaning was performed using Python to ensure the dataset was ready for analysis.

Key steps included:

* Handling missing values in customer data
* Removing duplicate orders
* Checking data types and formatting
* Validating relationships between tables
* Preparing datasets for analysis

---

# Data Modeling

The data follows a relational model typical for e-commerce systems.

Main relationships:

Customers → Orders
Orders → Order Items
Products → Order Items
Orders → Payments

This structure allows accurate revenue calculation and customer behavior analysis.

---

# Exploratory Data Analysis (EDA)

Exploratory analysis was performed using Python to better understand the dataset and identify patterns.

Examples of analysis performed:

* Revenue by country
* Revenue by customer segment
* Product category performance
* Return and cancellation analysis
* Payment method performance

---

# KPI Engineering

Several key business metrics were created:

**Total Revenue**
Total sales generated from all orders.

**Net Revenue**
Revenue excluding returned or cancelled orders.

**Average Order Value (AOV)**
Average revenue generated per order.

**Customer Lifetime Value (CLV)**
Basic estimation of the revenue generated per customer.

**Churn Proxy**
Customers who have not placed orders within a defined time window.

---

# Dashboard

An interactive dashboard was created to visualize business performance.

Main components include:

* KPI overview
* Revenue trends
* Customer segment analysis
* Product category performance
* Returns and cancellations
* Payment method analysis

The dashboard allows filtering by:

* Country
* Customer Segment
* Product Category
* Payment Method
* Order Status

---

# Business Questions Answered

This project addresses key business questions:

* What factors drive revenue?
* Which customer segment generates the most value?
* Where are losses occurring due to returns or cancellations?
* Which payment methods show higher risk?
* What improvements could increase profitability?

---

# Tools & Technologies

Python
Pandas
NumPy
SQL
Power BI

---

# Project Structure

Data/
Raw datasets generated for the analysis

Notebooks/
Python notebooks for cleaning, EDA, and KPI calculations

SQL/
SQL queries used for analysis

Power-BI-Dashboard/
Power BI dashboard file

Data_Script.py
Script used to generate the dataset

---

# Key Outcome

This project demonstrates the ability to perform end-to-end data analysis including data preparation, analytical modeling, KPI development, and business insight generation.
