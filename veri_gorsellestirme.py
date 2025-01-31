import pandas as pd
import matplotlib.pyplot as plt

# Örnek veri seti
data = {
    "İsim": ["Ali", "Ayşe", "Mehmet", "Zeynep"],
    "Yaş": [25, 30, 35, 40],
    "Maaş": [5000, 6000, 7000, 8000]
}

df = pd.DataFrame(data)

# Yaş ve maaş ilişkisini görselleştir
plt.bar(df["İsim"], df["Maaş"], color='skyblue')
plt.xlabel("İsim")
plt.ylabel("Maaş")
plt.title("Çalışan Maaş Dağılımı")
plt.show()
