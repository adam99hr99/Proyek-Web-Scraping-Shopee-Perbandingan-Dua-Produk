🛒 Proyek Web Scraping Shopee – Perbandingan Dua Produk
📘 Deskripsi
Proyek ini merupakan tugas scraping data komentar dari dua produk di Shopee menggunakan Python.
Tujuannya adalah untuk menganalisis dan membandingkan sentimen atau kata-kata yang paling sering muncul dari ulasan pengguna kedua produk tersebut.
Hasil scraping kemudian diolah melalui tahapan case folding (pembersihan teks), serta divisualisasikan dalam bentuk word cloud untuk setiap produk.
Proyek ini dijalankan secara lokal menggunakan Visual Studio Code (VSC).

⚙️ Teknologi yang Digunakan

🐍 Python 3.x
📦 Library utama:
requests – mengambil data dari halaman Shopee
BeautifulSoup – parsing HTML dari hasil scraping
re – membersihkan teks menggunakan Regular Expression
wordcloud – membuat visualisasi kata yang sering muncul
matplotlib – menampilkan hasil visualisasi
os – mengatur path penyimpanan hasil

🧠 Tahapan Proyek
1️⃣ Scraping Data

Mengambil komentar atau ulasan dari dua produk berbeda di Shopee dengan URL masing-masing produk.

url_produk1 = "https://shopee.co.id/produk_1"
url_produk2 = "https://shopee.co.id/produk_2"

2️⃣ Case Folding

Membersihkan hasil ulasan dengan mengubah teks menjadi huruf kecil, menghapus angka, tanda baca, dan simbol.
def casefolding(teks):
    teks = teks.lower()
    teks = re.sub(r'[^a-z\s]', '', teks)
    return teks

3️⃣ Visualisasi WordCloud

Menampilkan kata-kata yang paling sering muncul dari hasil ulasan pengguna untuk kedua produk.
from wordcloud import WordCloud
import matplotlib.pyplot as plt


📊 Hasil Analisis

Dari hasil word cloud, kita dapat melihat kata yang dominan pada masing-masing produk.
Misalnya:

Produk A: “bagus”, “cepat”, “murah”
Produk B: “lama”, “rusak”, “tidak sesuai”
Hal ini bisa membantu dalam menilai kualitas produk berdasarkan opini pelanggan.

💾 Struktur Folder

Scrappingdata/
│
├── main.py
├── Scraping_Result.csv
├── Casefolding_Result.csv
├── Wordcloud_Produk1.png
├── Wordcloud_Produk2.png
└── README.md

🚀 Cara Menjalankan

Buka proyek di Visual Studio Code
Pastikan Python sudah terinstall
Jalankan perintah berikut di terminal:

python main.py

Tunggu proses scraping dan case folding selesai
Lihat hasil pada folder Scrappingdata

🧑‍💻 Pengembang

Nama: Adam Herlambang
Email: herlambangadam9@gmail.com

Bahasa Pemrograman: Python
Dibuat: Oktober 2025
