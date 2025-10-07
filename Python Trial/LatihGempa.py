import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from geopy.distance import geodesic
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv(r"C:\Users\ASUS\Downloads\katalog_gempa.csv")
print(df.head())
print(df.info())

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

plt.figure(figsize=(10, 5))
sns.histplot(df_jawa['mag'], bins=15, kde=True)
plt.title('Distribusi Magnitudo Gempa di Wilayah Jawa (2021-2023)')
plt.xlabel('Magnitudo (mag)')
plt.ylabel('Frekuensi')
plt.show()

PUSAT_JAWA = (-7.7956, 110.3695)

def hitung_jarak_km(lat, lon):
    titik_gempa = (lat, lon)
    return geodesic(PUSAT_JAWA, titik_gempa).km

df_jawa['jarak_dari_pusat_km'] = df_jawa.apply(
    lambda row: hitung_jarak_km(row['lat'], row['lon']),
    axis=1
)

BATAS_MAG_NORMAL = 3.4
df_jawa['kategori_mag_normal'] = np.where(
    df_jawa['mag'] > BATAS_MAG_NORMAL,
    f'> {BATAS_MAG_NORMAL} SR (Besar)',
    f'<= {BATAS_MAG_NORMAL} SR (Normal)'
)

df_visual = df_jawa.sort_values(
    by=['jarak_dari_pusat_km', 'mag', 'depth'],
    ascending=[False, False, False]
)

# IMPLEMENTASI RANDOM FOREST REGRESSION

X_reg = df_jawa[['lat', 'lon', 'depth', 'jarak_dari_pusat_km']]
y_reg = df_jawa['mag']

X_train_reg, X_test_reg, y_train_reg, y_test_reg = train_test_split(
    X_reg, y_reg, 
    test_size=0.2, 
    random_state=42
)

model_rfr = RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1)
model_rfr.fit(X_train_reg, y_train_reg)

y_pred_reg = model_rfr.predict(X_test_reg)

mse = mean_squared_error(y_test_reg, y_pred_reg)
rmse = np.sqrt(mse)
r2 = r2_score(y_test_reg, y_pred_reg)

print("\n\n=== HASIL EVALUASI RANDOM FOREST REGRESSION ===")
print(f"Memprediksi Target: Magnitudo (mag)")
print(f"Metrik RMSE (Akar Kuadrat Rata-rata Eror): {rmse:.4f}")
print(f"Metrik R-squared (Koefisien Determinasi): {r2:.4f}")

feature_importances_rfr = pd.Series(model_rfr.feature_importances_, index=X_reg.columns)
print("\nKEPENTINGAN FITUR DALAM MEMPREDIKSI MAGNITUDO:")
print(feature_importances_rfr.sort_values(ascending=False))


# VISUALISASI 1: Kedalaman, Jarak, dan Magnitudo (Data Awal)

plt.figure(figsize=(14, 8))

scatter = sns.scatterplot(
    data=df_visual,
    x='jarak_dari_pusat_km',
    y='depth',
    hue='mag',
    size='mag',
    palette='viridis',
    sizes=(30, 300),
    alpha=0.7,
    style='kategori_mag_normal'
)

plt.title(f'Visualisasi 1: Korelasi Kedalaman, Jarak, dan Magnitudo Gempa di Jawa (2021-2023)', fontsize=16)
plt.xlabel('Jarak dari Pusat Jawa (km)', fontsize=12)
plt.ylabel('Kedalaman (depth) (km)', fontsize=12)

plt.gca().invert_yaxis()

norm = plt.Normalize(df_visual['mag'].min(), df_visual['mag'].max())
sm = plt.cm.ScalarMappable(cmap="viridis", norm=norm)
sm.set_array([])
scatter.figure.colorbar(sm, label='Magnitudo (SR)', ax=plt.gca())

plt.grid(True, linestyle='--', alpha=0.6)
plt.show() 

plt.figure(figsize=(10, 6))

plt.scatter(y_test_reg, y_pred_reg, alpha=0.6, label='Titik Data Prediksi')


plt.plot([y_test_reg.min(), y_test_reg.max()], 
         [y_test_reg.min(), y_test_reg.max()], 
         '--r', linewidth=2, label='Prediksi Ideal')

plt.title('Visualisasi 2: Magnitudo Aktual vs. Prediksi (Random Forest Regression)')
plt.xlabel('Magnitudo Aktual (SR)')
plt.ylabel('Magnitudo Prediksi (SR)')
plt.legend()
plt.grid(True)
plt.show() 

print("\nRINGKASAN DATA VISUALISASI (Top 5 Gempa Terjauh, Terbesar, dan Terdalam)")

print(df_visual[['tgl', 'mag', 'depth', 'jarak_dari_pusat_km', 'kategori_kerusakan', 'kategori_mag_normal']].head())
