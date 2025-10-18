import os
from scraper import scrape_comments
from preprocess import preprocess_dataframe
from wordcloud_generator import generate_wordcloud
import pandas as pd

# Buat folder hasil_model kalau belum ada
os.makedirs("hasil_model", exist_ok=True)

def main():
    print("=== 📦 MODEL PEMBANDING PRODUK SHOPEE ===\n")

    # Input dua link produk (dummy dulu)
    link_A = input("Masukkan link produk A Shopee: ")
    link_B = input("Masukkan link produk B Shopee: ")

    # Scraping data komentar
    data_A = scrape_comments(link_A, "Produk A")
    data_B = scrape_comments(link_B, "Produk B")

    # Gabungkan dan preprocessing
    print("\n[INFO] Melakukan preprocessing teks...")
    data_A = preprocess_dataframe(data_A)
    data_B = preprocess_dataframe(data_B)

    # Tampilkan word cloud
    print("\n[INFO] Menampilkan Word Cloud Produk A...")
    generate_wordcloud(data_A, "Produk A")

    print("\n[INFO] Menampilkan Word Cloud Produk B...")
    generate_wordcloud(data_B, "Produk B")

    # Simpan hasil scraping mentah
    data_A.to_csv("hasil_model/scraping_produk_A.csv", index=False)
    data_B.to_csv("hasil_model/scraping_produk_B.csv", index=False)
    print("[✅] Hasil scraping disimpan di folder 'hasil_model'.")

    # Simpan hasil preprocessing (casefolding, tokenizing, dst)
    data_A.to_csv("hasil_model/preprocessing_produk_A.csv", index=False)
    data_B.to_csv("hasil_model/preprocessing_produk_B.csv", index=False)
    print("[✅] Hasil preprocessing juga disimpan di folder 'hasil_model'.")

    # Gabungkan untuk perbandingan keseluruhan
    combined = pd.concat([data_A, data_B])
    combined.to_csv("hasil_model/hasil_perbandingan.csv", index=False)
    print("\n✅ Semua hasil analisis telah disimpan dalam folder 'hasil_model'")


if __name__ == "__main__":
    main()
