import pandas as pd
from deneme_df import dene_df

df = pd.DataFrame(dene_df)
df['discount'] = 0
#  Çalışmayan kodun çalışır hali
#for i in range(len(df)):
#    if df['price'][i] > 100:
#        df.at[i,'discount']= df['price'][i] * 0.1
print(df)

#for döngüsü yerine aşağıdaki kısmı kullanarak optimize edildi
df['discount'] = 0  # Initialize with zeros

df.loc[df['price'] > 100, 'discount'] = df['price'] * 0.1