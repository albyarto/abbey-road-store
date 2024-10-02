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
### Mengakses keempat URL di poin 2 menggunakan Postman
1. FORMAT XML
![xml](https://github.com/user-attachments/assets/b6265130-6920-4da2-879a-7b65209de83b)
2. FORMAT JSON
![json](https://github.com/user-attachments/assets/7387f96e-9532-4721-b783-72d3e0051161)
3. FORMAT XML BY ID
![xml by id](https://github.com/user-attachments/assets/226b5246-b669-40d7-90ac-4bcc2905dbbd)
4. FORMAT JSON BY ID
![json by id](https://github.com/user-attachments/assets/1198cf6f-cc0e-40d7-84ac-2d9edd56a751)

---

## Tugas 4

### Apa perbedaan antara HttpResponseRedirect() dan redirect()?
`HttpResponseRedirect()` dan `redirect()` di Django keduanya digunakan untuk mengarahkan pengguna ke URL yang berbeda, tetapi ada perbedaan dalam cara penggunaannya. `HttpResponseRedirect()` adalah kelas yang memerlukan URL absolut sebagai argumen dan memberikan kontrol penuh atas respons HTTP, cocok untuk situasi di mana pengembang ingin memanipulasi header secara lebih rinci. Di sisi lain, `redirect()` adalah fungsi utilitas yang lebih fleksibel dan mudah digunakan. Fungsi ini dapat menerima URL, nama URL pattern, atau bahkan objek model, kemudian mengarahkan pengguna ke URL yang sesuai. `redirect()` sebenarnya merupakan pembungkus dari `HttpResponseRedirect()` dan banyak digunakan karena kesederhanaan dan fleksibilitasnya.

### Jelaskan cara kerja penghubungan model Product dengan User!
Dalam Django, penghubungan model `Product` dengan model `User` dilakukan menggunakan ForeignKey, yang merupakan tipe field yang memungkinkan kita untuk menyimpan referensi ke objek lain, dalam hal ini, pengguna. Ketika kita mendeklarasikan user = models.ForeignKey(User, on_delete=models.CASCADE), kita memastikan bahwa setiap entri product akan memiliki referensi ke pengguna yang membuatnya. Ini menciptakan relasi many-to-one, di mana satu pengguna bisa memiliki banyak entri product.

Contoh implementasi dari hubungan model Product Entry dengan User adalah sebagai berikut:
   ```
   ...
   class ProductEntry(models.Model):
      user = models.ForeignKey(User, on_delete=models.CASCADE)
       id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
       name = models.CharField(max_length=255)
       price = models.IntegerField()
      ...
   ```

### Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.
- Authentication
Authentication adalah proses untuk verifikasi data user. Pada umumnya, user diminta untuk memasukkan kredensial yang layak seperti username dan password
Implementasi pada Django: Pada Django, proses authentication dilakukan dalam fitur login. Setelah user memasukkan kredensial, Django akan memverifikasi apakah kredensial valid atau tidak.

- Authorization
Authorization adalah proses penentuan hak akses yang dapat dan tidak dapat dilakukan oleh seorang user dalam aplikasi. Hal ini berkaitan dengan pengaturan akses ke sumber daya tertentu
Implementasi pada Django: Setelah proses authentication, Django akan memverifikasi izin user untuk menentukan akses mereka ke berbagai bagian aplikasi. Hal ini diatur dengan menggunakan decorator, seperti @login_required.

Ketika pengguna login, Django pertama kali memverifikasi kredensial (autentikasi). Jika berhasil, Django menyimpan informasi sesi pengguna dalam cookie untuk mempertahankan status login. Selanjutnya, saat pengguna mengakses halaman atau fitur tertentu, Django memeriksa apakah pengguna memiliki izin yang diperlukan (otorisasi) untuk mengakses sumber daya tersebut.
Jadi secara keseluruhan, autentikasi memastikan siapa pengguna tersebut, sedangkan otorisasi memastikan apa yang boleh mereka lakukan di dalam aplikasi.

### Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?
- Django mengingat pengguna yang telah login dengan menggunakan **session cookies**. Saat pengguna berhasil login, Django membuat sesi unik untuk pengguna tersebut dan menyimpannya di server (bisa di database, file, atau cache). ID sesi ini kemudian disimpan di browser pengguna dalam bentuk cookie yang dikirim setiap kali pengguna mengunjungi halaman. Django menggunakan cookie ini untuk memverifikasi identitas pengguna pada setiap permintaan, memastikan bahwa pengguna yang sama terus dianggap "login" tanpa harus memverifikasi ulang kredensial di setiap permintaan.

- Cookies tidak hanya digunakan untuk mengingat sesi pengguna, tetapi juga bisa digunakan untuk menyimpan preferensi atau melacak aktivitas. Namun, tidak semua cookies aman digunakan. Agar terlindungi dari serangan, cookies harus dikonfigurasi dengan benar menggunakan fitur seperti Secure untuk memastikan cookie hanya dikirim melalui koneksi HTTPS, HttpOnly untuk mencegah akses oleh JavaScript, dan SameSite untuk membatasi pengiriman cookie lintas situs yang dapat mengurangi risiko serangan CSRF.
  
### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step.

### Checklist 1: Mengimplementasikan fungsi registrasi, login, dan logout☑️
1. Buka `views.py` pada direktori `main`. Tambahkan beberapa import berikut.
   ```
   #register
   from django.shortcuts import redirect
   from django.contrib.auth.forms import UserCreationForm
   from django.contrib import messages

   #login dan logout
   from django.contrib.auth import authenticate, login, logout
   ```
   Masih di berkas yang sama, buat fungsi `register`, `login`, dan `logout`.
   Fungsi register
   ```
   def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)
   ```
   Fungsi login
   ```
   def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main:show_main')
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)
   ```
   Fungsi logout
   ```
   def logout_user(request):
    logout(request)
    return redirect('main:login')
   ```
2. Buat berkas baru bernama `register.html` di direktori `templates`. Isilah dengan teks berikut.
   ```
   {% extends 'base.html' %}

   {% block meta %}
   <title>Register</title>
   {% endblock meta %}
   
   {% block content %}
   
   <div class="login">
     <h1>Register</h1>
   
     <form method="POST">
       {% csrf_token %}
       <table>
         {{ form.as_table }}
         <tr>
           <td></td>
           <td><input type="submit" name="submit" value="Daftar" /></td>
         </tr>
       </table>
     </form>
   
     {% if messages %}
     <ul>
       {% for message in messages %}
       <li>{{ message }}</li>
       {% endfor %}
     </ul>
     {% endif %}
   </div>
   
   {% endblock content %}
   ```
3. Buat berkas baru bernama `login.html` di direktori `templates`. Isilah dengan teks berikut.
   ```
   {% extends 'base.html' %}
   
   {% block meta %}
   <title>Login</title>
   {% endblock meta %}
   
   {% block content %}
   <div class="login">
     <h1>Login</h1>
   
     <form method="POST" action="">
       {% csrf_token %}
       <table>
         {{ form.as_table }}
         <tr>
           <td></td>
           <td><input class="btn login_btn" type="submit" value="Login" /></td>
         </tr>
       </table>
     </form>
   
     {% if messages %}
     <ul>
       {% for message in messages %}
       <li>{{ message }}</li>
       {% endfor %}
     </ul>
     {% endif %} Don't have an account yet?
     <a href="{% url 'main:register' %}">Register Now</a>
   </div>
   
   {% endblock content %}
   ```
4. Buat tombol logout dengan cara tambahkan teks berikut di berkas `main.html` pada direktori `templates` setelah bagian `add new progress`.
   ```
   <a href="{% url 'main:logout' %}">
      <button>Logout</button>
   </a>
   ```
5. Lakukan routing. Pada `urls.py` di direktori `main`, tambahkan import fungsi yang telah kita buat.
   ```
   from main.views import register, login_user, logout_user
   ```
   Masih di berkas yang sama, tambahkan beberapa baris berikut di urlpatterns.
   ```
   path('register/', register, name='register'),
   path('login/', login_user, name='login'),
   path('logout/', logout_user, name='logout'),
   ```
### Checklist 2: Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.☑️
1. Jalankan server, lalu buka `http://localhost:8000/` pada web browser.
2. Pada halaman login, klik `register now`, lalu buat dua buah akun.
3. Masuk dengan salah satu akun. Klik `add new progress` untuk menambah sebuah progress. Lakukan tiga kali untuk menambah tiga buah progress.
4. Lakukan hal yang sama pada akun lainnya.
   
### Checklist 3: Menghubungkan model Product dengan User☑️
1. Buka berkas `models.py` pada direktori `main`. Tambahkan import berikut.
   ```
   from django.contrib.auth.models import User
   ```
   Masih di berkas yang sama, di dalam `class Progress`, tambahkan baris berikut.
   ```
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   ```
2. Buka berkas `views.py` pada direktori `main`. Ubah fungsi `create_product_entry` menjadi seperti berikut ini.
   ```
   def create_product_entry(request):
       form = ProductEntryForm(request.POST, request.FILES)
   
       if form.is_valid() and request.method == "POST":
           product_entry = form.save(commit=False)
           product_entry.user = request.user
           form.save()
           return redirect('main:show_main')
   
       context = {'form': form}
       return render(request, "create_product_entry.html", context)
   ```
   Masih di berkas yang sama, ubah fungsi `show_main` menjadi seperti berikut ini.
   ```
   def show_main(request):
    product_entries = ProductEntry.objects.filter(user=request.user)

    context = {
        'app_name' : 'Abbey Road Co.',
        'class': 'PBP D',
        'my_name': 'Muhammad Albyarto Ghazali',
        'product_entries' : product_entries,
        'last_login': request.COOKIES['last_login'],
        'name': request.user.username,
    }

    return render(request, "main.html", context)
   ```
3. Lakukan migration dengan cara `py manage.py makemigrations` lalu `py manage.py migrate`
   
### Checklist 4: Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi.☑️
1. Buka berkas `views.py` pada direktori `main`. Tambahkan beberapa import berikut.
   ```
   import datetime
   from django.http import HttpResponseRedirect
   from django.urls import reverse
   ```
   Masih di berkas yang sama, pada fungsi `login_user`, ganti kode pada blok `if form.is_valid()` menjadi seperti berikut ini.
   ```
   if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response
   ```
   Masih di berkas yang sama, pada fungsi `show_main`, tambahkan baris berikut pada `context`.
   ```
   'last_login': request.COOKIES['last_login'],
   ```
   Masih di berkas yang sama, ubah fungsi `logout_user`.
   ```
   def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
   ```
2. Untuk menampilkan sesi terakhir login, tambahkan baris berikut setelah tombol logout.
   ```
   <h5>Sesi terakhir login: {{ last_login }}</h5>
   ```

---

## Tugas 5

### Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
Dalam CSS, ketika terdapat beberapa selector yang diterapkan pada elemen HTML, prioritas pengambilan selector ditentukan oleh tingkat spesifisitasnya. Urutan prioritas dimulai dari **inline style**, yang memiliki prioritas tertinggi karena langsung ditulis pada elemen menggunakan atribut `style`. Di bawahnya, **ID selector** memiliki spesifisitas yang lebih tinggi daripada selector lain, diikuti oleh **class selector**, **pseudo-class**, dan **attribute selector**, yang memiliki tingkat spesifisitas sedang. **Tag selector** dan **pseudo-elements** memiliki tingkat spesifisitas paling rendah. Jika beberapa selector memiliki tingkat spesifisitas yang sama, aturan yang didefinisikan **terakhir** dalam file CSS akan diterapkan. Misalnya, aturan dengan ID akan mengesampingkan aturan dengan class atau tag, dan jika beberapa aturan memiliki spesifisitas yang sama, maka aturan terakhir yang ditulis dalam CSS akan berlaku.

### Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!
Responsive design menjadi konsep yang sangat penting dalam pengembangan aplikasi web karena memungkinkan tampilan dan fungsionalitas website beradaptasi dengan baik di berbagai ukuran layar dan perangkat, mulai dari desktop hingga tablet dan smartphone. Dengan semakin beragamnya perangkat yang digunakan pengguna untuk mengakses situs web, responsive design memastikan pengalaman pengguna (user experience) yang konsisten, nyaman, dan optimal di semua platform. Tanpa responsive design, aplikasi web mungkin terlihat baik di layar desktop, tetapi bisa jadi tidak proporsional, sulit digunakan, atau tidak fungsional pada perangkat dengan layar yang lebih kecil.

Contoh aplikasi yang **sudah menerapkan responsive design** adalah **Twitter atau X**. Tampilan dan elemen-elemen UI (user interface) di Twitter secara otomatis beradaptasi dengan ukuran layar perangkat, seperti memperkecil atau menata ulang elemen pada perangkat mobile untuk tetap mudah digunakan. Sebaliknya, contoh aplikasi yang **belum menerapkan responsive design** adalah beberapa situs web **lama** yang dirancang untuk tampilan desktop saja, di mana ketika diakses dari perangkat mobile, elemen-elemen seperti teks, gambar, dan tombol mungkin tidak proporsional, sulit dibaca, atau bahkan meluber keluar dari layar, memaksa pengguna untuk melakukan zoom manual. 

Responsive design menjadi penting karena menjaga aksesibilitas dan kenyamanan penggunaan pada semua jenis perangkat, membantu meningkatkan engagement dan mempertahankan pengguna.

### Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
Margin, border, dan padding adalah tiga konsep penting dalam CSS yang digunakan untuk mengatur ruang dan penempatan elemen dalam layout. **Margin** adalah ruang di luar batas elemen yang menciptakan jarak antara elemen tersebut dan elemen lain di sekitarnya; margin tidak mempengaruhi ukuran elemen, tetapi mengubah posisinya. Margin dapat diterapkan secara individual untuk masing-masing sisi elemen atau sekaligus. **Border** adalah garis yang mengelilingi elemen dan dapat memiliki berbagai jenis, ketebalan, dan warna; border mempengaruhi ukuran total elemen karena ditambahkan ke dimensi elemen itu sendiri. Sementara itu, **padding** adalah ruang di dalam batas elemen, yang memberikan jarak antara isi elemen dan border; padding juga mempengaruhi ukuran total elemen, menciptakan ruang ekstra di dalam elemen agar konten tidak terlalu dekat dengan border. Ketiganya dapat digunakan secara bersamaan untuk menciptakan layout yang teratur. Contoh implementasinya adalah dengan mendefinisikan CSS seperti `.box { margin: 20px; border: 2px solid black; padding: 15px; }`, yang memberikan margin 20px dari elemen lain, border 2px hitam, dan padding 15px di dalam elemen tersebut.

### Jelaskan konsep flex box dan grid layout beserta kegunaannya!
**Flexbox** dan **Grid Layout** adalah dua sistem layout CSS yang dirancang untuk membantu pengembang web dalam menyusun elemen-elemen di halaman dengan lebih efisien dan responsif.

**- Flexbox**
**Flexbox** (Flexible Box Layout) adalah model layout satu dimensi yang memungkinkan pengaturan elemen dalam baris (row) atau kolom (column) secara fleksibel. Dengan menggunakan flexbox, elemen dapat tumbuh, menyusut, dan menyesuaikan ukuran mereka untuk mengisi ruang yang tersedia dalam kontainer. Flexbox sangat berguna untuk membuat desain yang responsif dan menyesuaikan elemen-elemen di dalam wadah, sehingga pengguna dapat mengatur jarak, penyelarasan, dan arah elemen dengan lebih mudah. Misalnya, flexbox sering digunakan untuk membuat navbar, kartu produk, atau elemen dalam form, di mana pengaturan elemen dalam satu baris atau kolom sangat diperlukan.

**- Grid Layout**
**Grid Layout** adalah model layout dua dimensi yang memungkinkan pengaturan elemen dalam bentuk baris dan kolom secara bersamaan. Dengan grid layout, pengembang dapat membagi halaman menjadi grid yang lebih kompleks dan menetapkan posisi elemen secara lebih terstruktur. Grid sangat berguna untuk membuat layout yang lebih rumit, seperti halaman berita, dashboard, atau desain yang memerlukan penempatan elemen dalam format yang teratur. Grid layout memberikan kontrol lebih besar atas posisi dan ukuran elemen dalam suatu area, memungkinkan penggunaan area grid yang tidak teratur dan kombinasi berbagai ukuran kolom dan baris.

**Kegunaan**
Kegunaan **flexbox** meliputi pembuatan layout yang fleksibel dan responsif dalam satu dimensi, sedangkan **grid layout** ideal untuk pengaturan elemen dalam dua dimensi, memungkinkan desain yang lebih terstruktur dan kompleks. Masing-masing memiliki kekuatan dan kegunaan tersendiri, dan dalam banyak kasus, pengembang web dapat menggunakan keduanya secara bersamaan untuk mencapai hasil yang diinginkan dalam pengembangan halaman web.

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step!
### Menambahkan Fitur _edit_ dan _delete_ untuk Masing-Masing _Item_
1. Di berkas `views.py` pada folder `main`, tambahkan fungsi `delete` dan `edit`.
   ```
   def delete_product(request, id):
      product = ProductEntry.objects.get(pk = id)
      product.delete()
      return HttpResponseRedirect(reverse('main:show_main'))
   ```
   ```
   def edit_product(request, id):
    product = ProductEntry.objects.get(pk = id)
    form = ProductEntryForm(request.POST or None, instance=progress)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_product.html", context)
   ```
2. Di folder yang sama, buka berkas `urls.py`, lalu import fungsi delete dan edit.
   ```
   from main.views import delete_product, edit_product
   ```
   Masih di berkas yang sama, tambahkan `path` berikut pada `urlpatterns`
   ```
   path('edit-product/<int:id>', edit_product, name='edit_product'),
   path('delete/<int:id>', delete_product, name='delete_product'),
   ```

### Melakukan kustomisasi pada halaman login, register, dan main
Untuk melakukan kusotmisasi, kita dapat menambahkan beberapa _style_ pada bagian-bagian yang ingin dikustomisasi. Seperti pada `abbey-road-store` ini, saya sudah mengkustomisasi daftar item menjadi menggunakan _card_, mengkustomisasi tombol, mengatur posisi teks, dan mengatur warna latar belakang _website_.
