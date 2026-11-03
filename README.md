# PA_4_Sistem_Rental_Konsol_Game

## JUDUL
RENT 4-BIT

## TEMA
Sistem Rental Konsol Game

## ANGGOTA & PERAN
**KELOMPOK 4 (4BIT)**
1. Muhammad Khaidir Ali Ramadhani (2609116015)  : Project Leader.
   
   Mengembangkan flowchart, merapikan kode program, merapikan penyusunan laporan.

2. Kayla Azzahra Tusyifa (2609116027)           : Anggota.

    Mengembangkan kode program, membuat konsep utama flowchart, merapikan penyusunan laporan.
   
3. Adnan Naufal Candra (2609116034)             : Anggota.

    Membuat konsep utama kode program, merapikan penyusunan laporan, merapikan flowchart
   
4. Naily Najwa Azahra (2609116040)              : Anggota.

    Menyusun laporan, merapikan kode program, merapikan flowchart

## DESKRIPSI
RENT 4-BIT merupakan program sistem rental konsol game berbasis bahasa pemrograman Python yang dibuat untuk membantu proses pengelolaan penyewaan konsol game secara lebih terstruktur dan efisien. Program ini dijalankan melalui terminal dan menggunakan file CSV sebagai media penyimpanan data akun pengguna, daftar konsol, serta transaksi.

Program RENT 4-BIT memiliki dua jenis hak akses, yaitu Admin dan User. Admin memiliki akses untuk mengelola data konsol melalui fitur tambah, lihat, ubah, dan hapus data (CRUD), melihat seluruh transaksi penyewaan, serta mengakses laporan ringkas yang menampilkan total pendapatan, jumlah transaksi, dan produk terlaris.
Sementara itu, User dapat melakukan registrasi dan login, melihat daftar konsol, melakukan top up saldo e-money, menyewa konsol berdasarkan stok dan saldo yang tersedia, melihat riwayat transaksi, mencetak invoice, serta melakukan pengembalian konsol.

Program ini juga dilengkapi dengan validasi input, penanganan kesalahan, pencatatan waktu transaksi, dan pengelolaan stok secara otomatis untuk mendukung proses penyewaan.

## TUJUAN
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

## DAFTAR FITUR PER ROLE
Program RENT 4-BIT memiliki beberapa fitur yang dikelompokkan berdasarkan hak akses pengguna, yaitu Menu Utama, Admin, dan User. Setiap role memiliki fungsi dan hak akses yang berbeda sesuai kebutuhan sistem.

## A. MENU UTAMA 
<img width="2383" height="1506" alt="E45C1BA1-FC83-4BC9-B553-C68717B3FC57_1_201_a" src="https://github.com/user-attachments/assets/1415f652-3bf4-4d25-beab-5eb6feb83093" />

Menu utama merupakan tampilan awal program yang digunakan pengguna untuk memilih layanan sebelum masuk ke dalam sistem. Terdapat tiga pilihan yang tersedia, yaitu: 1. Registrasi, 2. Login dan 3. Keluar. Program juga melakukan validasi pilihan agar input sesuai dengan menu dan menampilkan pesan apabila terjadi kesalahan saat memasukkan pilihan.

**1. Registrasi**
<img width="2358" height="1469" alt="5762F1FC-F872-4B43-A195-160E3530585D_1_201_a" src="https://github.com/user-attachments/assets/2f338ba7-c3a1-4881-9c5f-cd966eb5d380" />
<img width="2394" height="533" alt="85E2C56F-127A-49EC-A1BE-BBB1ECABD6C9_1_201_a" src="https://github.com/user-attachments/assets/ccc1a8f7-32fd-4918-b35f-75eb85603f52" />
Fitur registrasi digunakan oleh pengguna baru untuk membuat akun dengan role User, agar dapat mengakses program RENT 4-BIT. Pengguna diminta memasukkan username dan password dengan ketentuan username minimal 4 karakter dan belum digunakan oleh pengguna lain. Program juga melakukan validasi untuk memastikan username tidak terdaftar sebelumnya.
Setelah data berhasil dimasukkan, akun baru akan disimpan ke dalam file ``user.csv`` dengan hak akses sebagai User dan saldo awal sebesar Rp0. Jika proses penyimpanan berhasil, program akan menampilkan pesan bahwa registrasi berhasil dan pengguna dapat melanjutkan ke proses login.

**2. Login**
<img width="2381" height="1492" alt="8CE97C9A-3FA6-45BB-BD84-A0C5AA8AE159_1_201_a" src="https://github.com/user-attachments/assets/060ed2c3-5be1-4018-b86e-fd285a0a8347" />
<img width="2386" height="333" alt="5BF03622-A2E5-47DA-B4EA-59DBC8798069_1_201_a" src="https://github.com/user-attachments/assets/8dd62b3f-10f5-42b6-970b-6258a4cfe353" />
Fitur login digunakan pengguna untuk masuk ke program RENT 4-BIT dengan memasukkan username dan password yang telah didaftarkan. Program akan memeriksa kesesuaian data akun dengan data yang tersimpan dalam file user.csv. Pengguna diberikan maksimal 3 kali kesempatan untuk melakukan login. Jika berhasil, program akan menentukan role atau hak akses pengguna berdasarkan akun yang digunakan, yaitu Admin atau User. Selanjutnya, pengguna akan diarahkan ke menu sesuai dengan role tersebut. Jika data yang dimasukkan salah, program akan menampilkan pesan kesalahan dan sisa kesempatan login.

**3. Keluar**
<img width="2414" height="182" alt="B03D33BC-1CB8-4DB8-968E-5953F6076CE1_1_201_a" src="https://github.com/user-attachments/assets/5193b78a-4f1b-42bf-8a34-f1d342c01f61" />
Fitur keluar digunakan untuk mengakhiri program RENT 4-BIT. Ketika pengguna memilih menu nomor 3, program akan menampilkan pesan "Terima kasih telah menggunakan RENT 4-BIT." Setelah itu, program akan berhenti dijalankan.

## B. MENU ADMIN
<img width="2396" height="1488" alt="8968112D-EE8C-4ED2-BF8E-62969C04454B_1_201_a" src="https://github.com/user-attachments/assets/cad8f4cf-9db2-450d-b24a-471c4ad56021" />
<img width="2384" height="360" alt="6FE681E9-1423-4E90-9915-9ADCAB2175D8_1_201_a" src="https://github.com/user-attachments/assets/49d6f31b-0421-4907-96ae-8cd0c8b5d967" />
Menu Admin hanya satu satunya dengan username : *admin* dan password : *admin123*. Pada menu admin tersedia berbagai pilihan fitur khusus untuk pengelola rental konsol game. Pada menu ini terdapat tujuh pilihan, yaitu tambah konsol, lihat konsol, ubah konsol, hapus konsol, lihat penyewaan dan transaksi, laporan ringkas, serta logout. Admin dapat memilih fitur sesuai kebutuhan dengan memasukkan nomor menu yang tersedia. Program juga melakukan validasi pilihan agar input sesuai dengan menu dan menampilkan pesan apabila terjadi kesalahan saat memasukkan pilihan.

**1. Tambah Konsol**
<img width="2370" height="1545" alt="D277FF22-CA61-4469-B45D-D08F2F90307F_1_201_a" src="https://github.com/user-attachments/assets/dd4e7ba4-ff9a-447e-ac73-0d19474bbfaf" />
<img width="2400" height="1481" alt="3D356E93-32D6-40E2-B894-CFB5B6C9FC98_1_201_a" src="https://github.com/user-attachments/assets/c6186025-694b-4b14-a312-8c3ad5b8b33b" />
<img width="2407" height="182" alt="DC3C8261-5F2F-4E76-AD92-8F63652BF818_1_201_a" src="https://github.com/user-attachments/assets/ca424e05-a93a-458c-a31a-8de4fab7676b" />
Fitur tambah konsol digunakan Admin untuk memasukkan data konsol baru ke dalam sistem. Admin mengisi kode konsol, nama, merek, harga sewa per jam, dan jumlah stok. Program akan memeriksa agar kode konsol tidak sama dengan data yang sudah ada, harga harus lebih dari nol, dan stok tidak boleh bernilai negatif. Setelah semua data diisi, Admin dapat mengonfirmasi penyimpanan. Jika disetujui, data konsol akan ditambahkan dan disimpan ke dalam file ``DaftarKonsol.csv.``

**2. Lihat Konsol**
<img width="2391" height="1114" alt="A421B33C-C2D7-466A-9802-FBFCF01A82BF_1_201_a" src="https://github.com/user-attachments/assets/82e4b65b-7257-4057-98f6-98dfc797d6ed" />
Fitur lihat konsol digunakan Admin untuk menampilkan seluruh data konsol yang tersimpan dalam file ``DaftarKonsol.csv.`` Informasi yang ditampilkan meliputi kode konsol, nama, merek, harga sewa per jam, dan stok yang tersedia. Data tersebut ditampilkan dalam bentuk tabel menggunakan library ``PrettyTable`` agar lebih rapi dan mudah dibaca. Jika belum terdapat data konsol, program akan menampilkan pesan belum ada data konsol.

**3. Ubah Konsol**
<img width="2406" height="1477" alt="3B6E24FF-FA34-49C5-A276-B55285F7C13D_1_201_a" src="https://github.com/user-attachments/assets/32ec3d8a-201e-4b16-bc55-d8abf6ae88e3" />
<img width="2392" height="1412" alt="CE4D17B8-E0EB-48E5-9797-F042D8456873_1_201_a" src="https://github.com/user-attachments/assets/6070d2af-ccd0-43e0-bcc0-54568c36e1e8" />
<img width="2406" height="1490" alt="82F468BD-E3B0-4204-B4BE-C95010C864FA_1_201_a" src="https://github.com/user-attachments/assets/025e5097-92b7-41d0-8213-45aff1e90fd6" />
<img width="2388" height="537" alt="184690C9-0949-4C24-B69F-70020D94247D_1_201_a" src="https://github.com/user-attachments/assets/4f1cff8c-07ee-4c1f-b5d4-c618557a027b" />
Fitur ubah konsol digunakan Admin untuk memperbarui data konsol yang sudah tersimpan dalam file ``DaftarKonsol.csv.`` Sebelum melakukan perubahan, Admin diminta memasukkan kode konsol yang ingin diubah. Program akan mencari data berdasarkan kode tersebut dan menampilkan daftar konsol sebagai referensi. Admin dapat mengubah nama, merek, harga sewa per jam, dan menambahkan stok konsol. Jika terdapat bagian yang tidak ingin diubah, Admin dapat membiarkannya atau menekan Enter. Program juga melakukan validasi agar harga lebih dari nol dan stok tidak bernilai negatif. Setelah selesai, Admin dapat mengonfirmasi penyimpanan perubahan. Jika disetujui, data terbaru akan disimpan kembali ke dalam file ``DaftarKonsol.csv.``

**4. Hapus Konsol**
<img width="2401" height="1504" alt="DA26E439-6C31-44EB-A60E-B1136A006156_1_201_a" src="https://github.com/user-attachments/assets/bd8feac6-f7c4-4a0a-8b8f-bb13315ab82f" />
<img width="2401" height="854" alt="FF0BD8CA-6FE6-40BD-9AA4-25EC5E7EAA81_1_201_a" src="https://github.com/user-attachments/assets/eeeb3e60-f3b2-4804-9cc5-4332adbe31b9" />
Fitur hapus konsol digunakan Admin untuk menghapus data konsol dari sistem. Admin terlebih dahulu melihat daftar konsol, kemudian memasukkan kode konsol yang ingin dihapus. Program akan mencari data konsol berdasarkan kode tersebut. Konsol hanya bisa dihapus jika jumlah stoknya sudah 0. Sebelum menghapus, program akan meminta konfirmasi kepada Admin. Jika Admin menyetujui, data konsol akan dihapus dan perubahan disimpan ke dalam file ``DaftarKonsol.csv.``

**5. Lihat Penyewaan dan Transaksi**
<img width="2389" height="1445" alt="9B59B4CC-3407-4CE1-BF05-1BE5E68DDC3D_1_201_a" src="https://github.com/user-attachments/assets/0b2a0f99-1940-4621-91f0-604cd5d67b79" />
<img width="2391" height="133" alt="7173E5DF-2664-4CB6-AC79-79305CCF04C7_1_201_a" src="https://github.com/user-attachments/assets/a48d390e-a669-4039-a879-0ca8b6c3d4ab" />
Fitur ini digunakan Admin untuk melihat seluruh data penyewaan dan transaksi yang dilakukan oleh pengguna. Data diambil dari file ``Transaksi.csv`` dan ditampilkan dalam bentuk tabel menggunakan library ``PrettyTable`` agar lebih mudah dibaca. Informasi yang ditampilkan meliputi ID transaksi, username, jenis transaksi, kode konsol, nama konsol, durasi penyewaan, jumlah, total pembayaran, dan waktu transaksi. Jika belum ada transaksi yang tercatat, program akan menampilkan pesan bahwa belum ada transaksi.

**6. Laporan Ringkas**
<img width="2405" height="1467" alt="FB20BC5C-56D9-4CA1-8098-E0BD784278DA_1_201_a" src="https://github.com/user-attachments/assets/fe579afa-5764-485e-913b-272bc07f0486" />
<img width="2388" height="1368" alt="96D2FDD0-3B60-4DBB-AA69-9011AED85D7A_1_201_a" src="https://github.com/user-attachments/assets/3e2dea5b-0c2c-4bb8-bc54-71e4996c4773" />
Fitur laporan ringkas digunakan Admin untuk melihat rangkuman hasil penyewaan konsol. Data diambil dari file ``Transaksi.csv``, kemudian program menghitung total pendapatan dan jumlah transaksi penyewaan. Selain itu, program juga menentukan produk atau konsol yang paling laris berdasarkan jumlah unit yang disewa. Informasi yang ditampilkan meliputi total pendapatan, jumlah transaksi, produk terlaris, total unit yang disewa, dan frekuensi penyewaan. Dengan fitur ini, Admin dapat mengetahui gambaran aktivitas penyewaan yang terjadi dalam sistem.

**7. Logout**
<img width="2409" height="184" alt="4CAAD56D-AC89-49CF-836E-FDB2882FE522_1_201_a" src="https://github.com/user-attachments/assets/2ebd8c1d-edb6-46eb-a7bd-afd9ee06102f" />
Fitur logout digunakan Admin untuk keluar dari akun yang sedang digunakan dan mengakhiri sesi sebagai Admin. Ketika Admin memilih menu nomor 7, program akan menampilkan pesan "Logout berhasil." Setelah itu, pengguna akan diarahkan kembali ke menu utama sehingga dapat keluar dari akun Admin.

## C. MENU USER
<img width="2412" height="1513" alt="D12FD678-2B4A-40BA-858B-0D244FB44827_1_201_a" src="https://github.com/user-attachments/assets/3a9eaa35-0867-40fe-be59-3feb9924aee0" />
<img width="2411" height="772" alt="C7231AFA-94E5-4B86-B166-0371491D49F9_1_201_a" src="https://github.com/user-attachments/assets/f7337f23-4ffc-432e-920c-910b02668705" />
Menu User menyediakan berbagai pilihan fitur bagi pengguna yang ingin menyewa konsol. Pada bagian atas menu, program menampilkan username dan saldo e-money yang dimiliki. Terdapat tujuh pilihan fitur, yaitu lihat daftar konsol, top up e-money, sewa konsol, riwayat transaksi, cetak invoice, pengembalian konsol, dan logout. User dapat memilih fitur dengan memasukkan nomor menu yang tersedia. Program juga dilengkapi validasi input untuk memastikan pilihan berada pada angka 1 sampai 7. Jika pengguna memasukkan pilihan yang tidak sesuai, program akan menampilkan pesan kesalahan.

**1. Lihat Daftar Konsol**
<img width="2405" height="1114" alt="216D35DA-AE77-48DB-9910-E9C1229C1744_1_201_a" src="https://github.com/user-attachments/assets/dc79d765-4fe5-49a2-9dea-5ed88419e51e" />
Fitur lihat daftar konsol digunakan User untuk melihat konsol yang tersedia untuk disewa. Data konsol diambil dari file ``DaftarKonsol.csv`` dan ditampilkan dalam bentuk tabel menggunakan library ``PrettyTable`` agar lebih mudah dibaca. Informasi yang ditampilkan meliputi kode konsol, nama, merek, harga sewa per jam, dan jumlah stok yang tersedia. Jika belum ada data konsol, program akan menampilkan pesan bahwa data konsol belum tersedia.

**2. Top up E-Money**
<img width="2381" height="1420" alt="4BC28B3D-55B3-48F9-A149-301EE42431CA_1_201_a" src="https://github.com/user-attachments/assets/09b01699-d211-4688-a21e-cb9c88bdde58" />
<img width="2396" height="1442" alt="66E2E48B-69C4-4A95-85A5-CAFF5725AC84_1_201_a" src="https://github.com/user-attachments/assets/80808979-8b58-4284-8661-fdf053d5c00b" />
<img width="2425" height="1147" alt="F354E21C-4181-4061-8E27-3511964F8E6E_1_201_a" src="https://github.com/user-attachments/assets/abeada97-e961-4938-9cdc-8b883284cb5c" />
Fitur Top Up E-Money digunakan User untuk mengisi atau menambahkan saldo ke akun. Pada bagian ini, program menetapkan batas minimal top up sebesar Rp5.000 dan maksimal Rp2.000.000 dalam satu kali pengisian. User diminta memasukkan nominal top up. Jika nominal yang dimasukkan tidak sesuai dengan batas tersebut atau bukan berupa angka, program akan menampilkan pesan dan memberikan pilihan untuk memasukkan nominal kembali. Jika User memasukkan angka 0, proses top up akan dibatalkan.

Setelah nominal sesuai, program mengambil data akun dari file user.csv dan mencari akun berdasarkan username User yang sedang login. Selanjutnya, saldo akan ditambahkan sesuai nominal yang dimasukkan. Program juga membuat ID transaksi dan mencatat aktivitas top up ke dalam file ``Transaksi.csv``. Setelah itu, perubahan saldo disimpan kembali ke ``user.csv``. Terakhir, program menampilkan informasi bahwa top up berhasil, ID transaksi, nominal top up, dan jumlah saldo terbaru.

**3. Sewa Konsol**
<img width="2390" height="1504" alt="6D9AA31A-D2CD-4EB6-999E-DCBB73706EBB_1_201_a" src="https://github.com/user-attachments/assets/9ded4634-9b38-4c33-b106-1560a1752273" />
<img width="2401" height="1484" alt="0BCA82A4-7BA1-451C-947A-33F6B6343AE6_1_201_a" src="https://github.com/user-attachments/assets/6f13703e-b900-4813-ac8c-8f4bbe1d928d" />
<img width="2408" height="1351" alt="7E12BE12-50E1-4600-B739-C80215EF4345_1_201_a" src="https://github.com/user-attachments/assets/d67414ec-a5c4-486b-871d-aec5ac25bf11" />
<img width="2397" height="1388" alt="82C2865C-080A-4BBA-8ED8-31AF7B5AA048_1_201_a" src="https://github.com/user-attachments/assets/b2546921-ae42-431d-b03f-0dfea12ccde6" />
<img width="2409" height="1510" alt="A41DABC3-1F78-403D-98E5-737DA3266390_1_201_a" src="https://github.com/user-attachments/assets/4b5532e0-e0c4-4125-b057-5612599f13be" />
<img width="2406" height="1518" alt="DC4344E1-05A3-4717-8027-377ED4BC99CE_1_201_a" src="https://github.com/user-attachments/assets/9af59e7d-a664-40d3-86c7-6c21d905a1c3" />
<img width="2418" height="1097" alt="2983CFB2-9889-47BC-B40E-A59027AE4AC2_1_201_a" src="https://github.com/user-attachments/assets/39af2bd5-5d99-4556-baf9-1ef3088f368a" />
Fitur Sewa Konsol digunakan User untuk menyewa konsol game yang tersedia. Pada awal proses, program mengambil data konsol dari file ``DaftarKonsol.csv`` dan menampilkan daftar konsol beserta harga dan stok yang tersedia.User kemudian memasukkan kode konsol yang ingin disewa. Program akan memeriksa apakah kode tersebut tersedia dan apakah stok konsol masih mencukupi. Jika kode tidak ditemukan atau stok habis, program akan menampilkan pesan dan meminta User memilih kembali.

Selanjutnya, User memasukkan durasi penyewaan dalam jam dan jumlah konsol yang ingin disewa. Program memastikan durasi dan jumlah konsol lebih dari 0 serta tidak melebihi stok yang tersedia. Setelah itu, program menghitung total biaya berdasarkan harga sewa per jam, durasi, dan jumlah konsol. Jika User ingin menyewa lebih dari satu jenis konsol, program memberikan pilihan untuk menambahkan konsol lainnya.

Setelah semua pilihan selesai, program menampilkan ringkasan penyewaan menggunakan tabel PrettyTable yang berisi kode konsol, nama konsol, harga per jam, durasi, jumlah, dan subtotal. Program juga menampilkan total pembayaran dan saldo User. Jika saldo mencukupi dan User menyetujui penyewaan, program akan mengurangi saldo sesuai total pembayaran, memperbarui stok konsol, membuat ID transaksi, serta menyimpan data penyewaan ke dalam file ``Transaksi.csv``. Terakhir, program menampilkan informasi bahwa penyewaan berhasil beserta ID transaksi, total pembayaran, dan sisa saldo User.

**4. Riwayat Transaksi**
<img width="2416" height="1492" alt="CC8F9E6E-0BCF-4770-9ACC-41E5E97C10B3_1_201_a" src="https://github.com/user-attachments/assets/4f379862-7639-497b-bca1-4a5c7c908be9" />
<img width="2412" height="272" alt="0974039F-4343-4A08-AEC4-AC8688DF7497_1_201_a" src="https://github.com/user-attachments/assets/d1b095d1-0547-4962-899c-7035e41742de" />
Fitur Riwayat Transaksi digunakan untuk menampilkan catatan transaksi yang pernah dilakukan oleh User. Pada awal proses, program mengambil data transaksi dari file ``Transaksi.csv``.
Selanjutnya, program melakukan penyaringan data berdasarkan username yang sedang login. Dengan demikian, User hanya dapat melihat riwayat transaksi miliknya sendiri dan tidak dapat melihat transaksi pengguna lain.

Jika belum terdapat transaksi, program akan menampilkan pesan bahwa belum ada riwayat transaksi. Apabila terdapat transaksi, program menampilkan data menggunakan tabel ``PrettyTable`` yang berisi ID transaksi, jenis transaksi, kode konsol, nama konsol, durasi, jumlah, total pembayaran, dan waktu transaksi. Dengan adanya fitur ini, User dapat melihat kembali seluruh aktivitas transaksi yang pernah dilakukan sehingga informasi penyewaan dan pembayaran dapat diketahui dengan lebih mudah.

**5. Cetak Invoice**
<img width="2404" height="1518" alt="6527057D-E58B-41DB-94A8-488CA290DEAB_1_201_a" src="https://github.com/user-attachments/assets/3a034dff-f6f0-43fb-9855-b91566909578" />
<img width="2394" height="1147" alt="2FD37007-DB20-462D-A625-3C6A1680A036_1_201_a" src="https://github.com/user-attachments/assets/f41ea535-3047-4802-83ce-2a3b52b69339" />
<img width="2429" height="1160" alt="A2F7D949-B7AC-4BC3-8FF8-7228A49F5C7E_1_201_a" src="https://github.com/user-attachments/assets/a05d54dc-74fb-43ff-85bc-59f792a8b0da" />
Fitur Cetak Invoice digunakan untuk menampilkan bukti transaksi yang telah dilakukan oleh User. Pada awal proses, program mengambil data transaksi dari file ``Transaksi.csv``, kemudian menyaring data berdasarkan username yang sedang login agar User hanya dapat melihat transaksi miliknya sendiri. Jika belum terdapat riwayat transaksi, program akan menampilkan pesan bahwa belum ada transaksi. Apabila terdapat transaksi, program akan mengelompokkan data berdasarkan ID transaksi agar setiap transaksi hanya ditampilkan satu kali pada daftar pilihan. Selanjutnya, program menampilkan daftar transaksi menggunakan tabel ``PrettyTable`` yang berisi nomor, ID transaksi, jenis transaksi, waktu, dan total pembayaran.

User kemudian memilih nomor transaksi yang ingin dicetak. Program akan memeriksa apakah nomor yang dimasukkan valid. Setelah itu, program mengambil rincian transaksi berdasarkan ID transaksi yang dipilih. Invoice kemudian ditampilkan dengan informasi berupa ID transaksi, username, jenis transaksi, waktu transaksi, kode konsol, nama konsol, durasi, jumlah, subtotal, dan total transaksi. Dengan adanya fitur ini, User dapat melihat bukti pembayaran secara lebih rinci sehingga transaksi yang telah dilakukan dapat diperiksa kembali.

**6. Pengembalian Konsol**
<img width="2403" height="1529" alt="D911F768-837B-48E8-9CAB-E33DE4087930_1_201_a" src="https://github.com/user-attachments/assets/c07da4bc-32aa-4ddd-9e1c-432d7ecfd196" />
<img width="2396" height="1513" alt="EE01D645-1524-4303-8608-273EFA5772E2_1_201_a" src="https://github.com/user-attachments/assets/58e5c825-f2cc-4549-b761-3f35df4deca8" />
<img width="2414" height="1518" alt="E4215A12-CCF2-45F7-8ABE-0A9A1355FD36_1_201_a" src="https://github.com/user-attachments/assets/4cdafb7b-50a7-4e88-aa02-395d4dfa7b26" />
<img width="2395" height="542" alt="E54E23E4-0E7A-4CB0-8AFB-D8C6CDDBC16C_1_201_a" src="https://github.com/user-attachments/assets/eaf00c2e-fca1-4668-91f1-3c90fe072fb7" />
Fitur Pengembalian Konsol digunakan untuk memproses pengembalian konsol yang telah disewa oleh User. Pada awal proses, program mengambil data dari file ``Transaksi.csv`` dan ``DaftarKonsol.csv``, kemudian menyaring transaksi berdasarkan username yang sedang login, jenis transaksi penyewaan, serta jumlah konsol yang belum dikembalikan. Jika tidak terdapat konsol yang perlu dikembalikan, program akan menampilkan pesan bahwa tidak ada konsol yang perlu dikembalikan. Apabila terdapat penyewaan , program menampilkan daftar konsol menggunakan ``PrettyTable`` yang berisi nomor, kode, nama konsol, jumlah sewa, jumlah yang sudah dikembalikan, dan jumlah yang belum dikembalikan.

Selanjutnya, User memilih nomor konsol yang ingin dikembalikan dan memasukkan jumlah konsol yang akan dikembalikan. Program melakukan validasi terhadap nomor pilihan dan jumlah pengembalian jika user menyewa lebih dari 1 konsol. Setelah User melakukan konfirmasi, program memperbarui jumlah konsol yang telah dikembalikan pada ``Transaksi.csv`` dan menambahkan kembali stok konsol pada ``DaftarKonsol.csv``. Jika seluruh proses berhasil, program menampilkan pesan bahwa pengembalian berhasil dicatat beserta nama konsol dan jumlah yang dikembalikan. 

**7. Logout**
<img width="2412" height="191" alt="B8A958A6-1B2D-471C-A278-5849D5A30EAC_1_201_a" src="https://github.com/user-attachments/assets/aa0767f8-f27a-474b-be65-5209074d8fc2" />
Fitur logout digunakan user untuk keluar dari akun yang sedang digunakan dan mengakhiri sesi sebagai user. Ketika user memilih menu nomor 7, program akan menampilkan pesan "Logout berhasil." Setelah itu, pengguna akan diarahkan kembali ke menu utama sehingga dapat keluar dari akun user.

## OUTPUT DAN PENJELASAN
