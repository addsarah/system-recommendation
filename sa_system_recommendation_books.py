# -*- coding: utf-8 -*-
"""SA - System Recommendation - Books.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1xSRa1B1mNUvdx9zJAZoh66Ev0hPjSODK

# Proyek Akhir Machine Learning Expert Dicoding: System Recommendation - Books

- **Nama:** Sarah Adibah
- **Email:** sarahadibah06@gmail.com
- **ID Dicoding:** [addsarah](https://www.dicoding.com/users/addsarah/academies)

**Kriteria Submission:**
- Project merupakan hasil pekerjaan sendiri.
- Project belum pernah digunakan untuk submission kelas Machine Learning di Dicoding dan belum pernah dipublikasikan di platform manapun.
- Dataset yang dipakai bebas, asal bisa digunakan untuk membuat sistem rekomendasi.
- Memberikan dokumentasi menggunakan text cell pada notebook (.ipynb) untuk menjelaskan setiap tahapan proyek.
- Menentukan solusi permasalahan dengan memilih pendekatan berikut:
  - Content-based Filtering
  - Collaborative Filtering
- Membuat draf laporan proyek machine learning yang menjelaskan alur proyek Anda mulai dari project overview, business understanding, data understanding, data preparation, modeling, hingga tahap evaluasi.


**Saran Submission**

Menerapkan Rubrik/Kriteria Penilaian (Tambahan) untuk mendapatkan skala penilaian (bintang) yang lebih tinggi.


**Submission yang Tidak Sesuai Kriteria:**
- Tidak melampirkan submission dengan bentuk .zip.
- Tidak melampirkan laporan dengan format markdown (.md) atau text (.txt).
- Tidak melampirkan proyek machine learning (.py atau .ipynb).
- File Jupyter Notebook belum dijalankan.
- Tidak menerapkan seluruh rubrik penilaian wajib (rubrik tidak lengkap).
- File submission tidak bisa di-load oleh tim reviewer.

**Tips**

Anda dapat memilih beberapa topik rekomendasi (namun tidak terbatas pada daftar) berikut:
- Rekomendasi film
- Rekomendasi buku
- Rekomendasi musik
- Rekomendasi video
- Rekomendasi produk
- Rekomendasi artikel
- Rekomendasi berita
- dsb.

**Ketentuan Berkas Submission**

Mengirimkan Submission dalam bentuk .zip yang terdiri dari 3 (tiga) berkas, yaitu:  
- File Jupyter Notebook (.ipynb). Pastikan file Jupyter Notebook sudah dijalankan, ya.
- File Python (.py)
- File laporan dalam bentuk Markdown (.md) atau Text (.txt)

# Dataset
[Books Dataset](https://www.kaggle.com/datasets/saurabhbagchi/books-dataset)

# **1. Library Import**

- *Library* [`os`](https://docs.python.org/3/library/os.html) digunakan untuk menjalankan *function* yang berhubungan dengan *operating system*. `os.environ` berfungsi untuk membaca *username* dan *key* dari [Kaggle](https://kaggle.com).

- *Library* [`numpy`](https://numpy.org) digunakan untuk melakukan pemrosesan matematis seperti operasi himpunan, *array*, matriks multidimensi, dan vektorisasi.

- *Library* [`pandas`](https://pandas.pydata.org) digunakan untuk memproses, menganalisis, dan memanipulasi data dalam format yang terstruktur.

- *Library* [`tensorflow`](https://www.tensorflow.org) digunakan untuk membangun dan melatih model *machine learning* serta *neural networks*.

- *Library* [`sklearn`](https://scikit-learn.org) digunakan dalam pemrosesan *machine learning* dan *data analysis*, seperti klasifikasi, regresi, dan klastering.

- *Library* [`seaborn`](https://seaborn.pydata.org) digunakan untuk membuat visualisasi data yang informatif dan menarik, serta berbasis pada `matplotlib`.

- *Library* [`matplotlib`](https://matplotlib.org) digunakan untuk melakukan visualisasi data menggunakan berbagai jenis *plotting* seperti line chart, bar chart, dan histogram.
"""

import os
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.losses import BinaryCrossentropy
from tensorflow.keras.metrics import RootMeanSquaredError

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

import seaborn as sns
import matplotlib.pyplot as plt

"""# **2. Data Loading**

## 2.1 Environment and Kaggle Credential

Menyiapkan *environment* pada `operating system` [Colab](https://colab.research.google.com 'Google Colaboratory') dengan menetapkan variabel `KAGGLE_USERNAME` dan `KAGGLE_KEY` untuk koneksi ke platform [Kaggle](https://kaggle.com 'Kaggle') melalui [Kaggle's Beta API](https://www.kaggle.com/docs/api 'Kaggle Public API Documentation') Token.
"""

# Username dan key Kaggle API
os.environ['KAGGLE_USERNAME'] = 'addsarah'
os.environ['KAGGLE_KEY']      = 'eff5b83c0a0943cd628b2c66f0878a19'

"""## 2.2 Dataset Download

Mengambil (*download*) *dataset* dari platform Kaggle dalam bentuk berkas yang masih terkompresi (*compressed file*) dengan nama `book-recommender-system.zip`. Berkas tersebut berasal dari *dataset* [Books Dataset](https://www.kaggle.com/datasets/saurabhbagchi/books-dataset) dan akan digunakan sebagai sumber data utama dalam proyek ini.
"""

# Download dataset dari Kaggle
!kaggle datasets download -d saurabhbagchi/books-dataset

"""Melakukan proses ekstraksi (*extract*) terhadap berkas *dataset* yang masih berada dalam format terkompresi (*compressed*) menggunakan perintah `!unzip`. Setelah diekstrak, akan dihasilkan tiga (3) berkas *dataset* dalam format `.csv` ([comma-separated values](https://docs.python.org/id/3.10/library/csv.html)), yaitu `BX-Books.csv`, `BX-Book-Ratings.csv`, dan `BX-Users.csv`."""

!unzip /content/books-dataset.zip

"""# **3. Data Understanding**

## 3.1 Jumlah Data Masing-masing Atribut dari *Dataset*

Melakukan pembacaan masing-masing berkas *dataset*, yaitu `books.csv`, `ratings.csv`, dan `users.csv` ke dalam variabel `df_bo`, `df_ra`, dan `df_us`. Proses ini menggunakan *library* [Pandas](https://pandas.pydata.org 'Python Data Analysis Library') untuk mengonversi berkas berformat CSV menjadi struktur data *dataframe*.
"""

df_bo = pd.read_csv('books_data/books.csv', encoding='latin-1', on_bad_lines='skip', delimiter=';')
df_ra = pd.read_csv('books_data/ratings.csv', encoding='latin-1', on_bad_lines='skip', delimiter=';')
df_us = pd.read_csv('books_data/users.csv', encoding='latin-1', on_bad_lines='skip', delimiter=';')

"""Melakukan eksplorasi terhadap jumlah nilai unik dari setiap atribut dalam masing-masing *dataframe* menggunakan fungsi `.unique()`."""

print(f'Jumlah data ISBN     : {len(df_bo["ISBN"].unique())}')
print(f'Jumlah data Judul    : {len(df_bo["Book-Title"].unique())}')
print(f'Jumlah data Penulis  : {len(df_bo["Book-Author"].unique())}')
print(f'Jumlah data Penerbit : {len(df_bo["Publisher"].unique())}')
print(f'Jumlah data Tahun    : {len(df_bo["Year-Of-Publication"].unique())}')
print(f'=====' * 9)
print(f'Jumlah data Pembaca              : {len(df_ra["User-ID"].unique())}')
print(f'Jumlah data Buku                 : {len(df_ra["ISBN"].unique())}')
print(f'Jumlah data Rating yang diterima : {len(df_ra)}')
print(f'=====' * 9)
print(f'Jumlah data User : {len(df_us)}')

"""## 3.2 Univariate Exploratory Data Analysis (EDA)

*Explanatory Data Analysis* (EDA) merupakan tahap awal eksplorasi data untuk memahami karakteristik data, mengidentifikasi pola, *anomaly*, dan memeriksa asumsi melalui pendekatan statistik dan visualisasi grafik.

### 3.2.1 Dataset Books

*Exploratory Data Analysis* (EDA) untuk *dataframe* `Books`.

Menampilkan isi Dataframe `Books`
"""

df_bo

"""Menampilkan ringkasan struktur Dataframe `Books`"""

df_bo.info()

"""### 3.2.2 Dataset Rating

*Exploratory Data Analysis* (EDA) untuk *dataframe* `Ratings`.

Menampilkan isi Dataframe `Ratings`
"""

df_ra

"""Menampilkan ringkasan struktur Dataframe `Ratings`"""

df_ra.info()

"""Menampilkan ringkasan statistik untuk *dataframe* `Ratings` guna memahami persebaran data, termasuk jumlah (`count`), rata-rata (`mean`), simpangan baku (`std`), nilai minimum (`min`), maksimum (`max`), serta kuartil pertama/Q1 (`25%`), median/Q2 (`50%`), dan kuartil ketiga/Q3 (`75%`)."""

df_ra.describe()

"""Menampilkan deskripsi statistik untuk *dataframe* `Ratings` pada atribut `Book-Rating` guna memperoleh gambaran statistik, seperti nilai rata-rata (`mean`), simpangan baku (`std`), nilai minimum (`min`), maksimum (`max`), serta nilai kuartil pertama/Q1 (`25%`), median/Q2 (`50%`), dan kuartil ketiga/Q3 (`75%`) dari *rating* yang diberikan pengguna terhadap buku yang sudah dibaca"""

df_ra['Book-Rating'].describe().apply(lambda x: '%.f' % x)

"""Membuat visualisasi berupa histogram untuk melihat distribusi frekuensi *rating* buku, dengan rentang nilai mulai dari 0 hingga 10, yang menunjukkan seberapa sering masing-masing *rating* diberikan."""

df_ra['Book-Rating'].value_counts().sort_index().plot(
    kind    = 'barh',
    color   = ['k', 'gray', 'pink', 'm', 'c', 'b', 'g', 'lightgreen', 'yellow', 'orange', 'r'],
    title   = 'Jumlah Rating Buku',
    xlabel  = 'Rating',
    ylabel  = 'Jumlah',
    figsize = (14, 5),
    xticks  = (np.arange(0, 720000, 50000))
).grid(linestyle='-.', linewidth=0.5)

"""Berdasarkan hasil visualisasi histogram pada bagian "Jumlah Rating Buku", dapat diamati bahwa *rating* 0 merupakan yang paling sering muncul, dengan jumlah melebihi 700.000. Karena nilai ini berpotensi menyebabkan bias dalam analisis, maka *rating* bernilai 0 dapat dihapus pada tahap *data preparation* agar hasil model lebih akurat.

### 3.2.3 Dataset User

*Exploratory Data Analysis* (EDA) untuk *dataframe* `Users`.

Menampilkan isi Dataframe `Users`
"""

df_us

"""Menampilkan ringkasan struktur Dataframe `Users`"""

df_us.info()

"""Menampilkan ringkasan statistik untuk *dataframe* `Users` guna memahami persebaran data, termasuk jumlah (`count`), rata-rata (`mean`), simpangan baku (`std`), nilai minimum (`min`), maksimum (`max`), serta kuartil pertama/Q1 (`25%`), median/Q2 (`50%`), dan kuartil ketiga/Q3 (`75%`)."""

df_us.describe()

"""# **4. Data Preparation**

Tahap persiapan data atau *data preparation* adalah proses penting sebelum melakukan pengembangan model *machine learning*.

Pada bagian 4.1 — 4.3 data mentah (*raw data*) dibersihkan dan disiapkan menjadi *clean data* agar lebih siap digunakan dalam proses selanjutnya. Pada proyek sistem rekomendasi ini, proses *preparation* mencakup penyesuaian nama kolom dalam setiap *dataframe*, serta penggabungan data berdasarkan `ISBN` dan `user_id` untuk memperoleh informasi menyeluruh.

## 4.1 Mengubah Nama Kolom/Atribut

Perubahan nama atribut dalam masing-masing *dataframe* menggunakan fungsi `.rename()` bertujuan untuk menyederhanakan proses pemanggilan data pada tahap analisis dan pemodelan berikutnya.

### 4.1.1 Books

Mengganti nama columns pada Dataframe `Books`
"""

df_bo.rename(columns={
    'ISBN'                : 'isbn',
    'Book-Title'          : 'book_title',
    'Book-Author'         : 'book_author',
    'Year-Of-Publication' : 'year_pub',
    'Publisher'           : 'publisher',
    'Image-URL-S'         : 'image_url_s',
    'Image-URL-M'         : 'image_url_m',
    'Image-URL-L'         : 'image_url_l'
}, inplace=True)

df_bo.head()

"""### 4.1.2 Ratings

Mengganti nama columns pada Dataframe `Ratings`
"""

df_ra.rename(columns={
    'User-ID'     : 'user_id',
    'ISBN'        : 'isbn',
    'Book-Rating' : 'book_rating'
}, inplace=True)

df_ra.head()

"""### 4.1.3 Users

Mengganti nama columns pada Dataframe `Users`
"""

df_us.rename(columns={
    'User-ID'  : 'user_id',
    'Location' : 'location',
    'Age'      : 'age'
}, inplace=True)

df_us.head()

"""## 4.2 Menggabungkan Data ISBN

Penggabungan data `Books` berdasarkan ISBN dilakukan dengan menggunakan fungsi `.concatenate` dari *library* [`numpy`](https://numpy.org), untuk mengintegrasikan atribut ISBN dari *dataframe* `df_bo` (buku) dan `df_ra` (rating), sehingga informasi buku dan *rating* dapat dianalisis secara bersamaan.
"""

ISBNAll = np.concatenate((
    df_bo.isbn.unique(),
    df_ra.isbn.unique()
))

ISBNAll = np.sort(np.unique(ISBNAll))

print(f'Jumlah Buku berdasarkan ISBN : {len(ISBNAll)}')

"""## 4.3 Menggabungkan Data *User*

Proses penggabungan data berdasarkan `user_id` juga dilakukan dengan fungsi `.concatenate` dari *library* [`numpy`](https://numpy.org), dengan menggabungkan informasi pengguna dari *dataframe* `df_us` dan *rating* dari `df_ra`, untuk mengetahui interaksi pengguna terhadap buku.
"""

UserAll = np.concatenate((
    df_ra.user_id.unique(),
    df_us.user_id.unique()
))

UserAll = np.sort(np.unique(UserAll))

print(f'Jumlah User : {len(UserAll)}')

"""Pada tahap 4.4 — 4.9, data diolah dan ditransformasi agar sesuai dengan kebutuhan proses pemodelan. Dalam proyek ini, tahap tersebut mencakup penanganan data yang hilang (*missing value)*, pengecekan data duplikat, serta penggabungan data dari dataset buku dan *rating*.

## 4.4 Pengecekan Missing Value

Proses identifikasi data yang missing pada sebuah dataframe dapat dilakukan dengan menggunakan metode `.isnull().sum()`. Dengan cara ini, kita dapat mengetahui jumlah total data yang memiliki nilai kosong atau hilang.

### 4.4.1 Books

Memeriksa total data yang memiliki nilai kosong atau hilang pada Dataframe `Books`
"""

books = df_bo
books.isnull().sum()

"""Hasil pemeriksaan deskripsi diatas terhadap *dataframe* `books` menunjukkan bahwa terdapat nilai kosong atau *null* pada beberapa atribut, yaitu `book_author` sebanyak 2 data, `publisher` sebanyak 2 data, dan `image_url_l` sebanyak 3 data.

Nilai-nilai kosong atau *null* tersebut dapat dibersihkan dari dataframe dengan menerapkan fungsi `.dropna()`. Setelah proses ini dilakukan, pengecekan ulang akan menunjukkan bahwa tidak ada lagi nilai kosong di dalam dataframe tersebut.
"""

books = books.dropna()
books.isnull().sum()

"""### 4.4.2 Ratings

Memeriksa total data yang memiliki nilai kosong atau hilang pada Dataframe `Ratings`
"""

ratings = df_ra
ratings.isnull().sum()

"""Sementara itu, berdaasarkan deskripsi diatas terhadap *dataframe* `ratings` memperlihatkan bahwa semua kolom tidak memiliki nilai kosong atau *null*.

Namun, pada tahap *Univariate Exploratory Data Analysis* (EDA) sebelumnya, terlihat dari histogram "Jumlah Rating Buku" bahwa sebagian besar *rating* berada di nilai 0, yang mencapai lebih dari 700.000 data. Nilai *rating* 0 ini berpotensi menimbulkan bias dalam analisis, sehingga perlu dihapus dari *dataframe*.

Menghitung Total `Ratings` 0
"""

print(f'Total Rating 0 : {ratings.book_rating.eq(0).sum()}')

ratings = ratings[df_ra.book_rating > 0]

"""Setelah dihitung, jumlah data dengan *rating* 0 mencapai 716.109 baris. Oleh karena itu, hanya *rating* di atas 0 yang akan disertakan dalam analisis, yaitu rating dari 1 hingga 10."""

ratings.book_rating.value_counts().sort_index().plot(
    kind    = 'barh',
    color   = ['gray', 'pink', 'm', 'c', 'b', 'g', 'lightgreen', 'yellow', 'orange', 'r'],
    title   = 'Jumlah Rating Buku',
    xlabel  = 'Rating',
    ylabel  = 'Jumlah',
    figsize = (14, 5),
    xticks  = (np.arange(0, 110000, 7500))
).grid(linestyle='-.', linewidth=0.5)

"""Berdasarkan hasil visualisasi grafik histogram di atas, distribusi data dalam histogram menjadi lebih teratur, terutama pada rentang *rating* 1 hingga 4.

### 4.4.3 Users

Memeriksa total data yang memiliki nilai kosong atau hilang pada Dataframe `Users`
"""

users = df_us
users.isnull().sum()

"""Berdasarkan deskripsi di atas, dapat dilihat bahwa pada *dataframe* `users` terdapat atribut yang memiliki nilai kosong atau *null*, yaitu pada atribut `age` sebanyak 110.762 data.

Menampilkan isi Dataframe `Users`
"""

df_us

"""Berdasarkan tabel *dataframe* `Users` di atas, dapat dilihat bahwa terdapat nilai `null` atau `NaN` (*Not a Number*) pada kolom/atribut `Age`. Sehingga perlu dilakukan pemrosesan lebih lanjut dengan  mengganti nilai kosong atau string tidak valid seperti `'NaN'`, `'nan'`, `' '`, dan `'`' menjadi nilai `np.nan`. Setelah itu, kolom `Age` dikonversi ke dalam tipe numerik agar dapat dianalisis lebih lanjut, dan baris-baris yang mengandung nilai NaN dihapus menggunakan `dropna()` untuk memastikan kualitas dan konsistensi data."""

df_us.replace(['NaN', 'nan', ' ', ''], np.nan, inplace=True)
df_us['age'] = pd.to_numeric(df_us['age'])
df_us.dropna(inplace=True)

"""Menampilkan isi Dataframe `Users` guna memeriksa apakah nilai `null` atau `NaN` (*Not a Number*) pada kolom/atribut `Age` sudah terhapus atau belum"""

df_us

"""Berdasarkan tabel *dataframe* `Users` di atas, dapat dilihat bahwa terdapat nilai `null` atau `NaN` (*Not a Number*) pada kolom/atribut `Age` sudah dihapus.

Memeriksa kembali total data yang memiliki nilai kosong atau hilang pada Dataframe `Users`
"""

users = df_us
users.isnull().sum()

"""Pemeriksaan terhadap *dataframe* `users` diatas menunjukkan bahwa tidak ada nilai kosong atau *null* yang ditemukan di seluruh kolomnya.

Menampilkan histogram dari kolom age pada Dataframe `users`
"""

users.age.hist(bins=100)

"""Berdasarkan hasil visualisasi grafik histogram umur *user* di atas, dapat dilihat bahwa mayoritas pengguna berada pada rentang usia 20—40 tahun, dengan puncak distribusi antara 30—35 tahun.

Terdapat pula sebagian kecil pengguna dengan usia di bawah 10 tahun dan di atas 80 tahun, namun jumlahnya jauh lebih sedikit dibandingkan kelompok usia produktif. Hal ini menunjukkan bahwa sistem rekomendasi buku kemungkinan besar akan lebih relevan jika disesuaikan dengan preferensi kelompok usia 20—40 tahun.

## 4.5 Pengecekan Data Duplikat

Untuk mendeteksi apakah terdapat data duplikat di dalam *dataframe*, dapat menggunakan fungsi `.duplicated().sum()`.
"""

print(f'Jumlah data books  yang duplikat: {books.duplicated().sum()}')
print(f'Jumlah data rating yang duplikat: {ratings.duplicated().sum()}')
print(f'Jumlah data users  yang duplikat: {users.duplicated().sum()}')

"""Hasilnya, tidak ditemukan adanya data duplikat pada *dataframe* `books`, `ratings`, maupun `users`.

## 4.6 Menggabungkan Data Buku dan Rating

Menggabungkan dua Datadrame yaitu `ratings` dan `books` berdasarkan kolom yang sama, yaitu `'isbn'`
"""

books_ratings = pd.merge(ratings, books, on=['isbn'])
books_ratings

"""## 4.7 TF-IDF Vectorizer

*Term Frequency Inverse Document Frequency Vectorizer* ([TF-IDF Vectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html 'TfidfVectorizer - scikit-learn Documentation')) *Algorithm* digunakan untuk mengubah teks mentah menjadi representasi numerik yang memiliki makna tertentu dalam bentuk matriks, yang dapat diproses dan digunakan oleh model *machine learning*.

Mengubah data teks pada kolom `book_author` menjadi representasi numerik menggunakan teknik TF-IDF (Term Frequency-Inverse Document Frequency)
"""

tfidf = TfidfVectorizer()
tfidf.fit(books.book_author)
# tfidf.get_feature_names_out()

"""Transformasi data pada atribut `book_author` ke dalam matriks dilakukan menggunakan fungsi `.fit_transform()`."""

tfidf_matrix = tfidf.fit_transform(books.book_author)
tfidf_matrix.shape

"""Hasil dari transformasi ini adalah matriks dengan ukuran 10.000 baris buku dan 5.575 kolom yang mewakili *author*.

Karena hasil dari vectorizer masih berupa vektor *(vectorizer)*, maka perlu dikonversi ke bentuk matriks dengan fungsi `.todense()`.
"""

tfidf_matrix.todense()

"""Untuk menampilkan hasil transformasi TF-IDF ke dalam format yang lebih mudah dibaca, matriks tersebut dikonversi menjadi *dataframe* dengan kolom berupa nama *author* dan baris *(index)* adalah judul buku."""

pd.DataFrame(
    tfidf_matrix.todense(),
    columns = tfidf.get_feature_names_out(),
    index   = books.book_title
).sample(20, axis=1).sample(10, axis=0)

"""## 4.8 Encoding

Melakukan penyandian (*encoding*) fitur `user_id` ke dalam indeks integer.
"""

user_ids = ratings.user_id.unique().tolist()
user_to_user_encoded = {x: i for i, x in enumerate(user_ids)}
user_encoded_to_user = {i: x for i, x in enumerate(user_ids)}

"""Menampilkan hasil mapping antara `user IDs` dengan ID yang sudah di-encode"""

print(user_ids)
print(user_to_user_encoded)
print(user_encoded_to_user)

"""Langkah pertama adalah melakukan *encoding* terhadap fitur `isbn` ke dalam indeks integer."""

book_ids = ratings.isbn.unique().tolist()
book_to_book_encoded = {x: i for i, x in enumerate(book_ids)}
book_encoded_to_book = {i: x for i, x in enumerate(book_ids)}

"""Menampilkan hasil mapping antara `Boook IDs` dengan ID yang sudah di-encode"""

print(book_ids)
print(book_to_book_encoded)
print(book_encoded_to_book)

"""`user_id` dan `isbn` kemudian dipetakan ke dataframe masing-masing.


"""

ratings['user'] = ratings.user_id.map(user_to_user_encoded)
ratings['book'] = ratings.isbn.map(book_to_book_encoded)

"""Pemeriksaan selanjutnya dilakukan terhadap jumlah *user*, jumlah buku, serta nilai *rating* minimum dan maksimum."""

num_users = len(user_encoded_to_user)
num_books = len(book_encoded_to_book)
print(num_users)
print(num_books)

min_ratings = min(ratings.book_rating)
max_ratings = max(ratings.book_rating)
print(f'Number of User: {num_users}, Number of Books: {num_books}, Min Rating: {min_ratings}, Max Rating: {max_ratings}')

"""## 4.9 Training Data and Validation Data Split

Melakukan pengecekan terhadap *dataframe* `ratings` setelah atribut tambahan `user` dan `book` ditambahkan ke dalam dataframe ratings, data kemudian diacak menggunakan fungsi [`.sample(frac=1)`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sample.html 'pandas.DataFrame.sample - Pandas Documentation').
"""

ratings = ratings.sample(frac=1, random_state=412)
ratings

"""Dataset kemudian dibagi menjadi data latih dan data uji dengan rasio 80:20, di mana 80% digunakan untuk pelatihan model (*training data*) dan 20% untuk validasi (*validation data*)."""

x = ratings[['user', 'book']].values
y = ratings['book_rating'].apply(lambda x: (x-min_ratings) / (max_ratings-min_ratings)).values

train_indices = int(0.8 * ratings.shape[0])

xTrain, xVal, yTrain, yVal = (
    x[:train_indices],
    x[train_indices:],
    y[:train_indices],
    y[train_indices:]
)

print(x, y)

"""Berdasarkan proses *data understanding* atau pemahaman data sebelumnya, diketahui bahwa jumlah data yang tersedia cukup besar, dengan ratusan ribu hingga jutaan data. Volume data ini berpengaruh terhadap waktu komputasi dan sumber daya yang dibutuhkan untuk proses *modeling*. Oleh karena itu, pada proyek ini, jumlah data akan dibatasi menjadi 10.000 data `books` dan 5.000 data `ratings` untuk proses pemodelan."""

books   = books[:10000]
ratings = ratings[:5000]

"""# **5. Modeling**

Tahap selanjutnya dalam proyek ini adalah proses *modeling* atau membangun model *machine learning* yang berfungsi sebagai sistem rekomendasi. Model ini akan menggunakan berbagai algoritma rekomendasi tertentu untuk memberikan rekomendasi buku terbaik kepada pengguna.

## 5.1 Content-based Recommendation

Sistem rekomendasi berbasis konten *(Content-based Recommendation)* digunakan untuk merekomendasikan item yang serupa dengan yang disukai pengguna sebelumnya. Metode *content-based filtering* mempelajari preferensi pengguna berdasarkan informasi dari item yang pernah mereka nilai.

### 5.1.1 Cosine Similarity

Pengukuran kesamaan antar judul buku dilakukan dengan menggunakan teknik [`cosine_similarity`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_similarity.html 'cosine_similarity - scikit-learn Documentation'), melalui fungsi `cosine_similarity` dari library `sklearn`.
"""

cosine_sim = cosine_similarity(tfidf_matrix)
cosine_sim

"""Array hasil *cosine similarity* tersebut kemudian dikonversi menjadi *dataframe*.

"""

cosine_sim_df = pd.DataFrame(
    cosine_sim,
    columns = books.book_title,
    index   = books.book_title
)

print(f'Cosine Similarity Shape : {cosine_sim_df.shape}')

cosine_sim_df.sample(8, axis=1).sample(8, axis=0)

"""### 5.1.2 Recommendation Testing

Fungsi `author_recommendations` dibuat untuk menampilkan daftar buku yang direkomendasikan, berdasarkan input berupa nama penulis dari buku yang telah dibaca oleh *user*.
"""

def author_recommendations(book_title, similarity_data=cosine_sim_df, items=books[['book_title', 'book_author']], k=10):
    index = similarity_data.loc[:,book_title].to_numpy().argpartition(range(-1, -k, -1))
    closest = similarity_data.columns[index[-1:-(k+2):-1]]
    closest = closest.drop(book_title, errors='ignore')

    return pd.DataFrame(closest).merge(items).head(k)

"""Menyimpan judul buku yang sudah dibaca"""

readed_book_title = 'The Pillars of the Earth'

"""Mencari dan menampilkan data buku yang judulnya sama dengan nilai pada `readed_book_title`"""

books[books.book_title.eq(readed_book_title)]

"""Menampilkan rekomendasi buku berdasarkan buku yang telah dibaca `(readed_book_title)`, namun terkadang sistem memberikan rekomendasi yang sama lebih dari sekali, sehingga perlu menghilangkan judul buku yang duplikat dari hasil rekomendasi dengan `drop_duplicates()`."""

author_recommendations(readed_book_title).drop_duplicates()

"""Hasil dari sistem menunjukkan bahwa berdasarkan masukan nama buku "The Pillars of the Earth", sistem berhasil menghasilkan beberapa rekomendasi buku yang sesuai berdasarkan input atau masukan sebuah nama buku yaitu "The Pillars of the Earth" yang menghasilkan beberapa nama buku yang relevan berdasarkan perhitungan sistem.

## 5.2 Collaborative Filtering Recommendation

Sistem rekomendasi penyaringan kolaboratif (*Collaborative Filtering Recommendation*) bertujuan untuk merekomendasikan item yang disukai pengguna lain yang memiliki preferensi serupa. Pendekatan ini didasarkan pada rating yang diberikan oleh pengguna sebelumnya.

### 5.2.1 Model Development and Training

Model rekomendasi dikembangkan dengan memanfaatkan kelas `RecommenderNet` dengan [*keras model class*](https://keras.io/api/models/model 'Model class - Keras Documentation').
"""

class RecommenderNet(tf.keras.Model):
    def __init__(self, num_users, num_books, embedding_size, **kwargs):
        super(RecommenderNet, self).__init__(**kwargs)
        self.num_users = num_users
        self.num_books = num_books
        self.embedding_size = embedding_size
        self.user_embedding = layers.Embedding(
            num_users,
            embedding_size,
            embeddings_initializer = 'he_normal',
            embeddings_regularizer = keras.regularizers.l2(1e-6)
        )
        self.user_bias      = layers.Embedding(num_users, 1)
        self.book_embedding = layers.Embedding(
            num_books,
            embedding_size,
            embeddings_initializer = 'he_normal',
            embeddings_regularizer = keras.regularizers.l2(1e-6)
        )
        self.book_bias = layers.Embedding(num_books, 1)

    def call(self, inputs):
        user_vector = self.user_embedding(inputs[:,0])
        user_bias   = self.user_bias(inputs[:, 0])
        book_vector = self.book_embedding(inputs[:, 1])
        book_bias   = self.book_bias(inputs[:, 1])

        dot_user_book = tf.tensordot(user_vector, book_vector, 2)

        x = dot_user_book + user_bias + book_bias

        return tf.nn.sigmoid(x)

"""Dalam proses *model compiling*, digunakan [Adam optimizer](https://keras.io/api/optimizers/adam 'Adam - Keras Documentation'), [binary crossentropy loss function](https://keras.io/api/losses/probabilistic_losses/#binarycrossentropy-class 'BinaryCrossentropy - Keras Documentaion'), dan metrik [RMSE](https://keras.io/api/metrics/regression_metrics/#rootmeansquarederror-class 'RootMeanSquaredError - Keras Documentation') (Root Mean Squared Error).


"""

model = RecommenderNet(num_users, num_books, 50)

model.compile(
    optimizer = Adam(learning_rate=0.001),
    loss      = BinaryCrossentropy(),
    metrics   = [RootMeanSquaredError()]
)

"""Model kemudian dilatih *(training)* menggunakan fungsi `.fit()` dengan parameter `batch_size`=20 dan `epochs`=30.

"""

history = model.fit(
    x               = xTrain,
    y               = yTrain,
    batch_size      = 20,
    epochs          = 30,
    validation_data = (xVal, yVal),
)

"""### 5.2.2 Recommendation Testing

*Dataset books* dan *ratings* didefinisikan ulang.
"""

datasetBook   = books
datasetRating = ratings

"""Untuk menghasilkan rekomendasi, diperlukan sebuah data atau sampel dari pengguna secara acak dan mendefinisikan variabel buku yang belum pernah dibaca oleh pengguna (`notReadedBooks`)ditentukan menggunakan operator logika bitwise ([`~`](https://docs.python.org/3/reference/expressions.html#unary-arithmetic-and-bitwise-operations 'Unary Arithmetic and Bitwise Operations - Python Documentation')) terhadap buku yang sudah dibaca oleh *user* (`readedBooks`)."""

userId      = datasetRating.user_id.sample(1).iloc[0]
readedBooks = datasetRating[datasetRating.user_id == userId]

notReadedBooks = datasetBook[~datasetBook['isbn'].isin(readedBooks.isbn.values)]['isbn']
notReadedBooks = list(
    set(notReadedBooks).intersection(set(book_to_book_encoded.keys()))
)

notReadedBooks = [[book_to_book_encoded.get(x)] for x in notReadedBooks]
userEncoder    = user_to_user_encoded.get(userId)
userBookArray = np.hstack(
    ([[userEncoder]] * len(notReadedBooks), notReadedBooks)
)

"""Prediksi terhadap daftar buku yang akan direkomendasikan dilakukan dengan menggunakan fungsi [`.predict()`](https://keras.io/api/models/model 'Model class - Keras Documentation') dari *library* Keras."""

ratings = model.predict(userBookArray).flatten()

topRatingsIndices   = ratings.argsort()[-10:][::-1]
recommendedBookIds = [
    book_encoded_to_book.get(notReadedBooks[x][0]) for x in topRatingsIndices
]

print('Showing recommendations for users: {}'.format(userId))
print('=====' * 8)
print('Book with high ratings from user')
print('-----' * 8)

topBookUser = (
    readedBooks.sort_values(
        by = 'book_rating',
        ascending=False
    )
    .head(5)
    .isbn.values
)

bookDfRows = datasetBook[datasetBook['isbn'].isin(topBookUser)]
for row in bookDfRows.itertuples():
    print(row.book_title, 'oleh', row.book_author)

print('=====' * 8)
print('Top 10 Books Recommendation')
print('-----' * 8)

recommended_books = datasetBook[datasetBook['isbn'].isin(recommendedBookIds)]
for row in recommended_books.itertuples():
    print(row.book_title, 'oleh', row.book_author)

"""Berdasarkan hasil prediksi sistem, pengguna dengan `user_id` **1248** dipilih secara acak. Dari data yang diperoleh, sistem mengidentifikasi buku-buku dengan rating tertinggi yang diberikan oleh pengguna tersebut, yaitu:

- **House Harkonnen (Dune: House Trilogy, Book 2)** oleh **Brian Herbert**
- **House Atreides (Dune: House Trilogy, Book 1)** oleh **Brian Herbert**
- **Me and My Little Brain** oleh **John Fitzgerald**
- **And the Sea Will Tell** oleh **Vincent Bugliosi**
- **The Sparrow** oleh **Mary Doria Russell**

Langkah selanjutnya, sistem mencocokkan buku-buku favorit dari `user_id` **1248** dengan koleksi buku yang belum pernah dibaca oleh pengguna tersebut. Proses ini menghasilkan daftar rekomendasi berdasarkan skor prediksi tertinggi terhadap preferensi pengguna.

Jika diperhatikan, terdapat kemiripan antara buku favorit pengguna dan hasil rekomendasi, misalnya, **The Sparrow** memiliki kesamaan dengan **Life of Pi**.

Sistem rekomendasi ini menunjukkan kemampuannya dalam memahami pola preferensi pengguna dan menyarankan buku-buku yang tidak hanya serupa dalam tema, tetapi juga memperluas preferensi pengguna terhadap genre dan penulis baru. Hal ini menjadikan pengalaman membaca lebih beragam.

# **6. Evaluation**

Tahap berikutnya dalam proyek ini adalah menentukan metrik evaluasi yang digunakan untuk mengukur kinerja model rekomendasi yang telah dibangun. Pemilihan metrik evaluasi disesuaikan dengan konteks data, permasalahan yang dihadapi, serta solusi yang diharapkan dari sistem rekomendasi ini.

## 6.1 Content-based Evaluation

Metrik evaluasi yang digunakan dalam proyek ini adalah Precision. Precision mengukur seberapa tepat rekomendasi yang diberikan oleh model, yaitu proporsi rekomendasi yang relevan dari seluruh rekomendasi yang dihasilkan.

Mengukur precision@k, eberapa tepat rekomendasi buku yang diberikan berdasarkan buku tertentu dengan membandingkan berapa banyak buku yang direkomendasikan dari penulis yang sama dalam 10 rekomendasi teratas.
"""

def precision_at_k(book_title, k=10):
    if book_title not in books['book_title'].values:
        print(f"Judul buku '{book_title}' tidak ditemukan di dataset.")
        return 0.0, 0, 0, set()

    author_name = books[books.book_title == book_title]['book_author'].values[0]
    relevant_books = set(books[books.book_author == author_name]['book_title'].values)

    recommended = author_recommendations(book_title).drop_duplicates()
    recommended = recommended.head(k)  # Safe even if len < k
    recommended_titles = set(recommended['book_title'].values)

    actual_k = len(recommended_titles)
    relevant_in_k = len(recommended_titles & relevant_books)

    precision = (relevant_in_k / actual_k) * 100 if actual_k > 0 else 0

    return precision, relevant_in_k, len(relevant_books), recommended_titles

"""Menguji seberapa akurat sistem rekomendasi dengan menghitung precision@10 pada buku berjudul The Pillars of the Earth, lalu menampilkan persentase ketepatan rekomendasi dan jumlah rekomendasi yang relevan berdasarkan penulis yang sama."""

readed_book_title = 'The Pillars of the Earth'  # Judul buku yang sama dengan recommendation testing
precision, relevan_ditemukan, relevant_books, buku_rekomendasi = precision_at_k(readed_book_title, k=10)

print(f'Precision@10 untuk buku "{readed_book_title}": {precision:.2f}%')
print(f'{relevan_ditemukan} dari {len(buku_rekomendasi)} rekomendasi cocok dengan {relevant_books} buku oleh author yang sama.')

"""## 6.2 Collaborative Filtering Evaluation

Visualisasi performa *training* dan *validation* *error* serta *training* dan *validation* *loss* ditampilkan melalui grafik menggunakan *library* [`matplotlib`](https://matplotlib.org 'Matplotlib - Visualization with Python').
"""

rmse     = history.history['root_mean_squared_error']
val_rmse = history.history['val_root_mean_squared_error']

loss     = history.history['loss']
val_loss = history.history['val_loss']

plt.figure(figsize = (12, 4))
plt.subplot(1, 2, 1)
plt.plot(rmse,     label='RMSE')
plt.plot(val_rmse, label='Validation RMSE')
plt.title('Training and Validation Error')
plt.xlabel('Epoch')
plt.ylabel('Root Mean Squared Error')
plt.legend(loc='lower right')

plt.subplot(1, 2, 2)
plt.plot(loss,     label='Training Loss')
plt.plot(val_loss, label='Validation Loss')
plt.title('Training and Validation Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend(loc='upper right')

plt.show()

"""# **7. Kesimpulan**

Kesimpulan dari pengembangan model yang digunakan untuk membuat rekomendasi buku ini menunjukkan bahwa kedua pendekatan, yaitu *Content-based Recommendation* dan *Collaborative Filtering Recommendation*, berhasil diterapkan sesuai dengan preferensi pengguna. Pada metode *collaborative filtering*, data *rating* pengguna sangat diperlukan untuk menghasilkan rekomendasi, sedangkan pada *content-based filtering*, sistem hanya mengandalkan atribut dari buku tanpa membutuhkan data *rating*. Masing-masing pendekatan tersebut memiliki keunggulan dan keterbatasan tersendiri dalam penggunaannya.
"""