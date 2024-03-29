import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Veri setini yükleme
data = pd.read_csv("veri_seti.csv")

# Veri setinin ilk 5 satırını görüntüleme
print(data.head())

# Temel istatistikleri hesaplama
print(data.describe())

# Histogram görselleştirmesi
plt.hist(data["Satın Alma Tutarı"], bins=20)  # Histogram için "Satın Alma Tutarı" sütununu kullanın
plt.xlabel("Değerler")
plt.ylabel("Frekans")
plt.title("Histogram")
plt.show()

# Kutu grafiği görselleştirmesi
sns.boxplot(data=data)
plt.title("Kutu Grafiği")
plt.show()

# Korelasyon matrisi için sayısal sütunları seçme
numeric_columns = data.select_dtypes(include=['float64', 'int64']).columns
correlation_matrix = data[numeric_columns].corr()

# Korelasyon matrisini görselleştirme
sns.heatmap(correlation_matrix, annot=True)
plt.title("Korelasyon Matrisi")
plt.show()