import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns   

data = pd.read_csv('nilai_siswa.csv')  
data.info()
data.head() 
data.describe() 

print("Rata Rata:", data["Nilai"].mean())
print("Median:", data["Nilai"].mean())
print("Modus:", data["Nilai"].mode()[0])
print(data.columns)


matematika = data[data["Matpel"] == "Matematika"]
print(matematika)

inggris = data[data["Matpel"] == "Bahasa Inggris"]
print(inggris)

Indonesia = data[data["Matpel"] == "Bahasa Indonesia"]
print(Indonesia)

data.groupby(by="Matpel")["Nilai"].agg(['max', 'min'])

rata = data.groupby("Matpel")["Nilai"].mean()
rata.plot(kind='bar', color=['skyblue', 'orange', 'lightgreen'])
plt.title('Rata-rata Nilai Siswa per Mata Pelajaran')
plt.xlabel('Mata Pelajaran')    
plt.ylabel('Rata-rata Nilai')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))
sns.boxplot(x='Matpel', y='Nilai', data=data, palette='pastel')

plt.title('Sebaran Nilai per Mata Pelajaran')
plt.xlabel('Mata Pelajaran')
plt.ylabel('Nilai')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()