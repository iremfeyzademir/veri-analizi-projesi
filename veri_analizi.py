import pandas as pd

# Basit bir veri seti oluştur
data = {
    "İsim": ["Ali", "Ayşe", "Mehmet", "Zeynep"],
    "Yaş": [25, 30, 35, 40],
    "Maaş": [5000, 6000, 7000, 8000]
}

df = pd.DataFrame(data)

# Veriyi ekrana yazdır
print(df)
