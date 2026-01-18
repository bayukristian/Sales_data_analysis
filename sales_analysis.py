import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data_penjualan.csv')
df.head()
df.isna().sum()      # cek missing value
df.duplicated().sum()  # cek duplikasi
df['total_penjualan'] = df['harga'] * df['qty'] # hitung total penjualan
#print (df)
# total_revenue = df['total_penjualan'].sum() #hitung total revenue
#print(total_revenue)
# print(df.groupby('kategori')['total_penjualan'].sum()) #grouping per kategori
# df.groupby('produk')['qty'].sum().sort_values(ascending=False) #nyari top product
# df.groupby('customer')['total_penjualan'].sum().sort_values(ascending=False) #nyari top customer


df.groupby('kategori')['total_penjualan'].sum().plot(kind='bar')
plt.title("Total Penjualan per Kategori")
plt.ylabel("Revenue")
plt.show()



