import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:\Users\ASUS\Downloads\katalog_gempa.csv")
print(df.head())
print(df.info())
#df = data frame

df.columns = df.columns.str.strip()
df['tgl'] = pd.to_datetime(df['tgl'], errors = 'coerce')

df = df.dropna(subset=['tgl'])

for col in ['lat', 'lon', 'depth', 'mag']:
    df[col] = pd.to_numeric(df[col], errors= 'coerce')

df = df.dropna(subset=['lat', 'lon', 'depth', 'mag'])

df = df[(df['tgl'].dt.year >= 2021) & (df['tgl'].dt.year <= 2023)]

earthquake_jawa = ['Java', 'Bali Sea', 'South Indian Ocean']
df_jawa = df[df['remark'].str.contains('|'.join(earthquake_jawa), case=False, na=False)].copy()

print("\n=== DATA SETELAH DIBERSIHKAN ===")
print(df_jawa.head())
print("Jumlah kejadian gempa : ", len(df_jawa))

def klasifikasi_kerusakan(mag):
    if mag < 5.5:
        return 'Aman'
    elif 5.5 <= mag <= 6.0:
        return 'Kerusakan Ringan'
    else:
        return 'Kerusakan Berat'
    
df_jawa['kategori_kerusakan'] = df_jawa['mag'].apply(klasifikasi_kerusakan)

print("\n=== CONTOH DATA DENGAN KATEGORI KERUSAKAN ===")
print(df_jawa[['tgl', 'mag', 'kategori_kerusakan', 'remark']].head(20))

df_jawa.to_csv("data_gempa_jawa_dengan_kategori.csv", index=False)
print("\nFile berhasil disimpan sebagai 'data_gempa_jawa_dengan_kategori.csv'")

plt.figure(figsize=(10, 5))
sns.histplot(df_jawa['mag'], bins=15, kde=True)
plt.title('Distribusi Magnitudo Gempa di Wilayah Jawa (2021-2023)')
plt.xlabel('Magnitudo (mag)')
plt.ylabel('Frekuensi')
plt.show()

