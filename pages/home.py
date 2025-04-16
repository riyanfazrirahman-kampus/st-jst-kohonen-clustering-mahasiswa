import streamlit as st
import numpy as np
import pandas as pd
from pages.manual_hitung import tampilkan_perhitungan_manual

st.title("🧠 Self Organizing Map (SOM) Clustering Mahasiswa")
st.write("Upload data penilaian mahasiswa (format .csv) untuk dilakukan clustering dengan SOM.")

st.session_state["html_som_manual"] = None  


# Upload file
uploaded_file = st.file_uploader("📁 Upload file CSV", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("📄 Data Asli")
    st.dataframe(df, use_container_width=True)

    all_columns = df.columns.tolist()

    st.sidebar.header("🧩 Pilih Kolom Fitur")
    fitur_dipilih = st.sidebar.multiselect(
        "Pilih kolom numerik yang mau digunakan sebagai fitur (X1, X2, dst):",
        options=all_columns,
        default=[col for col in all_columns if col.startswith('X')]
    )

    if not fitur_dipilih:
        st.warning("Pilih setidaknya satu kolom sebagai fitur.")
        st.stop()

    # Pisahkan fitur & data lainnya
    data_fitur = df[fitur_dipilih].to_numpy()
    data_lain = df.drop(columns=fitur_dipilih)  # kolom non-fitur (NIM, Nama, dsb)

    # Normalisasi fitur
    max_vals = data_fitur.max(axis=0)
    normalized_data = data_fitur / max_vals

    st.subheader("📐 Data Setelah Normalisasi")
    st.dataframe(pd.DataFrame(normalized_data, columns=fitur_dipilih), use_container_width=True)

    # Parameter
    st.sidebar.header("🔧 Parameter SOM")
    num_neurons = st.sidebar.slider("Jumlah Neuron (Cluster)", min_value=2, max_value=10, value=2)
    learning_rate = st.sidebar.slider("Learning Rate", min_value=0.1, max_value=1.0, step=0.1, value=0.6)
    num_epochs = st.sidebar.slider("Jumlah Epoch", min_value=1, max_value=20, value=1)

    # Bobot awal (static demo)
    weights = np.random.rand(num_neurons, normalized_data.shape[1])
    # weights = [
    #     [0.2, 0.6, 0.5, 0.9],
    #     [0.8, 0.4, 0.7, 0.3],
    # ]

    if st.button("🚀 Jalankan SOM"):
        st.write("### 🧠 Bobot Awal")
        weights_df = pd.DataFrame(weights, columns=fitur_dipilih)
        st.dataframe(weights_df, use_container_width=True)

        def euclidean_distance(v1, v2):
            return np.sqrt(np.sum((v1 - v2) ** 2))

        # Training SOM
        for epoch in range(num_epochs):
            for x in normalized_data:
                distances = np.array([euclidean_distance(x, w) for w in weights])
                winner_index = np.argmin(distances)
                weights[winner_index] += learning_rate * (x - weights[winner_index])

        st.subheader("📊 Bobot Akhir Tiap Neuron")
        bobot_df = pd.DataFrame(weights, columns=fitur_dipilih)
        st.dataframe(bobot_df, use_container_width=True)

        # Penentuan cluster akhir
        clusters = []
        for x in normalized_data:
            distances = np.array([euclidean_distance(x, w) for w in weights])
            winner_index = np.argmin(distances)
            clusters.append(winner_index)

        # Gabungkan hasil cluster ke data asli
        hasil_akhir = data_lain.copy()
        for col, nilai in zip(fitur_dipilih, data_fitur.T):
            hasil_akhir[col] = nilai
        hasil_akhir['Cluster'] = clusters

        st.subheader("📌 Hasil Clustering")
        st.dataframe(hasil_akhir, use_container_width=True)

        # Download hasil
        csv = hasil_akhir.to_csv(index=False).encode('utf-8')
        st.download_button("⬇️ Download Hasil Clustering", csv, "hasil_clustering.csv", "text/csv")
    
    set_fitur_dipilih = fitur_dipilih.copy()

    # Tampilkan langkah manual perhitungan SOM
    if st.button("Tampilkan Langkah Manual Perhitungan SOM"):
        tampilkan_perhitungan_manual(normalized_data, weights, learning_rate, num_epochs, set_fitur_dipilih, data_lain)
   
else:
    st.info("Silakan upload file CSV terlebih dahulu.")
