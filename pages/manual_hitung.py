import streamlit as st
import pandas as pd
import numpy as np

def tampilkan_perhitungan_manual(data, initial_weights, initial_lr, num_epochs, fitur_dipilih, data_asli):
    
    st.subheader("🧮 Langkah Manual SOM dengan Epoch")

    weights = np.array(initial_weights)  # Copy bobot awal agar tidak overwrite bobot utama
    st.write("### 🧠 Bobot Awal")
    weights_df = pd.DataFrame(weights, columns=fitur_dipilih)
    st.dataframe(weights_df, use_container_width=True)
    
    for epoch in range(num_epochs):
        st.markdown(f"## 🕓 Epoch {epoch+1} / {num_epochs}")
        lr = initial_lr * (1 - (epoch / num_epochs))
        st.info(f"Learning Rate (turun linier): {np.round(lr, 4)}")

        for idx, x in enumerate(data):
            st.markdown(f"### 🔹 Data ke-{idx+1}")
            st.write("Input vektor:")
            st.code(x)

            st.markdown("#### 🔢 Bobot Saat Ini:")
            for i, w in enumerate(weights):
                st.write(f"Neuron {i}: {np.round(w, 4)}")

            st.markdown("#### 📏 Hitung Jarak Euclidean ke Semua Neuron:")
            distances = []
            for i, w in enumerate(weights):
                diff = x - w
                dist = np.sqrt(np.sum(diff**2))
                distances.append(dist)

                st.write(f"Neuron {i}: Jarak = √Σ(x - w)² = {np.round(dist, 4)}")

            winner_index = np.argmin(distances)
            st.success(f"🏆 Neuron Pemenang: Neuron {winner_index} (Jarak: {np.round(distances[winner_index], 4)})")

            old_weight = weights[winner_index]
            delta = lr * (x - old_weight)
            new_weight = old_weight + delta

            st.markdown("#### 🔧 Update Bobot Neuron Pemenang:")
            for i in range(len(x)):
                st.write(f"""
                w{i}_baru = {np.round(old_weight[i], 4)} + {np.round(lr, 4)} × ({np.round(x[i], 4)} - {np.round(old_weight[i], 4)})
                         = {np.round(new_weight[i], 4)}
                """)

            weights[winner_index] = new_weight

            st.markdown("#### ✅ Bobot Baru:")
            for i, w in enumerate(weights):
                st.write(f"Neuron {i}: {np.round(w, 4)}")

            st.markdown("---")

    st.success("✅ Selesai menghitung seluruh epoch dan data.")
    st.markdown("### 📊 Bobot Akhir Tiap Neuron")
    bobot_df = pd.DataFrame(weights, columns=fitur_dipilih)
    st.dataframe(bobot_df, use_container_width=True)

        # Penentuan cluster akhir setelah pelatihan selesai
    st.markdown("## 📌 Hasil Clustering")

    clusters = []
    for x in data:
        distances = np.array([np.sqrt(np.sum((x - w) ** 2)) for w in weights])
        winner_index = np.argmin(distances)
        clusters.append(winner_index)

    # Buat dataframe hasil akhir
    hasil_akhir = data_asli.copy()
    hasil_akhir['Cluster'] = clusters

    st.dataframe(hasil_akhir, use_container_width=True)


