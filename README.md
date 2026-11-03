# PA_4_Sistem_Rental_Konsol_Game

## Judul
RENT 4-BIT

## Tema
Sistem Rental Konsol Game

## Anggota & Peran
1. Muhammad Khaidir Ali Ramadhani (2609116015)  : Project Leader.
   
   Mengembangkan flowchart, merapikan kode program, merapikan penyusunan laporan.

2. Kayla Azzahra Tusyifa (2609116027)           : Anggota.

    Mengembangkan kode program, membuat konsep utama flowchart, merapikan penyusunan laporan.
   
3. Adnan Naufal Candra (2609116034)             : Anggota.

    Membuat konsep utama kode program, merapikan penyusunan laporan, merapikan flowchart
   
4. Naily Najwa Azahra (2609116040)              : Anggota.

    Menyusun laporan, merapikan kode program, merapikan flowchart

## Deskripsi 
RENT 4-BIT merupakan program sistem rental konsol game berbasis bahasa pemrograman Python yang dibuat untuk membantu proses pengelolaan penyewaan konsol game secara lebih terstruktur dan efisien. Program ini dijalankan melalui terminal dan menggunakan file CSV sebagai media penyimpanan data akun pengguna, daftar konsol, serta transaksi.

Program RENT 4-BIT memiliki dua jenis hak akses, yaitu Admin dan User. Admin memiliki akses untuk mengelola data konsol melalui fitur tambah, lihat, ubah, dan hapus data (CRUD), melihat seluruh transaksi penyewaan, serta mengakses laporan ringkas yang menampilkan total pendapatan, jumlah transaksi, dan produk terlaris.
Sementara itu, User dapat melakukan registrasi dan login, melihat daftar konsol, melakukan top up saldo e-money, menyewa konsol berdasarkan stok dan saldo yang tersedia, melihat riwayat transaksi, mencetak invoice, serta melakukan pengembalian konsol.

Program ini juga dilengkapi dengan validasi input, penanganan kesalahan, pencatatan waktu transaksi, dan pengelolaan stok secara otomatis untuk mendukung proses penyewaan.

## Tujuan
Tujuan pembuatan program RENT 4-BIT adalah sebagai berikut:

1. Membuat sistem rental konsol game menggunakan bahasa pemrograman Python untuk membantu pengelolaan penyewaan secara terstruktur.
2. Menerapkan fitur registrasi, login, serta pembagian hak akses antara Admin dan User.
3. Menerapkan konsep CRUD untuk mempermudah pengelolaan data konsol.
4. Mengimplementasikan penyimpanan dan pengolahan data menggunakan file CSV.
5. Menyediakan fitur top up e-money, penyewaan, pembayaran, dan pengembalian konsol.
6. Menyediakan fitur riwayat transaksi, pencetakan invoice, dan laporan ringkas.
7. Menerapkan konsep dasar pemrograman Python, seperti function, percabangan, perulangan, list, tuple, dictionary, dan set.









# **FLOWCHART SISTEM RENTAL KONSOL GAME**

**1. MENU UTAMA**

<img width="3256" height="5968" alt="FLOWCHARTPAKEL4-MENU UTAMA drawio" src="https://github.com/user-attachments/assets/a5a2d73e-acb4-4f4a-93b5-24e9c5e8a1a1" />

**1. Flowchart Menu Utama**

  Flowchart Menu Utama berfungsi untuk mengatur proses awal program rental konsol. Pada bagian ini, program menyiapkan data yang dibutuhkan, kemudian memberikan pilihan kepada pengguna untuk melakukan registrasi, login, atau keluar dari program.

**Proses Awal Program**
  Program memeriksa dan memuat data yang tersimpan dalam file JSON/CSV, jika file sudah tersedia, program membaca data yang ada, Namun jika file belum tersedia, user membuat file beserta data awal yang diperlukan dan Setelah data siap, program menampilkan Menu Utama, lalu pengguna memilih menu yang ingin dijalankan.

 **Opsi 1 — Registrasi**
  Pengguna memilih menu ``registrasi`` dan Program meminta pengguna memasukkan username dan password setelah itu Program memeriksa data yang dimasukkan. Jika data tidak sesuai, proses registrasi tidak dilanjutkan, namun jika data sesuai, program menyimpan akun baru dan pengguna dapat menggunakan akun tersebut untuk login. Fungsinya adalah Membantu pengguna membuat akun baru agar dapat menggunakan program rental konsol.

**Opsi 2 — Login**
  Pengguna memilih menu ``login`` lalu program meminta pengguna memasukkan username dan password, steelah itu program memeriksa apakah data akun sesuai dengan data yang tersimpan. Jika data salah, program menampilkan pesan bahwa login gagal, namun jika data benar, program memeriksa jenis akun pengguna. Jika akun merupakan Admin, program mengarahkan pengguna ke Menu Admin dan jika akun merupakan User, program mengarahkan pengguna ke Menu User. Fungsinya adalah memeriksa akun pengguna dan mengarahkan pengguna ke menu sesuai dengan jenis akunnya.

**Opsi 3 — Keluar**
  Pengguna memilih menu keluar. Program menampilkan pesan terima kasih lalu program mengakhiri proses dan berhenti berjalan.
   

**2. MENU ADMIN**

<img width="7944" height="5424" alt="FLOWCHARTPAKEL4-MENU ADMIN drawio" src="https://github.com/user-attachments/assets/f9a97b13-11e6-4e5e-9445-6098d2565b55" />

Flowchart Menu Admin berfungsi untuk mengatur kegiatan Admin dalam program rental konsol, seperti menambah, melihat, mengubah, dan menghapus data konsol, melihat transaksi, membuat laporan, serta logout.

**Opsi 1 — Tambah Konsol**
  Admin memilih menu ``tambah konsol``, kemudian program meminta admin memasukkan informasi konsol yang akan ditambahkan, seperti nama konsol, jenis, harga sewa, dan jumlah stok. Setelah semua data dimasukkan, program akan memeriksa kelengkapan data tersebut. Jika data sudah sesuai, program menyimpan data konsol baru ke dalam sistem.

**Opsi 2 — Lihat Konsol**
  Admin memilih menu ``lihat konsol``, kemudian program mengambil dan menampilkan seluruh data konsol yang tersimpan. Data yang ditampilkan dapat berupa nama konsol, jenis konsol, harga sewa, dan jumlah stok. Setelah data ditampilkan, admin dapat kembali ke menu utama Admin.

**Opsi 3 — Ubah Konsol**
  Admin memilih menu ``ubah konsol``, kemudian program menampilkan daftar konsol yang tersedia. Admin memilih konsol yang ingin diubah dan memasukkan informasi terbaru. Program kemudian memeriksa data tersebut dan menyimpan perubahan apabila data sudah sesuai.

**Opsi 4 — Hapus Konsol**
  Admin memilih menu ``hapus konsol``, kemudian program menampilkan daftar konsol yang tersedia. Admin memilih data konsol yang ingin dihapus. Program meminta konfirmasi penghapusan sebelum menghapus data tersebut dari sistem.

**Opsi 5 — Lihat Daftar Penyewaan dan Transaksi**
  Admin memilih menu ``daftar penyewaan dan transaksi``. Program kemudian mengambil data penyewaan serta transaksi yang tersimpan dan menampilkannya kepada admin. Melalui menu ini, admin dapat memantau aktivitas penyewaan yang dilakukan oleh pengguna.

**Opsi 6 — Laporan Ringkas**
  Admin memilih menu ``laporan ringkas``, kemudian program mengolah data penyewaan dan transaksi yang tersedia. Setelah proses pengolahan selesai, program menampilkan ringkasan laporan yang berisi informasi aktivitas rental konsol.

**Opsi 7 — Logout**
Admin memilih menu ``logout``, kemudian program mengakhiri sesi Admin dan mengarahkan pengguna kembali ke Menu Utama.


**3. MENU USER**

<img width="7460" height="6688" alt="FLOWCHARTPAKEL4-MENU USER drawio" src="https://github.com/user-attachments/assets/64d056d9-7c85-4337-97c5-a6afb8cdeffa" />

Flowchart Menu User berfungsi untuk memberikan akses kepada pengguna agar dapat melihat konsol, mengecek dan mengisi saldo, menyewa konsol, melihat riwayat penyewaan, mencetak invoice, serta mengembalikan konsol.

**Opsi 1 — Lihat Konsol**
  User memilih menu ``lihat konsol1``, kemudian program mengambil dan menampilkan daftar konsol yang tersedia. Informasi yang ditampilkan meliputi nama konsol, jenis, harga sewa, dan jumlah stok. Dengan demikian, pengguna dapat mengetahui konsol yang dapat disewa.

**Opsi 2 — Lihat dan Top Up Saldo**
  User memilih menu ``lihat dan top up saldo``. Program akan menampilkan jumlah saldo yang dimiliki pengguna. Jika pengguna ingin melakukan top up, program meminta pengguna memasukkan nominal saldo yang ingin ditambahkan. Setelah nominal dimasukkan, program memproses penambahan saldo dan menyimpan jumlah saldo terbaru.

**Opsi 3 — Sewa Konsol**
  User memilih menu ``sewa konsol``, kemudian program menampilkan daftar konsol yang tersedia. Pengguna memilih konsol yang ingin disewa dan memasukkan informasi penyewaan yang diperlukan. Program kemudian memeriksa ketersediaan stok dan kecukupan saldo pengguna. Jika seluruh persyaratan terpenuhi, program memproses penyewaan, mengurangi saldo sesuai biaya sewa, memperbarui stok konsol, dan menyimpan data transaksi.

**Opsi 4 — Riwayat Penyewaan**
  User memilih menu ``riwayat penyewaan``, kemudian program mengambil data penyewaan berdasarkan akun pengguna yang sedang login. Program menampilkan daftar riwayat penyewaan sehingga pengguna dapat melihat aktivitas penyewaan yang pernah dilakukan.

**Opsi 5 — Cetak Invoice**
  User memilih menu ``cetak invoice``, kemudian program menampilkan data transaksi penyewaan yang tersedia. Pengguna memilih transaksi yang ingin dicetak. Setelah itu, program membuat dan menampilkan invoice yang berisi informasi penyewaan dan rincian biaya transaksi.

**Opsi 6 — Pengembalian Konsol**
  User memilih menu ``pengembalian konsol``, kemudian program menampilkan data penyewaan yang masih berlangsung. Pengguna memilih konsol yang akan dikembalikan. Program memproses pengembalian, memperbarui status penyewaan, dan menyesuaikan jumlah stok konsol setelah pengembalian berhasil dilakukan.

**Opsi 7 — Logout**
User memilih menu ``logout``, kemudian program mengakhiri sesi pengguna dan mengarahkan pengguna kembali ke Menu Utama.

## Daftar Fitur per Role
Program RENT 4-BIT memiliki beberapa fitur yang dikelompokkan berdasarkan hak akses pengguna, yaitu Menu Utama, Admin, dan User. Setiap role memiliki fungsi dan hak akses yang berbeda sesuai kebutuhan sistem.

## A. Menu Utama 

Menu utama merupakan tampilan awal program yang digunakan pengguna untuk memilih layanan sebelum masuk ke dalam sistem. Terdapat tiga pilihan yang tersedia, yaitu:
