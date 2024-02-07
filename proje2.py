import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Veri setini yükleme
data = pd.read_csv("kargo_verileri.csv")

# Veri setinin ilk 5 satırını görüntüleme
print(data.head())

# Temel istatistikleri hesaplama (sadece sayısal sütunlar)
print(data.describe())

# Gönderi durumu sayısını görselleştirme
plt.figure(figsize=(8, 6))
sns.countplot(data=data, x='Gönderi Durumu')
plt.title('Gönderi Durumu Dağılımı')
plt.xlabel('Gönderi Durumu')
plt.ylabel('Sayı')
plt.xticks(rotation=45)
plt.show()

# Gönderi türüne göre ortalama ağırlık görselleştirme
plt.figure(figsize=(8, 6))
sns.barplot(data=data, x='Gönderi Tipi', y='Ağırlık', ci=None)  # ci=None parametresi hata çubuklarını kaldırır
plt.title('Gönderi Türüne Göre Ortalama Ağırlık')
plt.xlabel('Gönderi Türü')
plt.ylabel('Ortalama Ağırlık')
plt.xticks(rotation=45)
plt.show()

# Göndericiye göre gönderi sayısı görselleştirme (en çok gönderenler)
plt.figure(figsize=(10, 6))
top_senders = data['Gönderici'].value_counts().nlargest(10)
top_senders.plot(kind='bar')
plt.title('En Çok Gönderi Yapan Göndericiler')
plt.xlabel('Gönderici')
plt.ylabel('Gönderi Sayısı')
plt.xticks(rotation=45)
plt.show()

# Alıcıya göre gönderi sayısı görselleştirme (en çok alanlar)
plt.figure(figsize=(10, 6))
top_recipients = data['Alıcı'].value_counts().nlargest(10)
top_recipients.plot(kind='bar', color='orange')
plt.title('En Çok Gönderi Alan Alıcılar')
plt.xlabel('Alıcı')
plt.ylabel('Gönderi Sayısı')
plt.xticks(rotation=45)
plt.show()