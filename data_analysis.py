#Burada  top_n=10 ile tablonun tamamındansa 10 tanesini getiriyor (ilk 10 değil ama)
import pandas as pd


def identify_best_selling_products(sales,products, top_n=10):

    best_selling = sales.groupby('product_id')['quantity'].sum().reset_index()
    best_selling.rename(columns={'quantity':'total_quantity'}, inplace=True)

    best_selling = best_selling.merge(products[['product_id','product_name','category']], on='product_id',how='left')

    #Ascending=False ile desc sağlıyor
    best_selling = best_selling.sort_values('total_quantity', ascending=False)

    print(f"En çok satılan {top_n} Ürün ve kategoriler")

    #Burada başına head gelince top_n ilk 10 anlamına geliyor [top_n dendiğinde sayı zaten 10 by default]
    print(best_selling.head(top_n))

    return best_selling.head(top_n)


def rank_top_customers(sales,customers, top_n=10):

    sales['total_spent'] = sales['price_per_unit'] * sales['quantity']

    #her bir müşteriyi ve toplam harcamasını ayrı ayrı grupla
    top_customers = sales.groupby('customer_id')['total_spent'].sum().reset_index()

    #aynı değişkeni hem veri atamak için hem de atanan verinin içinde kullandım!!!
    top_customers = top_customers.sort_values('total_spent',ascending=False)

    #aynı değişkeni modifiye edip müşteri adı ve emaili de ekliyorum
    top_customers = top_customers.merge(customers[['customer_id','customer_name','email']], on='customer_id', how='left')

    print(f"En çok harcayan {top_n} mişteri:")
    print(top_customers.head(top_n))

    return  top_customers.head(top_n)

def pareto_analysis(top_customers, treshold=0.8):

    total_sales = top_customers['total_spent'].sum()
    top_customers['cumulative_spent'] = top_customers['total_spent'].cumsum()
    top_customers['cumulative_percent'] = top_customers['cumulative_spent'] / total_sales

    pareto_customers = top_customers[top_customers['cumulative_percent'] <= treshold]

    print(f"Müşteri, toplam satışların %{treshold * 100} kısmından sorumludur:")
    print(pareto_customers)

    return pareto_customers

if __name__ == "__main__":
    from data_cleaning import clean_data
    from data_manipulation import analyze_sales_by_category
    from data_analysis import (
        rank_top_customers,
        pareto_analysis,
        identify_best_selling_products,
    )

    # Clean and load data
    sales, products = clean_data()
    customers = pd.read_csv('customers.csv')

    # Rank top customers and save to CSV
    top_customers = rank_top_customers(sales, customers)
    top_customers.to_csv('top_customers.csv', index=False)
    print("En çok harcayan müşteriler 'top_customers.csv' dosyasına kaydedildi.")

    # Perform Pareto analysis and save to CSV
    pareto_customers = pareto_analysis(top_customers)
    pareto_customers.to_csv('pareto_customers.csv', index=False)
    print("Pareto analizi tamamlandı ve 'pareto_customers.csv' dosyasına kaydedildi.")

    # Identify best-selling products and save to CSV
    best_selling = identify_best_selling_products(sales, products)
    best_selling.to_csv('best_selling_products.csv', index=False)
    print("En çok satılan ürünler 'best_selling_products.csv' dosyasına kaydedildi.")

    # Analyze sales by category (if needed)
    sales_by_category = analyze_sales_by_category(sales, products)
    sales_by_category.to_csv('sales_by_category.csv', index=False)
    print("Satışların kategoriye göre dağılımı 'sales_by_category.csv' dosyasına kaydedildi.")



