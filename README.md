## Tugas 2
### Checklist 1: Membuat Proyek Django Baru ☑️
1. Buat direktori baru bernama `abbey-road-store` dan nyalakan _virtual environment_ dengan menjalankan perintah berikut di Terminal yang sudah berada di direktori `abbey-road-store`.
   
   `python -m venv env`
   
   `env\Scripts\activate`
2. Di direktori tersebut, buat file txt baru bernama `requirements.txt` yang berisi beberapa _dependencies_ berikut.
   ```
   django
   gunicorn
   whitenoise
   psycopg2-binary
   requests
   urllib3
   ```
3. Lakukan instalasi terhadap _dependencies_ tersebut dengan menjalankan perintah berikut di Terminal.
   
   `pip install -r requirements.txt`
4. Buat proyek Django bernama `abbey-road-store` dengan menjalankan perintah berikut di Terminal.

   `django-admin startproject abbey-road-store .`

   Proyek Django bernama `abbey-road-store` akan muncul di dalam direktori.

### Checklist 2: Membuat Aplikasi `main`☑️
1. Jalankan perintah berikut di Terminal untuk membuat aplikasi baru.
   
   `python manage.py startapp main`
2. Daftarkan `main` ke dalam proyek dengan cara B]buka berkas `settings.py` dalam direktory `abbey-road-store`, lalu tambahkan `'main',` di dalam `INSTALLED_APPS`.
   ```
   INSTALLED_APPS = [
    ...,
    'main',
    ...
   ]
   ```
   
### Checklist 3: Melakukan _routing_ pada proyek☑️
1. Buka `urls.py` yang ada di dalam direktori `abbey-road-store`.
2. Pada bagian `import`, tambahkan baris berikut.

   ```
   ...
   from django.urls import path, include
   ...
   ```
3. Di dalam `urlpatterns` tambahkan baris berikut.

   ```
   urlpatterns = [
    ...
    path('', include('main.urls')),
    ...
   ]
   ```

### Checklist 4: Membuat Model pada Aplikasi `main` dengan atribut wajib `name`, `price`, `description`☑️
1. Buka berkas `models.py` pada aplikasi `main`, lalu isi dengan kode berikut.

   ```
   from django.db import models
   
   class AttributeEntry(models.Model):
       name = models.CharField(max_length=255)
       price = models.IntegerField()
       description = models.TextField()
   ```
2. Buat migrasi model dengan cara menjalankan perintah berikut di Terminal.

   `python manage.py makemigrations`
   
   Lalu, jalankan perintah berikut untuk menerapkan migrasi.

   `python manage.py migrate`

### Checklist 5: Membuat Fungsi pada `views.py`☑️
1. Buka berkas `views.py` pada aplikasi `main`, kemudian tambahkan baris berikut pada bagian `import`.

   `from django.shortcuts import render`
2. Tambahkan fungsi `show_main` di bawah `import`.

   ```
   def show_main(request):
    context = {
       'name': 'Abbey Road T-Shirt',
       'price': 'Rp 300.000',
       'description': 'The Beatles T-Shirt',
       'class': 'PBP D',
       'my_name': 'Muhammad Albyarto Ghazali',
    }

    return render(request, "main.html", context)
   ```

### Checklist 6:  Membuat sebuah _routing_ pada `urls.py` aplikasi `main`☑️
1. Buat berkas `urls.py` di dalam direktori `main`
2. Isi urls.py dengan kode:
```
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```


### Checklist 7: Deployment melalui PWS☑️
1. Buat proyek baru dengan menekan tombol Create New Project lalu masukkan nama proyeknya.
2. Simpan Project Credentials yang ditampilkan setelah membuat proyek baru
3. Pada `settings.py` di proyek Django yang sudah kamu buat tadi, tambahkan URL deployment PWS pada `ALLOWED_HOSTS`
```
...
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "muhammad-albyarto-abbeyroadstore.pbp.cs.ui.ac.id"]
...
```
4. Lakukan git add, commit, dan push
5. Jalankan perintah yang terdapat pada informasi Project Command pada halaman PWS.
6. Lihat status deployment di situs PWS. Jik statusnya SUDAH Running, maka proyek sudah bisa diakses pada URL deployment.
7. Tekan tombol View Project yang terdapat pada halaman proye
   
### Bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya
![Screenshot 2024-02-13 175909](https://github.com/FasiIkom/study-tracker/assets/158117087/627dbd25-7467-45df-be4c-302a208995e7)

### Kaitan antara urls.py, views.py, models.py, dan berkas html.
Permintaan untuk aplikasi web Django dikirim ke server oleh klien atau browser. Pertama, urls.py mengembalikan URL yang cocok dengan fungsi yang ditemukan di views.py. Permintaan diajukan di views.py dan, jika diperlukan, berinteraksi dengan models.py untuk mengambil atau mengekstrak data dari basis data. Setelah data diekstraksi dari views.py, template HTML (yang biasanya terletak di folder templates) dirender dan hasilnya dikirim kembali ke klien sebagai respons. Jadi untuk kaitannya, urls.py menangani permintaan, views.py menangani logika, models.py menangani data, dan berkas HTML menampilkan hasil kepada pengguna.

### Fungsi git dalam pengembangan perangkat lunak!
Git berfungsi sebagai sistem kontrol versi (VCS) yang memungkinkan pengembang perangkat lunak menangani setiap perubahan kode dengan adil dan konsisten. Git memungkinkan anggota tim pengembangan bekerja secara kolaboratif pada proyek bersama, membuat cabang unik untuk fitur baru, memperbaiki bug, dan menyelaraskan perubahan (merge) dengan etika. Selain itu, Git memungkinkan untuk kembali ke versi sebelumnya jika terjadi masalah, sehingga mengurangi risiko yang terkait dengan pengembangan perangkat lunak. Dengan kata lain, Git membantu menjaga integritas kode dan memastikan bahwa peserta dapat bekerja secara efektif dalam proyek yang kompleks.

### Mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Menurut saya, Django sering digunakan sebagai framework untuk pengembangan karena memiliki arsitektur yang terstruktur, yakni arsitektur Model-View-Template (MVT). Hal ini mempermudah pemula untuk memahami konsep dasar seperti routing, templating, dan manajemen basis data tanpa terhambat oleh kode yang rumit. Selain itu, dokumentasi yang ditulis dengan baik dan komunitas yang besar memudahkan pemula untuk menemukan sumber belajar dan solusi.

### Mengapa model pada Django disebut sebagai ORM?
Karena memungkinkan pemrograman berorientasi objek dalam basis data relasional, model Django terkadang dikenal sebagai ORM (Object-Relational Mapping). Dengan ORM, para programmer dapat membuat basis data menggunakan kode Python tanpa harus memasukkan kueri SQL secara manual. ORM memfasilitasi interaksi dengan basis data, membuat proses entri data menjadi lebih mudah dan memastikan bahwa kode tetap jelas dan mudah dipahami.



