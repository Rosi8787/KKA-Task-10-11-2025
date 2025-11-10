import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 


data = pd.read_csv('nilai_siswa - nilai_siswa.csv', sep=',') 


data.info() 

data.head() 

data.describe()

# 22. Hitung rata-rata, median, dan modus nilai mata pelajaran:
print("Rata-rata:", data['Nilai'].mean()) 
print("Median:", data['Nilai'].median()) 
print("Modus:", data['Nilai'].mode()[0]) 


matematika = data[data['Mapel'] == 'Matematika'] 
print("\n--- Nilai Matematika ---")
print(matematika) # [cite: 41]

# 29. Lanjutkan untuk menampilkan nilai mata Pelajaran yang lain:
bahasa_inggris = data[data['Mapel'] == 'Bahasa Inggris']
print("\n--- Nilai Bahasa Inggris ---")
print(bahasa_inggris)

bahasa_indonesia = data[data['Mapel'] == 'Bahasa Indonesia']
print("\n--- Nilai Bahasa Indonesia ---")
print(bahasa_indonesia)

produktif = data[data['Mapel'] == 'Produktif']
print("\n--- Nilai Produktif ---")
print(produktif)

# 30. Tampilkan nilai maksimum dan minimum per mata pelajaran:
print("\n--- Nilai Maksimum dan Minimum per Mata Pelajaran ---")
print(data.groupby('Mapel')['Nilai'].agg(['max', 'min'])) # [cite: 45]

# 32. Buat grafik batang (bar chart) rata-rata nilai per mapel:
rata_rata_mapel = data.groupby('Mapel')['Nilai'].mean() # [cite: 46]
rata_rata_mapel.plot(kind='bar') # [cite: 48]
plt.title('Rata-Rata Nilai per Mapel') # [cite: 49]
plt.xlabel('Mata Pelajaran') # [cite: 50]
plt.ylabel('Nilai Rata-Rata') # [cite: 51]
plt.show() # [cite: 52]

# 39. Buat diagram boxplot untuk melihat sebaran nilai:
sns.boxplot(x='Mapel', y='Nilai', data=data) # [cite: 54]
plt.title('Sebaran Nilai per Mata Pelajaran')
plt.show()