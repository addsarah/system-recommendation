
# Laporan Proyek Akhir Machine Learning Expert Dicoding: System Recommendation - Books - Sarah Adibah

## Table of Contents

- [Project Overview](#project-overview)
- [Business Understanding](#business-understanding)
- [Data Understanding](#data-understanding)
- [Data Preprocessing](#data-preprocessing)
- [Data Preparation](#data-preparation)
- [Modeling](#modeling)
- [Evaluation](#evaluation)
- [Kesimpulan](#kesimpulan)
- [Reference](#reference)
  
## Project Overview
<img src="https://foto.wartaekonomi.co.id/files/arsip_foto_2021_06_18/nasional_2021_06_18_113235_big.jpg" alt="Minat Baca Indonesia Infografis" title="Minat Baca Indonesia Infografis">

Di tengah pesatnya kemajuan teknologi digital dan derasnya arus informasi, kemampuan membaca tetap menjadi fondasi utama dalam proses pembelajaran dan menjadi benteng awal dalam menangkal informasi palsu atau hoaks yang marak tersebar di media sosial maupun platform digital lainnya. Namun, kenyataan di lapangan menunjukkan bahwa minat baca masyarakat Indonesia masih sangat rendah. UNESCO menyebut bahwa indeks minat baca di Indonesia hanya sebesar **0,001%**, artinya dari setiap 1.000 orang, hanya satu orang yang memiliki kebiasaan membaca secara aktif. Data serupa dari _World’s Most Literate Nations Ranked_ yang dilakukan oleh Central Connecticut State University pada 2016 juga menempatkan Indonesia di peringkat **ke-60 dari 61 negara**, tepat di bawah Thailand dan hanya sedikit lebih baik dari Botswana, meskipun secara infrastruktur literasi Indonesia berada di atas beberapa negara Eropa.[[1]](https://www.rri.co.id/daerah/649261/unesco-sebut-minat-baca-orang-indonesia-masih-rendah)

Meski begitu, masih ada harapan dari berbagai pihak untuk meningkatkan minat baca masyarakat. Salah satunya melalui studi dari _Programme for International Student Assessment (PISA)_ pada 2022 yang menunjukkan bahwa Indonesia naik lima peringkat dalam literasi membaca dibandingkan tahun 2018, walaupun skor yang didapatkan masih mengalami penurunan dan tetap berada di **11 posisi terbawah dari 81 negara**. Hal ini diperkuat oleh pernyataan Prof. Mochamad Nursalim dari Universitas Negeri Surabaya yang mengatakan bahwa rendahnya minat baca bukan hanya terjadi di masyarakat umum, tetapi juga di kalangan mahasiswa. Menurutnya, transformasi digital telah mengubah kebiasaan membaca dari buku fisik ke bentuk elektronik atau digital, namun hal ini belum tentu diikuti dengan peningkatan minat membaca.[[1]](https://www.rri.co.id/daerah/649261/unesco-sebut-minat-baca-orang-indonesia-masih-rendah)

Survei Perpustakaan Nasional Republik Indonesia pada tahun 2022 memperlihatkan peningkatan kegemaran membaca masyarakat, dengan skor nasional mencapai **63,9 poin**, dihitung berdasarkan frekuensi membaca dan durasi akses terhadap bacaan digital. Daerah Istimewa Yogyakarta menempati posisi tertinggi dengan skor **72,29 poin**, disusul oleh Jawa Tengah (70,96), Jawa Barat (70,1), DKI Jakarta (68,71), dan Jawa Timur (68,54). Rata-rata waktu yang dihabiskan masyarakat Indonesia untuk membaca dalam sehari mencapai **1 jam 37,8 menit**, atau **hampir 10 jam per minggu**, menandakan adanya pertumbuhan minat baca dibanding tahun-tahun sebelumnya. Namun, jika dibandingkan secara global, Indonesia masih jauh tertinggal. Amerika Serikat, misalnya, memiliki rata-rata **17 buku** yang dibaca per orang per tahun, disusul India (**16 buku**) dan Inggris (**15 buku**). [[2]](https://infogarut.id/23-april-diperingati-sebagai-hari-buku-sedunia-apa-kabar-dengan-minat-baca-orang-indonesia)

Melihat kenyataan ini, perlu adanya inovasi teknologi yang dapat membantu meningkatkan budaya literasi masyarakat. Salah satu solusi yang potensial adalah pengembangan **sistem rekomendasi buku** berbasis _machine learning_ yang dapat membantu pengguna menemukan buku yang sesuai dengan minat, kebiasaan, dan preferensi mereka. Sistem ini dapat di-_deploy_ untuk berbagai kebutuhan, seperti katalog buku di perpustakaan, daftar rekomendasi buku digital, media sosial literasi seperti Medium, maupun _e-commerce_ buku seperti Gramedia Digital maupun Google Books. Dengan penerapan sistem ini, pengalaman membaca akan menjadi lebih personal, menyenangkan, dan efisien sehingga dengan harapan mampu meningkatkan frekuensi dan minat baca masyarakat secara luas.


## Business Understanding
### Problem Statements
Berdasarkan latar belakang yang telah dijelaskan di atas, maka diperoleh rumusan masalah yang akan diselesaikan pada proyek ini, yaitu:

1.  Bagaimana cara melakukan tahap persiapan data buku, pengguna, dan _rating_ atau penilaian agar dapat digunakan sebagai informasi untuk membuat model _machine learning_ sistem rekomendasi?
    
2.  Bagaimana cara membuat model _machine learning_ untuk sistem rekomendasi buku?
    

### Goals

Berdasarkan rumusan masalah yang telah dipaparkan di atas, maka didapatkan tujuan dari proyek ini, yaitu:

1.  Melakukan tahap persiapan data sehingga data siap digunakan pada model _machine learning_ untuk sistem rekomendasi.
    
2.  Membuat model _machine learning_ untuk sistem rekomendasi buku terbaik kepada pengguna.

### Solution Statements
Dibawah ini merupakan diagram alir *(workflow)* yang digunakan dalam pengerjaan proyek ini
```mermaid
flowchart LR
    A[Dataset Download] --> B[Data Understanding]
    B --> C[Data Preprocessing]
    C --> D[Data Preparation]
    D --> E[Modeling]
    E --> F[Evaluation]
    B --> G[Data Visualization]
```

Berdasarkan tujuan dari proyek yang telah dipaparkan di atas, maka berikut adalah beberapa solusi yang dapat dilakukan agar dapat mencapai tujuan dari proyek ini, yaitu:
1.  **Tahap pra-pemrosesan data (data preprocessing)** merupakan proses awal yang bertujuan untuk mengubah data mentah menjadi data yang lebih rapi dan siap digunakan pada tahap berikutnya. Proses ini mencakup:
	-   Penyesuaian serta perubahan nama kolom atau atribut sehingga proses pemanggilan data menjadi lebih efisien.
	-   Penggabungan beberapa data yang terpisah agar dapat digunakan secara utuh pada proses analisis dan pemodelan selanjutnya.
    
2. **Tahap persiapan data (data preparation)** merupakan proses transformasi lanjutan agar data berada dalam format yang optimal untuk membangun model. Beberapa teknik yang dilakukan meliputi:
	-   Identifikasi nilai yang kosong atau tidak tersedia (_missing values_), lalu mengambil tindakan seperti menghapus data tersebut atau mengisinya dengan nilai tertentu agar tidak memengaruhi performa model.
	-   Deteksi data duplikat guna menghindari bias dalam hasil pemodelan.

3. **Tahap pembuatan model _machine learning_ untuk sistem rekomendasi buku** akan berfokus pada pembangunan sistem rekomendasi yang bersifat personal. Model akan dikembangkan menggunakan dua pendekatan utama, yaitu:
	-   _Content-based Recommendation_ merupakan metode yang menyarankan item yang memiliki kemiripan karakteristik dengan item yang sebelumnya disukai oleh pengguna. Pendekatan ini memanfaatkan profil preferensi pengguna berdasarkan data dari item yang telah diberi penilaian oleh pengguna lain sebelumnya dan merekomendasikan barang baru yang serupa kepada pengguna.[[3]](https://www.ibm.com/think/topics/content-based-filtering)

		Dalam implementasinya, _content-based filtering_ menggunakan algoritma _TF-IDF Vectorizer_ untuk merepresentasikan fitur item dalam bentuk vektor, serta _Cosine Similarity_ untuk mengukur tingkat kesamaan antar item.[[4]](https://medium.com/@prateekgaurav/step-by-step-content-based-recommendation-system-823bbfd0541c)
		- TF-IDF Vectorizer (Term Frequency-Inverse Document Frequency Vectorizer) merupakan metode yang digunakan untuk menghitung dan mengubah teks mentah menjadi bentuk numerik bermakna dalam format matriks, sehingga dapat diproses dan dipahami oleh model _machine learning_.[[5]](https://towardsdatascience.com/tf-idf-simplified-aba19d5f5530/) 

			Keunggulan dari teknik ini adalah tidak memerlukan data dari pengguna lain karena rekomendasi yang dihasilkan bersifat personal dan disesuaikan secara khusus untuk masing-masing pengguna. Namun, kelemahannya terletak pada keterbatasan rekomendasi yang hanya berasal dari preferensi pengguna tersebut, sehingga tidak memanfaatkan informasi dari penilaian pengguna lain untuk memperluas hasil rekomendasi.
			TF-IDF dapat dihitung menggunakan rumus sebagai berikut: 

			$$idf_i=log \left( \frac{n}{df_i} \right)$$

			Nilai $idf_i$ adalah skor Inverse Document Frequency untuk _term_ $i$, dengan $df_i$ menunjukkan jumlah dokumen yang mengandung _term_ tersebut, dan $n$ mewakili total seluruh dokumen. Semakin banyak dokumen yang mengandung _term_ tertentu (semakin tinggi $df$), maka nilai $idf$-nya akan semakin rendah. Jika suatu _term_ muncul di semua dokumen ($df = n$), maka nilai $idf$ menjadi 0 karena $log(1) = 0$.

			Sedangkan Nilai TF-IDF diperoleh dari hasil perkalian antara matriks frekuensi term (TF) dengan nilai Inverse Document Frequency (IDF) masing-masing term.

			$$w_{i,j}=tf_{i,j} \times idf_i$$

			Skor TF-IDF $w_{i,j}$ menunjukkan bobot _term_ $i$ dalam dokumen $j$ yang diperoleh dari hasil perkalian antara frekuensi _term_ $tf_{i,j}$ dalam dokumen $j$ dan skor IDF $idf_i$ dari _term_ tersebut.
		- Cosine Similarity
		Teknik **cosine similarity** digunakan untuk menghitung tingkat kemiripan antara dua sampel berdasarkan sudut di antara vektor representasinya. [[6]](https://www.sciencedirect.com/topics/computer-science/cosine-similarity)

			$$S_c(A,B) = \cos(\theta) = \frac{A \times B}{\|A\| \|B\|} = \frac{\displaystyle\sum_{i=1}^{n} {A_i}{B_i}}{\sqrt{\displaystyle\sum_{i=1}^{n} A_{i}^{2}} \sqrt{\displaystyle\sum_{i=1}^{n} B_{i}^{2}}}$$

			$A_i$ dan $B_i$ adalah elemen-elemen penyusun vektor A dan B masing-masing.

	-   _Collaborative Filtering Recommendation_
			Sistem rekomendasi yang bekerja dengan cara merekomendasikan item berdasarkan kesamaan preferensi atau interaksi antar pengguna. Berbeda dengan content-based filtering yang fokus merekomendasikan item berdasarkan fitur dari item itu sendiri, collaborative filtering memanfaatkan pola kesamaan antar pengguna untuk memberikan rekomendasi yang lebih personal dan relevan bagi kelompok pengguna tertentu.[[7]](https://www.ibm.com/think/topics/collaborative-filtering)

	    Collaborative filtering unggul dalam memberikan rekomendasi yang beragam dan personal berdasarkan kesamaan minat pengguna lain, sehingga bisa menyarankan item baru yang relevan. Namun, metode ini memiliki kekurangan seperti _cold start_ pada pengguna atau item baru tanpa data interaksi, serta masalah _data sparsity_ yang menyulitkan sistem menemukan pola yang tepat. [[7]](https://www.ibm.com/think/topics/collaborative-filtering)

[←Table of Contents](#table-of-contents)


## Data Understanding
<img src="https://raw.githubusercontent.com/addsarah/system-recommendation/refs/heads/main/img/Books%20Datasets%20Kaggle%20Dataset.png" alt="Books Datasets Kaggle Dataset" title="Books Datasets Kaggle Dataset">

Data yang digunakan dalam proyek ini berasal dari _dataset_ yang diunduh dari Kaggle. Berikut ini adalah rincian informasi mengenai _dataset_ tersebut.

| Keterangan             | Detail                                                                                     |
|------------------------|--------------------------------------------------------------------------------------------|
| Sumber                 | [Kaggle Dataset: Books Dataset](https://www.kaggle.com/datasets/saurabhbagchi/books-dataset) |
| Usability              | 10.00                                                                                      |
| Lisensi                | CC0: Public Domain                                                                         |
| Penilaian/Rating       | Silver                                                                                     |
| Jenis & Ukuran Berkas  | ZIP (26 MB)                                                                               |
| Kategori               | Business, Literature, E-Commerce Services, Recommender Systems, Marketing                  |

Dalam dataset tersebut berisi tiga (3) berkas CSV ([Comma-separated Values](https://docs.python.org/3/library/csv.html)), yaitu `books.csv`, `ratings.csv`, `users.csv` yang terdapat di dalam folder `books_data`.

1. **books.csv**, memiliki 271.360 baris, 8 kolom, dan atribut atau fitur sebagai berikut,  
   <img src="https://raw.githubusercontent.com/addsarah/system-recommendation/refs/heads/main/img/Deskripsi%20Variabel%20Books.png" alt="Deskripsi Variabel Books" title="Deskripsi Variabel Books">

   - `ISBN` : *International Standard Book Number*  
   - `Book-Title` : Judul buku  
   - `Book-Author` : Penulis buku  
   - `Year-Of-Publication` : Tahun terbit buku  
   - `Publisher` : Penerbit buku  
   - `Image-URL-S` : Tautan sampul buku ukuran kecil  
   - `Image-URL-M` : Tautan sampul buku ukuran sedang  
   - `Image-URL-L` : Tautan sampul buku ukuran besar  

2. **ratings.csv**, memiliki 1.149.780 baris, 3 kolom, dan atribut atau fitur sebagai berikut,  
   <img src="https://raw.githubusercontent.com/addsarah/system-recommendation/refs/heads/main/img/Deskripsi%20Variabel%20Ratings.png" alt="Deskripsi Variabel Ratings" title="Deskripsi Variabel Ratings">

   - `User-ID` : Identitas unik pengguna berupa bilangan bulat atau integer  
   - `ISBN` : *International Standard Book Number*  
   - `Book-Rating` : *Rating* buku yang diberikan pengguna  

3. **users.csv**, memiliki 278.858 baris, 3 kolom, dan atribut atau fitur sebagai berikut,  
   <img src="https://raw.githubusercontent.com/addsarah/system-recommendation/refs/heads/main/img/Deskripsi%20Variabel%20User.png" alt="Deskripsi Variabel Users" title="Deskripsi Variabel Users">

   - `User-ID` : Identitas unik pengguna berupa bilangan bulat atau integer  
   - `Location` : Lokasi tempat tinggal pengguna  
   - `Age` : Umur pengguna  

Deskripsi statistik untuk _dataset_ `ratings` pada fitur `Book-Rating` dapat dilihat pada tabel di bawah ini.

|                  | **Book-Rating** |
|------------------|-----------------|
| **count**        | 1,149,780       |
| **mean**         | 3               |
| **std**          | 4               |
| **min**          | 0               |
| **25%**          | 0               |
| **50%**          | 0               |
| **75%**          | 7               |
| **max**          | 10              |
| **dtype**        | object          |

Dari tabel di atas dapat dilihat bahwa terdapat:  
- Total jumlah data (`count`) sebanyak 1.149.780;  
- Rata-rata *rating* (`mean`) 3;  
- Simpangan baku/standar deviasi *rating* (`std`) 4;  
- *Rating* Minimal (`min`) 0;  
- Kuartil bawah/Q1 *rating* (`25%`) 0;  
- Kuartil tengah/Q2/median *rating* (`50%`) 0;  
- Kuartil atas/Q3 *rating* (`75%`) 7;  
- *Rating* maksimum (`max`) 10.  

Berikut merupakan visualisasi grafik histogram yang menampilkan frekuensi distribusi *rating* yang diberikan pengguna terhadap buku yang telah mereka baca, dengan rentang nilai dari 0 hingga 10.

<img src="https://raw.githubusercontent.com/addsarah/system-recommendation/refs/heads/main/img/Grafik%20Histogram%20Frekuensi%20Sebaran%20Data%20Rating%20010.png" alt="Grafik Histogram Frekuensi Sebaran Data Rating 0-10" title="Grafik Histogram Frekuensi Sebaran Data Rating 0-10">

Dari visualisasi grafik histogram "Jumlah Rating Buku" di atas, terlihat bahwa *rating* yang paling sering muncul adalah *rating* 0, dengan jumlah lebih dari 700.000. Kehadiran rating 0 ini berpotensi menimbulkan bias dan memengaruhi hasil analisis, sehingga rating tersebut sebaiknya dihapus pada tahap [data preparation](#data-preparation).

Kondisi data berdasarkan dataset [Books Dataset](https://www.kaggle.com/datasets/saurabhbagchi/books-dataset) yang digunakan:
- **Missing Value**
    -   Pada dataset **books.csv**, terdapat beberapa kolom yang memiliki missing value, seperti `Book-Author`, `Publisher`, dan `Image-URL-L`.
    -   Pada dataset **users.csv**, kolom `Age` memiliki banyak nilai kosong (missing value).
    -   Dataset **ratings.csv** umumnya lengkap tanpa missing value pada kolom utama (`User-ID`, `ISBN`, `Book-Rating`).
        
- **Duplikat**
    -   Pada dataset buku dan pengguna, ada kemungkinan data duplikat, misalnya buku dengan ISBN. Akan diperiksa dan dibersihkan pada bagian [_data preparation_](#data-preparation) jika ditemukan duplikat.
         
-  **Konsistensi Data**
    -   Ada kemungkinan ketidaksesuaian penulisan nama penulis atau judul buku (typo atau variasi penulisan) yang bisa memengaruhi hasil rekomendasi.
   
 - **Ukuran Dataset**
    -   Dataset cukup besar (jutaan baris pada ratings dan ratusan ribu pada books dan users), sehingga perlu dibatasi menjadi 10.000 data `books` dan 5.000 data `ratings` pada bagian [_data preparation_](#data-preparation).
        
[←Table of Contents](#table-of-contents)


## Data Preprocessing

Tahap _data preprocessing_ atau pra-pemrosesan data bertujuan untuk mengolah data mentah *(raw data)* menjadi data yang bersih *(clean data)* dan siap digunakan dalam proses analisis berikutnya. Proses ini mencakup beberapa langkah penting, antara lain:

- **Mengubah Nama Kolom/Atribut/Fitur**  
  Penggantian nama kolom, atribut, atau fitur pada masing-masing _dataframe_ dilakukan untuk mempermudah proses akses dan manipulasi data di tahap selanjutnya.

  1. Books

     | isbn       | book_title                                      | book_author           | year_pub | publisher              | image_url_s                                        | image_url_m                                        | image_url_l                                        |
     |------------|------------------------------------------------|-----------------------|----------|------------------------|---------------------------------------------------|---------------------------------------------------|---------------------------------------------------|
     | 0195153448 | Classical Mythology                             | Mark P. O. Morford    | 2002     | Oxford University Press| http://images.amazon.com/images/P/0195153448.0.jpg| http://images.amazon.com/images/P/0195153448.0.jpg| http://images.amazon.com/images/P/0195153448.0.jpg|
     | 0002005018 | Clara Callan                                    | Richard Bruce Wright  | 2001     | HarperFlamingo Canada  | http://images.amazon.com/images/P/0002005018.0.jpg| http://images.amazon.com/images/P/0002005018.0.jpg| http://images.amazon.com/images/P/0002005018.0.jpg|
     | 0060973129 | Decision in Normandy                            | Carlo D'Este          | 1991     | HarperPerennial        | http://images.amazon.com/images/P/0060973129.0.jpg| http://images.amazon.com/images/P/0060973129.0.jpg| http://images.amazon.com/images/P/0060973129.0.jpg|
     | 0374157065 | Flu: The Story of the Great Influenza Pandemic | Gina Bari Kolata      | 1999     | Farrar Straus Giroux   | http://images.amazon.com/images/P/0374157065.0.jpg| http://images.amazon.com/images/P/0374157065.0.jpg| http://images.amazon.com/images/P/0374157065.0.jpg|
     | 0393045218 | The Mummies of Urumchi                          | E. J. W. Barber       | 1999     | W. W. Norton & Company | http://images.amazon.com/images/P/0393045218.0.jpg| http://images.amazon.com/images/P/0393045218.0.jpg| http://images.amazon.com/images/P/0393045218.0.jpg|

  2. Ratings

     | user_id | isbn       | book_rating |
     |---------|------------|-------------|
     | 276725  | 034545104X | 0           |
     | 276726  | 0155061224 | 5           |
     | 276727  | 0446520802 | 0           |
     | 276729  | 052165615X | 3           |
     | 276729  | 0521795028 | 6           |

  3. User

     |     | user_id | location                         | age  |
     |-----|---------|---------------------------------|------|
     | 0   | 1       | nyc, new york, usa              | NaN  |
     | 1   | 2       | stockton, california, usa       | 18.0 |
     | 2   | 3       | moscow, yukon territory, russia| NaN  |
     | 3   | 4       | porto, v.n.gaia, portugal       | 17.0 |
     | 4   | 5       | farnborough, hants, united kingdom | NaN |

- **Menggabungkan Data ISBN**  
  Penggabungan data ISBN buku dilakukan dengan memanfaatkan fungsi `.concatenate` dari _library_ [`numpy`](https://numpy.org/). Karena informasi ISBN terdapat pada _dataframe_ buku dan _dataframe_ _rating_, maka dilakukan penyatuan data berdasarkan kolom `isbn`.

- **Menggabungkan Data User**  
  Sementara itu, penggabungan data `user_id` dilakukan juga menggunakan fungsi `.concatenate` dari _library_ [`numpy`](https://numpy.org/). Kolom `user_id` terdapat pada _dataframe_ _rating_ dan _user_, sehingga proses penggabungan dilakukan berdasarkan atribut `user_id`.

[←Table of Contents](#table-of-contents)


## Data Preparation

Tahap _data preparation_ dilakukan proses transformasi data agar memiliki format yang sesuai untuk keperluan pemodelan. Beberapa langkah dilakukan dalam proses ini, antara lain:

- Pengecekan *Missing Value*

  Pemeriksaan terhadap data kosong, hilang, _null_, atau _missing value_ dilakukan dan ditemukan pada _dataframe_ `books`, sehingga data yang hilang tersebut dihapus.

  Sementara itu, pada _dataframe_ `ratings` tidak ditemukan _missing value_, namun perlu dilakukan penghapusan terhadap _rating_ bernilai 0. Hal ini dikarenakan _rating_ 0 merupakan kategori terbanyak berdasarkan hasil [_data understanding_](#data-understanding) sebelumnya, yaitu sebanyak 716.109 data. Jumlah tersebut berpotensi menimbulkan bias dalam analisis data, sehingga _rating_ 0 tidak disertakan dalam proses visualisasi grafik histogram berikutnya.

  <img src="https://raw.githubusercontent.com/addsarah/system-recommendation/refs/heads/main/img/Grafik%20Histogram%20Frekuensi%20Sebaran%20Data%20Rating%20110.png" alt="Grafik Histogram Frekuensi Sebaran Data Rating 1-10" title="Grafik Histogram Frekuensi Sebaran Data Rating 1-10">

  Setelah _rating_ 0 dihapus, hasil visualisasi grafik histogram menunjukkan pola distribusi frekuensi data yang lebih terstruktur dan mudah dibaca, khususnya pada rentang _rating_ 1 hingga 4.

  Kemudian pada *dataframe* `Users`, terdapat sebanyak 110.762 *missing value* pada fitur umur yang terdapat nilai kosong atau tidak valid seperti `'NaN'`, `'nan'`, `' '`, dan tanda kutip tunggal (`'`).

  | user_id | location                          | age  |
  |---------|---------------------------------|------|
  | 1       | nyc, new york, usa              | NaN  |
  | 2       | stockton, california, usa       | 18.0 |
  | 3       | moscow, yukon territory, russia | NaN  |
  | 4       | porto, v.n.gaia, portugal       | 17.0 |
  | 5       | farnborough, hants, united kingdom | NaN  |
  | ...     | ...                             | ...  |
  | 278854  | portland, oregon, usa           | NaN  |
  | 278855  | tacoma, washington, united kingdom | 50.0 |
  | 278856  | brampton, ontario, canada       | NaN  |
  | 278857  | knoxville, tennessee, usa       | NaN  |
  | 278858  | dublin, n/a, ireland            | NaN  |
  | 278858 rows × 3 columns          |       |


  Oleh karena itu, dilakukan proses pembersihan data dengan mengganti nilai-nilai tersebut menjadi `np.nan`. Selanjutnya, kolom `age` dikonversi ke tipe numerik agar bisa dianalisis, dan baris yang masih mengandung nilai NaN dihapus menggunakan fungsi `dropna()`.

  | user_id | location                         | age  |
  |---------|---------------------------------|------|
  | 1       | nyc, new york, usa              | 24.0 |
  | 2       | stockton, california, usa       | 18.0 |
  | 4       | porto, v.n.gaia, portugal       | 17.0 |
  | 6       | santa monica, california, usa   | 61.0 |
  | 10      | albacete, wisconsin, spain      | 26.0 |
  | ...     | ...                             | ...  |
  | 278849  | georgetown, ontario, canada     | 23.0 |
  | 278851  | dallas, texas, usa              | 33.0 |
  | 278852  | brisbane, queensland, australia | 32.0 |
  | 278853  | stranraer, n/a, united kingdom  | 17.0 |
  | 278855  | tacoma, washington, united kingdom | 50.0 |
  | 168096 rows × 3 columns          |       |

  Pemeriksaan ulang terhadap *dataframe* `users` menunjukkan bahwa tidak ada nilai kosong atau *null* yang ditemukan di seluruh kolomnya.

  <img src="https://raw.githubusercontent.com/addsarah/system-recommendation/refs/heads/main/img/Grafik%20Umur%20Users.png" alt="Grafik Umur Users" title="Grafik Umur Users">

  Berdasarkan hasil visualisasi grafik histogram umur *user* di atas, dapat dilihat bahwa mayoritas pengguna berada pada rentang usia 20—40 tahun, dengan puncak distribusi antara 30—35 tahun.

  Terdapat pula sebagian kecil pengguna dengan usia di bawah 10 tahun dan di atas 80 tahun, namun jumlahnya jauh lebih sedikit dibandingkan kelompok usia produktif. Hal ini menunjukkan bahwa sistem rekomendasi buku kemungkinan besar akan lebih relevan jika disesuaikan dengan preferensi kelompok usia 20—40 tahun.

- Pengecekan Data Duplikat

  Melakukan pengecekan terhadap duplikasi data pada masing-masing _dataframe_. Berdasarkan hasil verifikasi, tidak ditemukan adanya data yang terduplikasi pada ketiga _dataframe_ yang dianalisis.

- Data Buku dan *Rating*

  Melakukan penggabungan (_merge_) antara data buku dan data _rating_ untuk membentuk satu _dataframe_.

- TF-IDF Vectorizer

  Digunakan untuk mengubah data teks menjadi representasi numerik yang bermakna dalam bentuk matriks. Ukuran matriks yang dihasilkan memiliki 10.000 data buku dan 5.575 data penulis (*author*).

  | book_title                           | saavedra | louvish | gitlin | flank | reinhard | medina | volkart | hausman | hood | kincaid | morrell | whittaker | peretti | malerba | tropper | md  | nicola | riccardo | fan  | whittemore |
  |------------------------------------|----------|---------|--------|-------|----------|--------|---------|---------|------|---------|---------|-----------|---------|---------|---------|-----|--------|----------|------|------------|
  | The Night of Four Hundred Rabbits  | 0.0      | 0.0     | 0.0    | 0.0   | 0.0      | 0.0    | 0.0     | 0.0     | 0.0  | 0.0     | 0.0     | 0.0       | 0.0     | 0.0     | 0.0     | 0.0 | 0.0    | 0.0      | 0.0  | 0.0        |
  | Who Needs Decaf? (Harlequin Flipside, No. 6) | 0.0      | 0.0     | 0.0    | 0.0   | 0.0      | 0.0    | 0.0     | 0.0     | 0.0  | 0.0     | 0.0     | 0.0       | 0.0     | 0.0     | 0.0     | 0.0 | 0.0    | 0.0      | 0.0  | 0.0        |
  | BEAUTIFUL AND DAMNED               | 0.0      | 0.0     | 0.0    | 0.0   | 0.0      | 0.0    | 0.0     | 0.0     | 0.0  | 0.0     | 0.0     | 0.0       | 0.0     | 0.0     | 0.0     | 0.0 | 0.0    | 0.0      | 0.0  | 0.0        |
  | The Seville Communion              | 0.0      | 0.0     | 0.0    | 0.0   | 0.0      | 0.0    | 0.0     | 0.0     | 0.0  | 0.0     | 0.0     | 0.0       | 0.0     | 0.0     | 0.0     | 0.0 | 0.0    | 0.0      | 0.0  | 0.0        |
  | Richtig leben mit Geri Weibel. Neue Folge. | 0.0      | 0.0     | 0.0    | 0.0   | 0.0      | 0.0    | 0.0     | 0.0     | 0.0  | 0.0     | 0.0     | 0.0       | 0.0     | 0.0     | 0.0     | 0.0 | 0.0    | 0.0      | 0.0  | 0.0        |
  | Bodyguard / A Novel                | 0.0      | 0.0     | 0.0    | 0.0   | 0.0      | 0.0    | 0.0     | 0.0     | 0.0  | 0.0     | 0.0     | 0.0       | 0.0     | 0.0     | 0.0     | 0.0 | 0.0    | 0.0      | 0.0  | 0.0        |

- _Data preparation_
		Proses _data preparation_ dilakukan dengan menyandikan (*encoding*) fitur `user_id` dan `isbn` pada *dataframe* `ratings` menjadi  bentuk indeks integer. Setelah itu, hasil *encoding* tersebut dipetakan kembali ke dalam *dataframe ratings* masing-masing.

	Dari hasil tersebut, diperoleh 1.204 pengguna, 4.565 buku, dengan nilai *rating* terendah sebesar 1 dan nilai tertinggi sebesar 10.

- Split *Training Data* dan *Validation Data*
		Pada tahap ini, *dataframe ratings* diacak terlebih dahulu sebelum dibagi menjadi dua bagian dengan perbandingan 80:20, di mana 80% digunakan sebagai data pelatihan (*training data*) dan 20% sisanya sebagai data pengujian (*validation data*).

|       | user_id | isbn        | book_rating | user | book |
|-------|---------|-------------|-------------|------|------|
| 1554  | 277427  | 0375408886  | 9           | 200  | 681  |
| 1465  | 277427  | 0060542128  | 7           | 200  | 666  |
| 9656  | 81      | 0375410538  | 5           | 649  | 2307 |
| 4153  | 278257  | 0060194596  | 9           | 462  | 1728 |
| 4324  | 278411  | 0446608831  | 8           | 500  | 1825 |
| ...   | ...     | ...         | ...         | ...  | ...  |
| 820   | 277051  | 0385720920  | 10          | 98   | 380  |
| 629   | 276939  | 2253063339  | 9           | 70   | 269  |
| 12371 | 1167    | 038533656X  | 5           | 941  | 3478 |
| 2120  | 277478  | 0451459393  | 8           | 215  | 385  |
| 12752 | 1424    | 0156001314  | 8           | 1012 | 3676 |
|5000 rows × 5 columns|
		
	
   Mengacu pada tahap [*data understanding*](#data-understanding) yang telah dilakukan sebelumnya, diketahui bahwa masing-masing _dataframe_ buku, _rating_, dan *user* memiliki volume data yang sangat besar, mencapai ratusan ribu hingga jutaan data. Kondisi ini berpotensi menimbulkan peningkatan kebutuhan waktu proses pemodelan _machine learning_, seperti memakan waktu yang lama dan _resource_ RAM maupun GPU yang cukup besar. Oleh karena itu, data yang digunakan dalam tahap pemodelan akan dibatasi pada 10.000 data buku dan 5.000 data _rating_.

```python
books = books[:10000]

ratings = ratings[:5000]
```


[←Table of Contents](#table-of-contents)


## Modeling

Tahap selanjutnya adalah proses _modeling_, yaitu membangun model _machine learning_ yang berfungsi sebagai sistem rekomendasi untuk menyarankan buku terbaik kepada pengguna berdasarkan sejumlah algoritma sistem rekomendasi tertentu.

### 1. Content-based Recommendation

- **_Cosine Similarity_**  
  Digunakan untuk menghitung tingkat kemiripan antar judul buku. Hasil perhitungan ini menghasilkan matriks berukuran 10.000 data buku dan 10.000 data buku.

| book_title                                             | Whisper to Me of Love | En LA Boca Del Dragon | Standing Out (72) | Angel of Darkness (Key Books) | Rebekah (Women of Genesis) | There's No Toilet Paper on the Road Less Traveled: The Best of Travel Humor and Misadventure (Travelers' Tales Guides) | Wolf Moon | The Country Under My Skin: A Memoir of Love and War |
|--------------------------------------------------------|----------------------|----------------------|-------------------|-------------------------------|----------------------------|----------------------------------------------------------------------------------------------------------------------|-----------|-----------------------------------------------------|
| The Pursuit (Avon Historical Romance)                  | 0.0                  | 0.0                  | 0.0               | 0.0                           | 0.0                        | 0.0                                                                                                                  | 0.0       | 0.0                                                 |
| Hawaii's Best Spooky Tales: True Local Spine-Tinglers  | 0.0                  | 0.0                  | 0.0               | 0.0                           | 0.0                        | 0.0                                                                                                                  | 0.0       | 0.0                                                 |
| The STAR GROUP PAPERBACK                                | 0.0                  | 0.0                  | 0.0               | 0.0                           | 0.0                        | 0.0                                                                                                                  | 0.0       | 0.0                                                 |
| Too Close to the Falls: A Memoir                        | 0.0                  | 0.0                  | 0.0               | 0.0                           | 0.0                        | 0.0                                                                                                                  | 0.0       | 0.0                                                 |
| Die Entdeckung der Langsamkeit.                         | 0.0                  | 0.0                  | 0.0               | 0.0                           | 0.0                        | 0.0                                                                                                                  | 0.0       | 0.0                                                 |
| Crescent City                                          | 0.0                  | 0.0                  | 0.0               | 0.0                           | 0.0                        | 0.0                                                                                                                  | 0.0       | 0.0                                                 |
| The 1998 What Color Is Your Parachute                   | 0.0                  | 0.0                  | 0.0               | 0.0                           | 0.0                        | 0.0                                                                                                                  | 0.0       | 0.0                                                 |
| Rush Limbaugh Is a Big Fat Idiot: And Other Observations | 0.0                | 0.0                  | 0.0               | 0.0                           | 0.0                        | 0.0                                                                                                                  | 0.0       | 0.0                                                 |

- **Top-N Recommendation**  
  Hasil pengujian sistem rekomendasi berbasis pendekatan _content-based recommendation_ ditampilkan pada tabel di bawah.

|     | isbn       | book_title             | book_author | year_pub | publisher   | image_url_s                                              | image_url_m                                              | image_url_l                                              |
|-----|------------|------------------------|-------------|----------|-------------|----------------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------|
| 102 | 0451166892 | The Pillars of the Earth | Ken Follett | 1996     | Signet Book | http://images.amazon.com/images/P/0451166892.0...        | http://images.amazon.com/images/P/0451166892.0...        | http://images.amazon.com/images/P/0451166892.0...        |

Tabel tersebut menunjukkan data berdasarkan judul buku yang dipilih oleh pengguna sebagai masukan.

|    | book_title                               | book_author |
|----|------------------------------------------|-------------|
| 0  | Jackdaws                                | Ken Follett |
| 1  | Doble Juego                            | Ken Follett |
| 2  | Code to Zero                           | Ken Follett |
| 3  | Nacht über den Wassern.                 | Ken Follett |
| 4  | Los Pilares de la Tierra                 | Ken Follett |
| 5  | The Hammer of Eden: A Novel              | Ken Follett |
| 6  | Paper Money                            | Ken Follett |
| 7  | Die Säulen der Erde. Roman.             | Ken Follett |
| 8  | Night over Water                       | Ken Follett |

Berdasarkan hasil di atas, dapat disimpulkan bahwa sistem yang dikembangkan mampu menghasilkan sejumlah rekomendasi judul buku yang relevan berdasarkan judul buku input **“The Pillars of the Earth”**. Judul-judul yang direkomendasikan merupakan hasil perhitungan kesamaan konten oleh sistem.

### 2. Collaborative Filtering Recommendation

- **Hasil Model Development**  
  Berikut adalah hasil evaluasi dari sistem rekomendasi buku yang telah dilatih menggunakan pendekatan _collaborative filtering recommendation_.

  <img src="https://raw.githubusercontent.com/addsarah/system-recommendation/refs/heads/main/img/hasil%20collaborative%20filtering%20recommendation.png" alt="hasil collaborative filtering recommendation" title="hasil collaborative filtering recommendation">

  Berdasarkan hasil prediksi sistem, pengguna dengan `user_id` **1248** dipilih secara acak. Dari data yang diperoleh, sistem mengidentifikasi buku-buku dengan rating tertinggi yang diberikan oleh pengguna tersebut, yaitu:
  - **House Harkonnen (Dune: House Trilogy, Book 2)** oleh **Brian Herbert**
  - **House Atreides (Dune: House Trilogy, Book 1)** oleh **Brian Herbert**
  - **Me and My Little Brain** oleh **John Fitzgerald**
  - **And the Sea Will Tell** oleh **Vincent Bugliosi**
  - **The Sparrow** oleh **Mary Doria Russell**

  Langkah selanjutnya, sistem mencocokkan buku-buku favorit dari `user_id` **1248** dengan koleksi buku yang belum pernah dibaca oleh pengguna tersebut. Proses ini menghasilkan daftar rekomendasi berdasarkan skor prediksi tertinggi terhadap preferensi pengguna.

  Jika diperhatikan, terdapat kemiripan antara buku favorit pengguna dan hasil rekomendasi, terutama dari segi tema. Misalnya, **The Sparrow** memiliki kesamaan dengan *Life of Pi*.

  Sistem rekomendasi ini menunjukkan kemampuannya dalam memahami pola preferensi pengguna dan menyarankan buku-buku yang tidak hanya serupa dalam tema, tetapi juga memperluas preferensi pengguna terhadap genre dan penulis baru. Hal ini menjadikan pengalaman membaca lebih beragam.

[←Table of Contents](#table-of-contents)

## Evaluation
1. **Content-based Recommendation**
		Pada tahap evaluasi model sistem rekomendasi berbasis _content-based recommendation_, dilakukan pengukuran akurasi menggunakan metrik tertentu yang dihitung dengan rumus sebagai berikut:

	$\text{Precision@K} = \frac{\text{Number of Relevant Items in Top } K}{Total Number of Relevant Items}$

	Masih menggunakan dataset yang sama seperti pada tahap [Modeling](#modeling) untuk pendekatan _content-based recommendation_, evaluasi dilakukan berdasarkan hasil _Top-N Recommendation_. Dalam hal ini, sistem memberikan rekomendasi buku berdasarkan kemiripan dengan **"The Pillars of the Earth"**. Selanjutnya, dilakukan pencarian terhadap jumlah seluruh buku (`book_title`) yang ditulis oleh penulis yang sama dalam data, yaitu **Ken Follett**, dengan memanfaatkan variabel baru yang merepresentasikan daftar buku hasil rekomendasi.

	Dari pencarian tersebut diketahui bahwa **Ken Follett** menulis sebanyak **19** judul buku dalam dataset.

	Akurasi kemudian dihitung menggunakan _metric precision_ dengan membagi jumlah buku yang berhasil direkomendasikan oleh sistem (yang juga ditulis oleh **Ken Follett**) dengan jumlah total buku yang masuk dalam _Top-N Recommendation_, lalu dikalikan 100. [[8]](https://towardsdatascience.com/evaluation-metrics-for-recommendation-systems-an-overview-71290690ecba/)
	Dari proses tersebut, diperoleh:
	-   Jumlah rekomendasi yang cocok: **9**
	-   Jumlah rekomendasi total (_Top-N_): **9**
    -   Precision@10: **100,00%**
    
	Selain itu, **9 dari 9** buku rekomendasi juga termasuk dalam total **19** buku yang ditulis oleh penulis yang sama. Hasil ini menunjukkan bahwa sistem memiliki kemampuan yang sangat baik dalam mengidentifikasi dan merekomendasikan karya lain dari penulis favorit pengguna, yang menjadi indikator kuat dalam pendekatan _content-based filtering_.
	
3. **Collaborative Filtering Recommendation**  
	Berdasarkan odel *machine learning* yang telah dikembangkan menggunakan *embedding layer* dengan *Adam optimizer* dan fungsi loss *binary crossentropy* dievaluasi menggunakan metrik *Root Mean Squared Error* (RMSE). [[9]](https://towardsdatascience.com/comparing-robustness-of-mae-mse-and-rmse-6d69da870828/)
	Perhitungan RMSE dapat dilakukan dengan rumus berikut:

	  $$RMSE=\sqrt{\sum^{n}_{i=1} \frac{y_i - y\\_pred_i}{n}}$$


	Dimana:
	- $n$ adalah jumlah data dalam *dataset*,
	- $y_i$ adalah nilai sebenarnya,
	- $y_{pred_i}$ adalah nilai prediksi untuk data ke-$i$ dalam *dataset*.

	Hasil nilai RMSE yang rendah mengindikasikan bahwa variasi hasil prediksi model sangat mendekati variasi nilai observasi. Dengan kata lain, semakin kecil nilai RMSE, maka prediksi model semakin akurat dan mendekati nilai asli.

	Berikut ini adalah visualisasi grafik yang menampilkan hasil *training* dan *validation error* berdasarkan metrik RMSE, serta *training* dan *validation loss*.

	<img src="https://raw.githubusercontent.com/addsarah/system-recommendation/refs/heads/main/img/Model%20Training%20Plot.png" alt="Model Training Plot" title="Model Training Plot">


[←Table of Contents](#table-of-contents)

## Kesimpulan
Kesimpulan dari pengembangan model yang digunakan untuk membuat rekomendasi buku ini menunjukkan bahwa kedua pendekatan, yaitu *Content-based Recommendation* dan *Collaborative Filtering Recommendation*, berhasil diterapkan sesuai dengan preferensi pengguna. Pada metode *collaborative filtering*, data *rating* pengguna sangat diperlukan untuk menghasilkan rekomendasi, sedangkan pada *content-based filtering*, sistem hanya mengandalkan atribut dari buku tanpa membutuhkan data *rating*. Masing-masing pendekatan tersebut memiliki keunggulan dan keterbatasan tersendiri dalam penggunaannya.


[←Table of Contents](#table-of-contents)


## Reference
[1] Indrasari, Y., & Handayani, R. R. L. (2024, April 23). UNESCO Sebut Minat Baca Orang Indonesia Masih Rendah. RRI. Retrieved May 17, 2025, from https://www.rri.co.id/daerah/649261/unesco-sebut-minat-baca-orang-indonesia-masih-rendah

[2] Mardiani, R. (2025, April 25). 23 April Diperingati sebagai Hari Buku Sedunia, Apa Kabar dengan Minat Baca Orang Indonesia? Infogarut.id. Retrieved May 17, 2025, from https://infogarut.id/23-april-diperingati-sebagai-hari-buku-sedunia-apa-kabar-dengan-minat-baca-orang-indonesia

[3] Murel, J., & Kavlakoglu, E. (2024, March 21). What is content-based filtering? IBM. Retrieved May 17, 2025, from https://www.ibm.com/think/topics/content-based-filtering

[4] Gaurav, P. (2023, February 14). Step By Step Content-Based Recommendation System | by Prateek Gaurav. Medium. Retrieved May 17, 2025, from https://medium.com/@prateekgaurav/step-by-step-content-based-recommendation-system-823bbfd0541c

[5] Ramadhan, L. (2021, January 20). TF-IDF Simplified. Towards Data Science. Retrieved May 17, 2025, from https://towardsdatascience.com/tf-idf-simplified-aba19d5f5530/

[6] Chiclana, F., Tang, J., Jiang, Y., & Sridharan, S. (2022, February 11). Cosine Similarity. ScienceDirect. Retrieved May 17, 2025, from https://www.sciencedirect.com/topics/computer-science/cosine-similarity

[7] Murel, J., & Kavlakoglu, E. (2024, March 21). What is collaborative filtering? IBM. Retrieved May 17, 2025, from https://www.ibm.com/think/topics/collaborative-filtering

[8] Aher, P. (2023, August 9). Evaluation Metrics for Recommendation Systems – An Overview. Towards Data Science. Retrieved May 17, 2025, from https://towardsdatascience.com/evaluation-metrics-for-recommendation-systems-an-overview-71290690ecba/

[9] Trevisan, V. (2022, January 11). Comparing robustness of MAE, MSE and RMSE. Towards Data Science. Retrieved May 17, 2025, from https://towardsdatascience.com/comparing-robustness-of-mae-mse-and-rmse-6d69da870828/

[←Table of Contents](#table-of-contents)





