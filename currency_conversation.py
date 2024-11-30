import requests
import pandas as pd

def fetch_try_to_usd_rate():

    print("Güncel ABD Doları / Türk Lirası kuru...")
    api_url =  "https://api.exchangerate-api.com/v4/latest/TRY"
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        try_to_usd_rate = data['rates']['USD']
        print(f"Güncel kur talebi başarılı: 1 TRY = {try_to_usd_rate} USD")
        return try_to_usd_rate
    else:
        print("HATA!")
        raise Exception("Veri getirilemedi")
def convert_sales_to_usd(sales, exchange_rate):
    print("Satış verileri USD ' ye dönüştürülüyor...")
    sales['price_per_unit_usd'] = sales['price_per_unit'] * exchange_rate
    print(f"Dönüştürme işlemi tamamlandı. Kullanılan döviz kuru: {exchange_rate}")
    return sales
if __name__ == "__main__":
    from data_cleaning import clean_data
    from data_manipulation import group_sales_by_date
    from currency_conversation import fetch_try_to_usd_rate, convert_sales_to_usd

    sales, products = clean_data()
    yearly_sales, monthly_sales, daily_sales = group_sales_by_date(sales)

    try:
        try_to_usd_rate = fetch_try_to_usd_rate()
    except Exception as e:
        print(f"Döviz kuru verisinde hata! {e}")
        exit()
    sales = convert_sales_to_usd(sales, try_to_usd_rate)

    sales.to_csv('sales_in_usd.csv', index=False)
    print("Satış verilerinin USD kuru karşılıkları 'sales_in_usd.csv' dosyasına kaydedildi.")
