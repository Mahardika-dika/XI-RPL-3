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

```

---

## Hasil Output

- Output Text

```plaintext
D:\Coding\SMK TELKOM\XI RPL 3\Python\praktikum 2>C:\Users\USER\AppData\Local\Programs\Python\Python314\python.exe "d:/Coding/SMK TELKOM/XI RPL 3/Python/praktikum 2/praktik-2.py"
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 22 entries, 0 to 21
Data columns (total 3 columns):
 #   Column    Non-Null Count  Dtype
---  ------    --------------  -----
 0   NamaNama  22 non-null     object
 1   Mapel     22 non-null     object
 2   Nilai     22 non-null     int64
dtypes: int64(1), object(2)
memory usage: 660.0+ bytes
RangeIndex: 22 entries, 0 to 21
Data columns (total 3 columns):
 #   Column    Non-Null Count  Dtype
---  ------    --------------  -----
 0   NamaNama  22 non-null     object
 1   Mapel     22 non-null     object
 2   Nilai     22 non-null     int64
dtypes: int64(1), object(2)
RangeIndex: 22 entries, 0 to 21
Data columns (total 3 columns):
 #   Column    Non-Null Count  Dtype
---  ------    --------------  -----
 0   NamaNama  22 non-null     object
 1   Mapel     22 non-null     object
 2   Nilai     22 non-null     int64
RangeIndex: 22 entries, 0 to 21
Data columns (total 3 columns):
 #   Column    Non-Null Count  Dtype
---  ------    --------------  -----
 0   NamaNama  22 non-null     object
 1   Mapel     22 non-null     object
RangeIndex: 22 entries, 0 to 21
Data columns (total 3 columns):
 #   Column    Non-Null Count  Dtype
---  ------    --------------  -----
 0   NamaNama  22 non-null     object
RangeIndex: 22 entries, 0 to 21
Data columns (total 3 columns):
 #   Column    Non-Null Count  Dtype
---  ------    --------------  -----
RangeIndex: 22 entries, 0 to 21
Data columns (total 3 columns):
 #   Column    Non-Null Count  Dtype
RangeIndex: 22 entries, 0 to 21
Data columns (total 3 columns):
 #   Column    Non-Null Count  Dtype
---  ------    --------------  -----
RangeIndex: 22 entries, 0 to 21
Data columns (total 3 columns):
 #   Column    Non-Null Count  Dtype
RangeIndex: 22 entries, 0 to 21
Data columns (total 3 columns):
RangeIndex: 22 entries, 0 to 21
Data columns (total 3 columns):
 #   Column    Non-Null Count  Dtype
---  ------    --------------  -----
 0   NamaNama  22 non-null     object
 1   Mapel     22 non-null     object
 2   Nilai     22 non-null     int64
dtypes: int64(1), object(2)
memory usage: 660.0+ bytes
None
  NamaNama             Mapel  Nilai
0      Ade  Bahasa Indonesia     87
1     Aira  Bahasa Indonesia     88
2     Badi    Bahasa Inggris     78
3     Cyla    Bahasa Inggris     90
4   Khansa        Matematika     98
           Nilai
count  22.000000
mean   86.318182
std     6.066193
min    75.000000
25%    85.000000
50%    86.500000
75%    90.000000
max    98.000000
Rata-rata: 86.31818181818181
Rata-rata: 86.5
Rata-rata: 85

  NamaNama       Mapel  Nilai
4   Khansa  Matematika     98
6      Dwi  Matematika     85

```

- Output Jendela Windows

![Windows Result](./Image/Diagram%20Rata-Rata%20Nilai.png)
![Windows Result](./Image/Diagram%20Sebaran%20per%20Mata%20Pelajaran.png)

---

## Hasil Analisis

- Mengetahui **mapel dengan rata-rata nilai tertinggi**.
- Mengetahui **mapel dengan nilai terendah**.
- Data divisualisasikan untuk **memudahkan interpretasi** perbandingan nilai antar mapel.

---

## Kesimpulan

Analisis data ini membantu memahami sebaran nilai siswa antar mapel dan mengidentifikasi area yang perlu ditingkatkan. Visualisasi data dapat memberikan gambaran yang lebih jelas dan cepat dibanding hanya melihat tabel angka.
"""
