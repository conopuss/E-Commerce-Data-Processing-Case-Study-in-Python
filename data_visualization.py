import pandas as pd
import matplotlib.pyplot as plt
import seaborn  as sns

from data_cleaning import  clean_data
from data_manipulation import group_sales_by_date

def plot_yearly_sales(yearly_sales):

    plt.figure(figsize=(10,6))
    plt.plot(yearly_sales.index, yearly_sales['price_per_unit'], marker='o', linestyle='-', color='b', label='Yearly Sales')
    plt.title('Yearly Sales Trends', fontsize=16)

    #yatay eksen
    plt.xlabel('Year', fontsize=12)

    #dikey eksen
    plt.ylabel('Total Sales (Price)', fontsize=12)
    plt.grid(True)
    plt.legend()
    plt.show()

def plot_monthly_sales(monthly_sales):
    monthly_sales = monthly_sales.reset_index()

    # Combine year and month for labels
    monthly_sales['year_month'] = monthly_sales['year'].astype(str) + '-' + monthly_sales['month'].astype(str)

    # Plot the bar chart
    plt.figure(figsize=(12, 6))

    # Assign colors explicitly without using 'palette'
    bar_colors = sns.color_palette('Blues_d', len(monthly_sales))
    for idx, bar_value in enumerate(monthly_sales['price_per_unit']):
        plt.bar(monthly_sales['year_month'][idx], bar_value, color=bar_colors[idx])

    # Chart customizations
    plt.title('Monthly Sales Trends', fontsize=16)
    plt.xlabel('Year-Month', fontsize=12)
    plt.ylabel('Total Sales (Price)', fontsize=12)
    plt.xticks(rotation=45)  # Rotate x-axis labels for readability
    plt.grid(axis='y', linestyle='--', alpha=0.7)  # Add gridlines for y-axis
    plt.tight_layout()  # Adjust layout for better visualization
    plt.show()

def plot_daily_sales(daily_sales):

    daily_sales = daily_sales.reset_index()

    daily_pivot = daily_sales.pivot_table(
        index='month', columns='day', values='price_per_unit', aggfunc='sum', fill_value=0
    )
    plt.figure(figsize=(16,10))
    sns.heatmap(
        daily_pivot, cmap='Blues', annot=True, fmt='.1f', linewidths=0.5, linecolor='gray',
        annot_kws={"size":10},
    )
    plt.title('Daily Sales Heatmap', fontsize=18)
    plt.xlabel('Day', fontsize=14)
    plt.ylabel('Month', fontsize=14)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':

    from data_cleaning import clean_data
    from data_manipulation import (group_sales_by_date, rank_top_customers, analyze_sales_by_category)
    from data_visualization  import plot_yearly_sales, plot_monthly_sales, plot_daily_sales

    sales, products = clean_data()
    yearly_sales, monthly_sales, daily_sales = group_sales_by_date(sales)

    plot_yearly_sales(yearly_sales)
    plot_monthly_sales(monthly_sales)
    plot_daily_sales(daily_sales)

    customers = pd.read_csv('customers.csv')
    top_customers = rank_top_customers(sales, customers)
    sales_by_category = analyze_sales_by_category(sales, products)

    daily_sales.to_csv('daily_sales_summary.csv', index=False)
    top_customers.to_csv('top_customers.csv', index=False)
    sales_by_category.to_csv('product_sales_summary', index=False)

    print("Sonuçlar ayrı birer .csv dosyası olarak kaydedildi")

    with pd.ExcelWriter('sales_summary.xlsx', engine='xlsxwriter') as writer:
        daily_sales.to_excel(writer, sheet_name='Daily Sales Summary', index=False)
        top_customers.to_excel(writer, sheet_name='Top Customers', index=False)
        sales_by_category.to_excel(writer, sheet_name='Product Sales Summary', index=False)
    print("Sonuçlar 'sales_summary.xlsx' dosyasına kaydeildi ")
