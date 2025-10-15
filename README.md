Overview

This project develops an end-to-end data processing and analysis pipeline for an e-commerce company.
The goal is to clean, analyze, visualize, and automate reporting of sales, customer, and product data using Python.
It demonstrates practical skills in data cleaning, transformation, visualization, and automation, providing a strong foundation for data engineering and analytics projects.

Features
🧹 Data Cleaning & Preparation

Handled missing product prices using cross-references from products.csv.

Corrected inconsistent or invalid date formats in sales.csv.

Detected and reported outliers in sales data (e.g., unusually high or low unit prices).

📊 Data Analysis

Summarized yearly, monthly, and daily sales trends.

Calculated total customer spending (total_spent).

Joined datasets to analyze sales distribution by product categories.

Identified top-selling products and customers.

Performed Pareto analysis (80/20 rule) to find customers generating most of the sales.

📈 Visualization

Line chart: Yearly sales trends.

Bar chart: Monthly sales summaries.

Pie chart: Category-wise sales distribution.

⚙️ Automation

A Python script processes all .csv files in the folder automatically.

Cleans and merges data, performs analysis, and exports results to multi-sheet Excel files.

Fetches daily USD/TRY exchange rate via API and adds a converted sales column.

Deliverables

Code Files

File	Description
data_cleaning.py	Cleans and prepares the raw data.
data_analysis.py	Performs aggregation and analysis.
data_visualization.py	Creates charts and graphs.
automation_script.py	Automates the entire process from input to output.

Generated Outputs

sales_summary.xlsx:

Multi-sheet Excel report with yearly, monthly, and daily summaries.

Customer spending patterns and product category distributions.

daily_sales_summary.csv, top_customers.csv, product_sales_summary.csv: Exported analysis results.

Visualizations saved as .png files.

Cleaned intermediate CSVs for future use.

Tools & Technologies

Python – Pandas, NumPy, Matplotlib, Seaborn

Excel Automation – via Pandas ExcelWriter

API Integration – Currency exchange API (USD/TRY)

Version Control – Git

Scenario Summary

An e-commerce company provides daily sales, customer, and product data.
Your task is to clean, analyze, and report on this data while automating the process through Python scripts.
The resulting pipeline supports reliable analytics and reporting for business decision-making.
