import pandas as pd  # panda kütüp.

def clean_data():
    # sales.cvs'yi, sales değişkenine yükle
    sales = pd.read_csv('sales.csv')
    products = pd.read_csv('products.csv')

    # kolon tipleri sorunlu oldu, ikisini de string yaptık
    sales['product_id'] = sales['product_id'].astype(str)
    products['product_id'] = products['product_id'].astype(str)

    # SQL'deki join gibi düşün   SELECT s.*, p.price
    #                            FROM sales AS s
    #                            LEFT JOIN products AS p
    #                            ON s.product_id = p.product_id;
    sales = sales.merge(products[['product_id', 'price']], on='product_id', how='left')
    # sales içerisindeki price_per_unit kolunu, products'ta price olarak geçiyor, sales tablosundaki
    # kolonu ona göre dolduruyoruz.
    sales['price_per_unit'] = sales['price_per_unit'].fillna(sales['price'])
    # Drop the additional 'price' column after filling
    sales.drop(columns=['price'], inplace=True)

    sales = clean_dates(sales)
    return sales, products

 #bozuk formattaki tarihler için
def clean_dates(sales):

    #sales_date girişlerini uygun formata çevir
    sales['sales_date'] = pd.to_datetime(sales['sales_date'], errors='coerce')

    #yanlış tarih girişlerini invalid_dates değişkenine ata
    invalid_dates= sales[sales['sales_date'].isnull()]

    #eğer invalid_dates değişkeni boş değilse yani yanlış formatta tarih varsa
    if not invalid_dates.empty:
        print(f"Formda bulunan yanlış tarih girişleri:\n{invalid_dates}")

    return sales


# aykırı fiyatlandırmaları bulmak için
def detect_outliers(sales):

    #(n-1) * 0.25   yani index değeri * 0.25 ile pozisyounu bul arından
    #eğer bu tam sayı değilse bu pozisyondaki iki sayının farkı * 0.25 + pozisyondaki büyük sayı
    Q1 = sales['price_per_unit'].quantile(0.25)

    #aynı işlem bu sefer 0.75 ile
    Q3 = sales['price_per_unit'].quantile(0.75)

    IQR = Q1 -Q3

    # burada 1.5 standart ve bu heplama için en optimal yani karar sayı ile üst ve alt sınır hesabı
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    #aykırı değer = sales, price_per_unit kolonunda alt sınırdan küçük ve üst sınırdan büyük değerler
    outliers = sales[(sales['price_per_unit'] < lower_bound) | (sales['price_per_unit'] > upper_bound)]

    print(f"Aykırı değerler: En düşük = {lower_bound}, Upper = {upper_bound}")

    #len , lenght için kullanılıyor!
    print(f"Aykırı değer toplam: {len(outliers)} tane")

    return outliers


if __name__ == "__main__":
    sales, products = clean_data()

    outliers = detect_outliers(sales)

    outliers.to_csv('outliers_report.csv', index=False)
    print("Aykırı fiyatlar 'outlier_report.csv' dosyasında saklandı")












