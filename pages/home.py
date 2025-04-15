import streamlit as st
import pandas as pd
import numpy as np
from minisom import MiniSom
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from collections import Counter

st.title("🎓 Clustering Mahasiswa Berdasarkan Karakter")

# --- Input Mahasiswa Baru dan Donut Chart ---
st.subheader("📝 Isi Karakter Mahasiswa (Jawaban Ya / Tidak)")


pertanyaan = {
    "Logika": "Suka memecahkan masalah logika?",
    "Coding": "Suka menulis kode program?",
    "Desain": "Tertarik pada desain visual?",
    "Bisnis": "Tertarik membangun bisnis?",
    "Organisasi": "Senang berorganisasi?",
    "Praktik": "Lebih suka praktik daripada teori?"
}

jawaban = {}

nama = st.text_input("Nama Mahasiswa", value="Mahasiswa Baru")

col1, col2 = st.columns([2, 1])
with col1:
    for key, text in pertanyaan.items():
        jawaban[key] = st.radio(text, ["Ya", "Tidak"], horizontal=True)

def to_num(j):
    return 1 if j == "Ya" else 0

data_input = [to_num(jawaban[k]) for k in pertanyaan.keys()]

with col2:
    st.markdown("### 📊 Karakter Mahasiswa")
    labels = list(pertanyaan.keys())
    fig_donut = go.Figure(data=[go.Pie(
        labels=labels,
        values=data_input,
        hole=0.5,
        marker_colors=['#66b3ff','#99ff99','#ffcc99','#ff9999','#c2c2f0','#ffb3e6']
    )])
    fig_donut.update_layout(
        showlegend=False,
        margin=dict(t=10, b=10),
        height=300
    )
    st.plotly_chart(fig_donut, use_container_width=True)

# --- Load Dataset dan Latih SOM ---
try:
    df = pd.read_csv("dataset.csv")
except FileNotFoundError:
    df = pd.DataFrame(columns=["Nama"] + list(pertanyaan.keys()))

X = df.drop(columns=["Nama"]).values.astype(float)


if len(X) > 0:
    scaler = MinMaxScaler(feature_range=(-1, 1))
    X_scaled = scaler.fit_transform(X)

    som = MiniSom(x=5, y=5, input_len=6, sigma=1.0, learning_rate=0.5)
    som.random_weights_init(X_scaled)
    som.train_random(X_scaled, 100)

    new_scaled = scaler.transform([data_input])[0]
    winner = som.winner(new_scaled)

    st.success(f"✅ Input Normalisasi: {new_scaled}")
    st.info(f"📍 Posisi Klaster Mahasiswa Baru: {winner}")

    # --- Simpan Data Baru ---
    if st.button("💾 Simpan Data Mahasiswa Baru"):
        df.loc[len(df.index)] = [nama] + data_input
        df.to_csv("dataset.csv", index=False)
        st.success("Data berhasil disimpan!")

    col3, col4 = st.columns([1, 1])
    with col3:
        # --- Visualisasi SOM (U-Matrix) ---
        st.subheader("🧠 Peta Self-Organizing Map (SOM)")

        u_matrix = som.distance_map().T
        fig, ax = plt.subplots(figsize=(8, 8))
        im = ax.imshow(u_matrix, cmap='bone_r')
        plt.colorbar(im, ax=ax)

        for i, x in enumerate(X_scaled):
            w = som.winner(x)
            label = str(df.iloc[i]["Nama"])[:5] if pd.notna(df.iloc[i]["Nama"]) else f"M{i}"
            ax.text(w[0], w[1], label, color='blue', fontsize=8, ha='center', va='center')

        ax.scatter(winner[0], winner[1], s=300, c='red', edgecolors='black', marker='o')
        ax.set_title("📌 Peta SOM dengan Posisi Mahasiswa Baru")
        ax.grid(True)
        st.pyplot(fig)
    
    with col4:
        # --- Donut Jumlah Mahasiswa per Klaster ---
        st.subheader("📊 Distribusi Mahasiswa per Klaster (Donut)")

        all_winners = [som.winner(x) for x in X_scaled]
        counts = Counter(all_winners)
        labels = [f"{k}" for k in counts.keys()]
        values = [v for v in counts.values()]

        fig2, ax2 = plt.subplots()
        ax2.pie(values, labels=labels, wedgeprops=dict(width=0.4), startangle=90, autopct='%1.1f%%')
        ax2.set_title("Distribusi Mahasiswa di Neuron Output")
        st.pyplot(fig2)

    # --- Menambahkan Kolom Klaster dan Menampilkan Tabel ---
    df['Klaster'] = [str(som.winner(x)) for x in X_scaled]
    df_new = df[["Nama", "Klaster"]]
    st.subheader("📊 Tabel Nama dan Klaster Mahasiswa")
    st.dataframe(df_new)


