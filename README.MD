# Praktikum 2

## Pertanyaan

---

1. Mapel mana yang memiliki rata-rata nilai tertinggi?  
2. Mapel mana yang memiliki nilai terendah?  
3. Bagaimana visualisasi membantu dalam memahami data?

---

## Refleksi Siswa

---

1. Apa hal baru yang kamu pelajari dari kegiatan analisis dan visualisasi data?  
2. Kesulitan apa yang kamu alami dalam membuat grafik?  
3. Menurut kamu, apakah AI membantu dalam analisis sebuah data?

---

## Deskripsi Program

Program ini digunakan untuk melakukan **analisis data nilai siswa** menggunakan bahasa pemrograman **Python** dengan library `pandas`, `matplotlib`, dan `seaborn`.

Langkah-langkah yang dilakukan pada program ini:

1. Membaca file data `nilai_siswa.csv` menggunakan `pandas`.
2. Menampilkan informasi dasar data (`info`, `head`, dan `describe`).
3. Menghitung nilai rata-rata, median, dan modus dari kolom **Nilai**.
4. Menampilkan data siswa dengan mata pelajaran **Matematika**.
5. Mengelompokkan data berdasarkan **Mapel** dan menampilkan nilai maksimum, minimum, serta rata-rata setiap mapel.
6. Membuat **visualisasi grafik batang** dan **boxplot** untuk mempermudah analisis.

---

## Kode Program

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('nilai_siswa.csv')
print(data.info())
print(data.head())
print(data.describe())

print("Rata-rata:", data['Nilai'].mean())
print("Rata-rata:", data['Nilai'].median())
print("Rata-rata:", data['Nilai'].mode()[0], "\n")

matematika = data[data['Mapel'] == 'Matematika']
print(matematika)

data.groupby('Mapel')['Nilai'].agg(['max','min'])

rata = data.groupby('Mapel')['Nilai'].mean()
rata.plot(kind='bar')

rata = data.groupby('Mapel')['Nilai'].mean()
rata.plot(kind='bar')
plt.title('Rata-Rata Nilai per Mapel')
plt.xlabel('Mata Pelajaran')
plt.ylabel('Nilai Rata-Rata')
plt.show()

sns.boxplot(x='Mapel', y='Nilai', data=data)
plt.title('Sebaran Nilai per Mata Pelajaran')
plt.show()

---

## Hasil Analisis

- Mengetahui **mapel dengan rata-rata nilai tertinggi**.
- Mengetahui **mapel dengan nilai terendah**.
- Data divisualisasikan untuk **memudahkan interpretasi** perbandingan nilai antar mapel.

---

## Kesimpulan

Analisis data ini membantu memahami sebaran nilai siswa antar mapel dan mengidentifikasi area yang perlu ditingkatkan. Visualisasi data dapat memberikan gambaran yang lebih jelas dan cepat dibanding hanya melihat tabel angka.
"""
