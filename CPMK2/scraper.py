import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_comments(url, product_name):
    """
    Fungsi scraping komentar Shopee (simulasi, contoh struktur umum)
    """
    print(f"[INFO] Mengambil data komentar dari {product_name}...")

    # ⚠️ Contoh scraping dummy (karena Shopee dinamis dan perlu API/selenium untuk real scraping)
    # Kamu bisa ganti bagian ini dengan hasil export CSV Shopee, atau integrasi Selenium nanti.
    comments = [
        "Produk bagus banget, sesuai deskripsi!",
        "Pengiriman cepat, kualitas oke",
        "Barang rusak pas datang, kecewa",
        "Harga murah tapi kualitas lumayan",
        "Packing rapi dan penjual ramah"
    ]

    df = pd.DataFrame(comments, columns=["comment"])
    df["product"] = product_name
    return df
