# Import required libraries
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df_day = pd.read_csv("day_clean.csv")
df_hour = pd.read_csv("hour_clean.csv")

# Convert date columns to datetime
df_day['dteday'] = pd.to_datetime(df_day['dteday'])
df_hour['dteday'] = pd.to_datetime(df_hour['dteday'])
df_day['yr'] = df_day['yr'].replace({0: 2011, 1: 2012})
df_hour['yr'] = df_hour['yr'].replace({0: 2011, 1: 2012})

# Dashboard title
st.title("🚴‍♂️ Analisis Penyewaan Sepeda")
st.markdown("""
**Analisis Penyewaan Sepeda** bertujuan untuk memahami perilaku pengguna dan tren penyewaan sepeda berdasarkan waktu, cuaca, dan hari kerja.
""")

st.sidebar.header("Navigasi")
options = ["Tren Penyewaan per Jam", "Peminjaman Hari Kerja vs Non-Hari Kerja", "Pengaruh Suhu terhadap Peminjaman", "Clustering Jam"]
selected_option = st.sidebar.selectbox("Pilih Analisis", options)

if selected_option == "Tren Penyewaan per Jam":
    st.header("📈 Tren Penyewaan per Jam")
    
   
    hourly_trend = df_hour.groupby('hr')['cnt'].sum().reset_index()
    
    
    plt.figure(figsize=(10, 6))
    sns.lineplot(x='hr', y='cnt', data=hourly_trend, marker='o', color='b')
    plt.title('Total Jumlah Penyewaan per Jam dalam Sehari')
    plt.xlabel('Jam (00.00-23.59)')
    plt.ylabel('Jumlah Total Penyewaan')
    plt.xticks(range(0, 24))
    plt.grid(True)
    st.pyplot(plt)
    
    
    max_rental_hour = hourly_trend.loc[hourly_trend['cnt'].idxmax()]
    st.markdown(f"**Jam Puncak:** Jam {max_rental_hour['hr']} dengan {max_rental_hour['cnt']} penyewaan.")


elif selected_option == "Peminjaman Hari Kerja vs Non-Hari Kerja":
    st.header("📊 Peminjaman: Hari Kerja vs Non-Hari Kerja")
    

    hourly_trend_working_day = df_hour.groupby(['hr', 'workingday'])['cnt'].sum().reset_index()
    hourly_trend_working_day['day_type'] = hourly_trend_working_day['workingday'].map({1: 'Hari Kerja', 0: 'Hari Non-Kerja'})


    plt.figure(figsize=(12, 6))
    sns.lineplot(data=hourly_trend_working_day, x='hr', y='cnt', hue='day_type', marker='o')
    plt.title('Perbandingan Penyewaan Sepeda antara Hari Kerja dan Non-Hari Kerja per Jam')
    plt.xlabel('Jam (00.00-23.59)')
    plt.ylabel('Jumlah Total Penyewaan')
    plt.xticks(range(0, 24))
    plt.grid(True)
    plt.legend(title='Tipe Hari')
    st.pyplot(plt)


elif selected_option == "Pengaruh Suhu terhadap Peminjaman":
    st.header("🌡️ Pengaruh Suhu terhadap Peminjaman Sepeda")
    

    plt.figure(figsize=(10, 6))
    sns.regplot(x='temp', y='cnt', data=df_hour, scatter_kws={'alpha': 0.6}, line_kws={'color': 'red'})
    plt.title('Korelasi antara Suhu dan Jumlah Peminjaman Sepeda dengan Garis Regresi')
    plt.xlabel('Suhu (Skala Normalisasi)')
    plt.ylabel('Jumlah Peminjaman Sepeda')
    plt.grid(True)
    st.pyplot(plt)

    correlation = df_hour['temp'].corr(df_hour['cnt'])
    st.markdown(f"**Koefisien Korelasi:** {correlation:.2f}")


elif selected_option == "Clustering Jam":
    st.header("🔍 Clustering Jam Berdasarkan Tingkat Kesibukan")
    

    total_peminjaman_per_jam = df_hour.groupby('hr')['cnt'].sum().reset_index()
    

    threshold = total_peminjaman_per_jam['cnt'].median()
    total_peminjaman_per_jam['jam_kategori'] = total_peminjaman_per_jam['cnt'].apply(
        lambda x: 'Sibuk' if x > threshold else 'Tidak Sibuk'
    )


    plt.figure(figsize=(10, 6))
    sns.barplot(data=total_peminjaman_per_jam, x='hr', y='cnt', hue='jam_kategori', palette='pastel')
    plt.title('Total Peminjaman Sepeda per Jam dan Kategorinya')
    plt.xlabel('Jam (00.00-23.59)')
    plt.ylabel('Jumlah Total Peminjaman')
    plt.xticks(range(0, 24))
    plt.legend(title='Kategori Jam')
    plt.grid(True)
    st.pyplot(plt)

st.sidebar.markdown("""
---

### 💌 Kontak
- **Nama:** Dzikri Maulana  
- **Email:** [dzikrimaulana1781945@gmail.com](mailto:dzikrimaulana1781945@gmail.com)  
- **ID Dicoding:** dzikrimaulana87  
""")
