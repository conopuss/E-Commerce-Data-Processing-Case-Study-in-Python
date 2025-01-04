This project focuses on developing an end-to-end data analysis pipeline for an e-commerce scenario. The goal is to analyze customer spending, product performance, and generate actionable insights using Python. This project demonstrates skills in data cleaning, visualization, and automation, providing a foundation for more advanced projects.

Features
Data Cleaning:
Addressed missing values in product prices.
Corrected inconsistent date formats and removed invalid entries.
Data Analysis:
Summarized yearly, monthly, and daily sales trends.
Identified customer spending patterns with a total_spent column.
Grouped sales by product categories to understand distribution.
Visualization:
Line chart for yearly sales trends.
Bar chart for monthly sales.
Pie chart for category-wise sales distribution.
Automation:
A script that processes .csv files and generates comprehensive reports in an Excel file.
Deliverables
Code Files:
data_cleaning.py: Cleans and prepares the data.
data_analysis.py: Performs the analysis and generates summaries.
data_visualization.py: Creates visualizations for trends and distributions.
automation_script.py: Automates the entire pipeline.
Generated Outputs:
sales_summary.xlsx: Consolidated Excel report with:
Yearly, monthly, and daily sales summaries.
Customer spending trends.
Product category sales distribution.
Visualizations:
Charts saved as .png files.
Intermediate CSV Files:
Cleaned and processed datasets.
Scenario


An e-commerce company provided datasets to analyze customer and product behavior:
________________________________________
Python Veri İşleme Case Study
Senaryo:
Bir e-ticaret şirketinin analitik departmanında çalışıyorsunuz. Şirket, satış, müşteri ve ürün verilerini içeren bir sistemden günlük olarak veri alıyor. Göreviniz, bu verileri temizlemek, analiz etmek ve anlamlı raporlar çıkarmaktır. Ayrıca, raporlamayı otomatikleştirmek ve potansiyel veri sorunlarını çözmek için bir Python script’i yazmanız gerekiyor.
________________________________________
Case Adımları
1. Veri Temizleme ve Hazırlama
Şirket size şu üç veri setini sağlamaktadır:
1.	sales.csv: Satış bilgileri.
2.	customers.csv: Müşteri bilgileri.
3.	products.csv: Ürün bilgileri.
Görevler:
•	sales.csv dosyasındaki eksik değerleri bulun ve uygun bir şekilde doldurun (örneğin, eksik ürün fiyatlarını products.csv dosyasından çekerek doldurun).
•	Tarih formatı hatalı olan kayıtları düzeltin (örneğin, sales_date sütununda "2024-11/25" gibi hatalı formatları doğru formata çevirin).
•	Satış verilerinde aykırı değerleri tespit edin (örneğin, birim fiyatı çok düşük veya çok yüksek olan satışlar) ve bu kayıtlarla ilgili bir rapor oluşturun.
________________________________________
2. Veri Manipülasyonu
•	Satış verisini yıllık, aylık ve günlük satış toplamları şeklinde gruplandırarak özetleyin.
•	Müşterilerin toplam alışveriş tutarını hesaplayarak yeni bir sütun ekleyin (total_spent).
•	Ürün verisiyle satış verisini birleştirerek (join işlemi) satışların ürün kategorisine göre dağılımını çıkarın.
________________________________________
3. Veri Analizi
•	En çok satış yapılan ürünleri ve bu ürünlerin kategorilerini belirleyin.
•	Hangi müşterilerin toplamda en fazla harcama yaptığını analiz edin ve sıralayın.
•	Satışların %80’ini oluşturan müşterileri belirleyin (Pareto analizi).
________________________________________
4. Dosya İşlemleri
•	Yukarıdaki işlemlerden sonra sonuçları üç farklı dosyaya kaydedin: 
o	daily_sales_summary.csv
o	top_customers.csv
o	product_sales_summary.csv
•	Çıktılarınızı Excel formatında birden fazla sheet ile kaydedin.
________________________________________
5. API ile Veri Alma ve İşleme
•	Bir döviz API’sine bağlanarak günlük USD/TRY kurunu alın.
•	Satış verisindeki toplam satış tutarını (TRY cinsinden) USD’ye çevirerek yeni bir sütun ekleyin.
________________________________________
6. Mini Otomasyon Görevi
•	Dosyaların bulunduğu klasördeki tüm *.csv dosyalarını otomatik olarak okuyup işleyen bir script yazın. Script: 
o	Verileri birleştirmeli.
o	Temizleme işlemlerini yapmalı.
o	Yukarıdaki özet raporları otomatik olarak oluşturmalı.
________________________________________
7. Hata Ayıklama ve Optimizasyon
•	Verilen bir Python kodu hatalı çalışmaktadır: 
•	for i in range(len(df)):
•	    if df['price'][i] > 100:
•	        df['discount'][i] = df['price'][i] * 0.1
Bu kodu düzeltin ve performansını optimize edin.




customers.csv: Customer details.
products.csv: Product catalog.
sales.csv: Transactional sales data.
Tasks Performed
Data Cleaning and Preparation:
Filled missing price data from products.csv.
Fixed invalid or inconsistent date entries in sales.csv.
Data Analysis:
Summarized sales by year, month, and day.
Computed total spending for each customer.
Aggregated sales data by product categories.
Visualization:
Line chart for yearly sales trends.
Bar chart for monthly sales summaries.
Pie chart for sales distribution across categories.
Automation:
Developed a script to read .csv files, clean the data, analyze it, and export the results as Excel and CSV files.
Tools & Technologies
Python (pandas, numpy, matplotlib, seaborn)
Excel Automation (via pandas' ExcelWriter)
Git for version control
