## Tugas 2

### Tautan ke Project di PWS :
https://muhammad-albyarto-abbeyroadstore.pbp.cs.ui.ac.id

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

---

## Tugas 3
### Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Data delivery merupakan elemen penting yang memungkinkan komunikasi efektif antara berbagai komponen dalam sebuah platform. Dengan adanya mekanisme ini, informasi dapat dikirim dengan aman, cepat, dan efisien dari satu titik ke titik lainnya, baik antar server, klien, maupun aplikasi. Tanpa Data delivery, platform tidak akan dapat beroperasi secara optimal karena pertukaran informasi yang dibutuhkan untuk menjalankan berbagai tugas tidak dapat berjalan dengan lancar.

### Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Menurut saya sendiri, Keduanya, XML dan JSON, memiliki kegunaan masing-masing dan kelebihan tersendiri tergantung pada kebutuhan aplikasi atau sistem yang sedang dikembangkan.

Namun, secara umum memang JSON lebih disukai/populer dibandingkan XML untuk pengiriman data dalam pengembangan aplikasi modern.. Berikut alasannya:
- **Sederhana dan Ringkas**: JSON lebih mudah dibaca dan ditulis karena formatnya yang lebih ringkas. Ini mengurangi overhead data dan memudahkan debugging.
- **Kinerja Lebih Baik**: JSON sering kali lebih cepat dalam hal parsing dan pemrosesan karena formatnya yang lebih sederhana.
- **Kompatibilitas dengan JavaScript**: JSON secara alami terintegrasi dengan JavaScript, menjadikannya lebih mudah diimplementasikan dalam aplikasi web.

Meskipun XML memiliki fitur tambahan seperti skema validasi dan namespace, JSON lebih populer karena sifatnya yang lebih ringan dan mudah diimplementasikan, terutama dalam aplikasi web modern.
Namun pada akhirnya, pilihan antara XML dan JSON bergantung pada kebutuhan spesifik proyek Anda dan lingkungan di mana data tersebut akan digunakan.

### Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
Method is_valid() pada form Django digunakan untuk memeriksa apakah data yang dimasukkan oleh pengguna sesuai dengan aturan validasi yang telah ditentukan. Method ini mengevaluasi data yang di-submit, dan jika memenuhi kriteria validasi, akan mengembalikan True, memungkinkan data untuk diproses lebih lanjut, seperti disimpan ke dalam database. Sebaliknya, jika data tidak valid, is_valid() mengembalikan False dan memberikan pesan error yang relevan.

Tanpa method is_valid(), kita tidak dapat memastikan bahwa data yang dikirim aman dan sesuai dengan aturan yang telah ditetapkan, yang dapat mengakibatkan pelanggaran integritas data dan risiko keamanan aplikasi.

### Mengapa kita membutuhkan `csrf_token` saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan `csrf_token` pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
`csrf_token` itu sendiri digunakan untuk melindungi aplikasi web dari serangan CSRF (Cross-Site Request Forgery), di mana penyerang mencoba mengirimkan permintaan berbahaya ke server dengan menggunakan kredensial pengguna yang sudah terautentikasi.

Jika `csrf_token` tidak ditambahkan pada form di Django, penyerang dapat membuat skrip atau tautan yang secara otomatis mengirimkan permintaan ke server dengan memanfaatkan sesi aktif pengguna. Tanpa token ini, server tidak memiliki cara untuk memverifikasi apakah permintaan tersebut berasal dari sumber yang sah, sehingga memungkinkan penyerang melakukan tindakan berbahaya, seperti mengubah data atau melakukan transaksi atas nama pengguna tanpa sepengetahuannya.

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step.
### Checklist 1: Membuat input form untuk menambahkan objek model☑️
1. Buat berkas baru pada direktori `main` bernama `forms.py` dan isi dengan kode berikut.
   ```
   from django.forms import ModelForm
   from main.models import ProductEntry
   
   class ProductEntryForm(ModelForm):
       class Meta:
           model = ProductEntry
           fields = ["name", "price", "description"]
   ```
2. Buka berkas `views.py` pada direktori `main`.
   Tambahkan beberapa import berikut.
   ```
   from django.shortcuts import render, redirect
   from main.forms import ProductEntryForm
   from main.models import ProductEntry
   ```
   Tambahkan juga fungsi berikut.
   ```
   def create_product_entry(request):
    form = ProductEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product_entry.html", context)
    ```
   Masih di berkas yang sama, update fungsi show_main menjadi seperti berikut ini.
   ```
   def show_main(request):
   product_entries = ProductEntry.objects.all()
   
   context = {
      'class': 'PBP D',
      'my_name': 'Muhammad Albyarto Ghazali',
      'product_entries' : product_entries
   }

    return render(request, "main.html", context)
    ```
3. Buka berkas `urls.py` pada direktori `main`.
   Tambahkan import berikut.
   ```
   from main.views import show_main, create_product_entry
   ```
   Tambahkan `path('create-product-entry', create_product_entry, name='create_product_entry'),` ke `urlpatterns`.
   ```
   urlpatterns = [
      ...
      path('create-product-entry', create_product_entry, name='create_product_entry'),
   ]
   ```
4. Pada direktori `main/templates`, buat berkas HTML baru bernama `create_product_entry.html` dan isilah dengan kode berikut ini.
   ```
   {% extends 'base.html' %} 
   {% block content %}
   <h1>Add New Product Entry</h1>
   
   <form method="POST">
     {% csrf_token %}
     <table>
       {{ form.as_table }}
       <tr>
         <td></td>
         <td>
           <input type="submit" value="Add Product Entry" />
         </td>
       </tr>
     </table>
   </form>
   
   {% endblock %}
   ```
5. Pada direktori `main/templates`, buka berkas `main.html` dan tambahkan kode di dalam bagian `{% block content %}`.
   ```
   {% if not product_entries %}
    <p class="no-data">Belum ada data product pada Abbey Road Store.</p>
   {% else %}
    <table>
      <tr>
        <th>Product Name</th>
        <th>Price</th>
        <th>Description</th>
      </tr>
    
      {% for product_entry in product_entries %}
      <tr>
        <td>{{ product_entry.name }}</td>
        <td>{{ product_entry.price }}</td>
        <td>{{ product_entry.description }}</td>
      </tr>
      {% endfor %}
    </table>
   {% endif %}
   
   <br />
   
   <a href="{% url 'main:create_product_entry' %}">
    <button>Add New Product Entry</button>
   </a>
   ```
### Checklist 2: Menambahkan 4 fungsi views dalam format XML, JSON, XML by ID, dan JSON by ID.☑️
1. Buka `views.py` pada direktori `main` dan tambahkan import berikut.
   ```
   from django.http import HttpResponse
   from django.core import serializers
   ```
2. Untuk format XML, tambahkan fungsi berikut pada `views.py`.
   ```
   def show_xml(request):
       data = Progress.objects.all()
       return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
   ```
3. Untuk format JSON, tambahkan fungsi berikut pada `views.py`.
   ```
   def show_json(request):
       data = Progress.objects.all()
       return HttpResponse(serializers.serialize("json", data), content_type="application/json")
   ```
4. Untuk format XML by ID, tambahkan fungsi berikut pada `views.py`.
   ```
   def show_xml_by_id(request, id):
       data = Progress.objects.filter(pk=id)
       return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
   ```
5. Untuk format JSON by ID, tambahkan fungsi berikut pada `views.py`.
   ```
   def show_json_by_id(request, id):
      data = Progress.objects.filter(pk=id)
      return HttpResponse(serializers.serialize("json", data), content_type="application/json")
   ```
### Checklist 3: Membuat routing URL untuk masing-masing views yang telah ditambahkan ☑️
1. Buka berkas `urls.py`, lalu import 4 fungsi show yang telah kita buat.
   ```
   from main.views import show_main, create_progress, show_xml, show_json, show_xml_by_id, show_json_by_id
   ```
2. Tambahkan path untuk setiap fungsi di dalam `urlpatterns`.
   ```
   path('json/', show_json, name='show_json'),
   path('xml/', show_xml, name='show_xml'),
   path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
   path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
   ```
### Checklist 5: Mengakses keempat URL di poin 2 menggunakan Postman☑️

### Checklist 6: Melakukan add-commit-push ke GitHub.☑️
