import pandas as pd
import matplotlib as plt
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

rata = data.groupby('Mapel') ['Nilai'].mean()
rata.plot(kind='bar')