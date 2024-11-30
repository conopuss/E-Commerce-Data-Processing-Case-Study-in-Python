import pandas as pd
from data_cleaning import clean_data

def group_sales_by_date(sales):

    #.dt.*  komutuyla sales_date kolonundan yılı alıp year, month vs adında bir kolonda topluyor
    sales['year'] = sales['sales_date'].dt.year
    sales['month'] = sales['sales_date'].dt.month
    sales['day'] = sales['sales_date'].dt.day

    #Dataframe'ler yaratıyor yearly_sales vs diye ve bunların içerisine eğer yılsa
    #aynı yıla ait numeric olan kolonların(miktar fiyat gibi) toplamını veriyor;
    #2024 yılında yapılan bütün satışların toplam quantity veya toplam price_per_unit gibi
    yearly_sales =sales.groupby('year').sum(numeric_only=True)
    monthly_sales = sales.groupby(['year','month']).sum(numeric_only=True)
    daily_sales = sales.groupby(['year','month','day']).sum(numeric_only=True)

    print("Yıllık Satış:")
    print(yearly_sales)
    print("\nAylık Satış:")
    print(monthly_sales)
    print("\nGünlük Satış")
    print(daily_sales)

    return yearly_sales, monthly_sales, daily_sales

def calculate_customer_spending(sales):

    #MsSql'den farklı olarak groupby komutu sadece görüntülemiyor, dataframe'i değiştiriyor
    #bu sebeple 'reset_index' ile eski haline getiriyoruz.
    customer_spending = sales.groupby('customer_id')['price_per_unit'].sum().reset_index()
    customer_spending.rename(columns={'price_per_unit': 'total_spent'}, inplace=True)

    sales = sales.merge(customer_spending, on='customer_id', how='left')

    print("Müşteri haracamları hesaplanıp 'sales' dataframe'e eklendi.")
    return sales

def analyze_sales_by_category(sales, products):

    # Product ve category tabloları prodcut_id üzerinden join ediliyor
    merged_data = sales.merge(products[['product_id', 'category']], on='product_id', how='left')

    # quantity kolumunu kategoriye göre grupla ve topla sonra eski haline getir
    sales_by_category = merged_data.groupby('category')['quantity'].sum().reset_index()

    #Burada inplace=True dediğimizde olan dataframe'i modifiye ediyor. Eğer bu komut olmazsa
    #kendiğinden söylenene göre yeni bir dataframe açıyor!
    sales_by_category.rename(columns={'quantity': 'total_quantity'}, inplace=True)

    print("Satışların kategoriye göre dağılımı:")
    print(sales_by_category)

    return sales_by_category

def rank_top_customers(sales, customers):

    customer_spending = sales.groupby('customer_id')['price_per_unit'].sum().reset_index()
    customer_spending.rename(columns={'price_per_unit': 'total_spent'}, inplace=True)

    ranked_customers = customer_spending.merge(customers[['customer_id', 'customer_name', 'email']],
                                               on='customer_id', how='left')
    ranked_customers = ranked_customers.sort_values('total_spent',ascending=False)

    print('Müşteri harcamaları hesaplanıp sıralandı:')
    print(ranked_customers)

    return ranked_customers

if __name__ == "__main__":

    #ilk dosyadan clean_data'yı yükle ancak buradaki sales ve products zaten ayıklanmış dataframe
    sales,products = clean_data()
    #aynı prensip! Bu sayede sonraki kullanıma hazır oluyor!
    yearly_sales, monthly_sales, daily_sales = group_sales_by_date(sales)

    yearly_sales.to_csv('yearly_sales.csv')
    monthly_sales.to_csv('monthly_sales.csv')
    daily_sales.to_csv('daily_sales.csv')

    print("Gruplanmış satış verileri CSV dosyalarına kaydedildi")

    sales = calculate_customer_spending(sales)
    sales.to_csv('sales_with_spending.csv', index=False)

    print("Müşteri harcamaları hesaplanıp 'sales_with_spending.csv' dosyasına kaydedildi.")

    sales_by_category = analyze_sales_by_category(sales, products)
    sales_by_category.to_csv('sales_by_category',index=False)
    print("Satışların kategoriye göre dağılımı 'sales_by_category.csv' dosyasına kaydedildi.")
