import os
import glob
import pandas as pd

from currency_conversation import fetch_try_to_usd_rate, convert_sales_to_usd
from data_cleaning import clean_data
from data_manipulation import(
    group_sales_by_date, rank_top_customers, analyze_sales_by_category
)

def read_csv_files(folder_path):

    csv_files = glob.glob(os.path.join(folder_path, '*.csv'))

    #dataframe adında bir dictionary
    dataframes = {}

    #for dögüsü ile csv dosyaları
    for file in csv_files:

        #file_name = aranan .csv dosyasının adı, 'sales.csv' gibi...
        file_name = os.path.basename(file)

        #dictionary'deki dosyaları read_csv ile oku
        dataframes[file_name] = pd.read_csv(file)
        print(f"Yüklendi {file_name}")
    return dataframes

def process_data(dataframes):

    sales = dataframes.get('sales.csv')
    products = dataframes.get('products.csv')
    customers = dataframes.get('customers.csv')

    sales, products = clean_data()
    yearly_sales, monthly_sales,daily_sales = group_sales_by_date(sales)

    top_customers = rank_top_customers(sales, customers)
    sales_by_category = analyze_sales_by_category(sales, products)

    try:
        try_to_usd_rate = fetch_try_to_usd_rate()
        sales = convert_sales_to_usd(sales,try_to_usd_rate)
    except Exception as e:
        print(f"Döviz kuru işleminde hata: {e}")
    yearly_sales.to_csv('yearly_sales_summary.csv', index=False)
    monthly_sales.to_csv('monthly_sales_summary.csv', index=False)
    daily_sales.to_csv('daily_sales_summary.csv',index=False)
    top_customers.to_csv('top_customers.csv',index=False)
    sales_by_category.to_csv('product_sales_summary.csv',index=False)
    sales.to_csv('sales_in_usd.csv',index=False)

    print("Bütün dosyalar oluşturulup saklandı!")

if __name__ == "__main__":
    folder_path = "."
    dataframes = read_csv_files(folder_path)
    process_data(dataframes)