# PA_4_Sistem_Rental_Konsol_Game















# **FLOWCHART SISTEM RENTAL KONSOL GAME**

**1. MENU UTAMA**

<img width="3256" height="5968" alt="FLOWCHARTPAKEL4-MENU UTAMA drawio" src="https://github.com/user-attachments/assets/a5a2d73e-acb4-4f4a-93b5-24e9c5e8a1a1" />

**1. Flowchart Menu Utama**

Flowchart Menu Utama berfungsi untuk mengatur proses awal program rental konsol. Pada bagian ini, program menyiapkan data yang dibutuhkan, kemudian memberikan pilihan kepada pengguna untuk melakukan registrasi, login, atau keluar dari program.

**Proses Awal Program**
1. Program memeriksa dan memuat data yang tersimpan dalam file JSON/CSV.
2. Jika file sudah tersedia, program membaca data yang ada.
3. Jika file belum tersedia, program membuat file beserta data awal yang diperlukan.
4. Setelah data siap, program menampilkan Menu Utama.
5. Pengguna memilih menu yang ingin dijalankan.

 **Opsi 1 — Registrasi**
1. Pengguna memilih menu registrasi.
2. Program meminta pengguna memasukkan username dan password.
3. Program memeriksa data yang dimasukkan.
4. Jika data tidak sesuai, proses registrasi tidak dilanjutkan.
5. Jika data sesuai, program menyimpan akun baru.
6. Pengguna dapat menggunakan akun tersebut untuk login.

**Fungsi:** Membantu pengguna membuat akun baru agar dapat menggunakan program rental konsol.

**Opsi 2 — Login**
1. Pengguna memilih menu login.
2. Program meminta pengguna memasukkan username dan password.
3. Program memeriksa apakah data akun sesuai dengan data yang tersimpan.
4. Jika data salah, program menampilkan pesan bahwa login gagal.
5. Jika data benar, program memeriksa jenis akun pengguna.
6. Jika akun merupakan Admin, program mengarahkan pengguna ke Menu Admin.
7. Jika akun merupakan User, program mengarahkan pengguna ke Menu User.

**Fungsi:** Memeriksa akun pengguna dan mengarahkan pengguna ke menu sesuai dengan jenis akunnya.

**Opsi 3 — Keluar**
1. Pengguna memilih menu keluar.
2. Program menampilkan pesan terima kasih.
3. Program mengakhiri proses dan berhenti berjalan.

**Fungsi:** Mengakhiri program ketika pengguna tidak ingin menggunakannya lagi.



**2. MENU ADMIN**

<img width="7944" height="5424" alt="FLOWCHARTPAKEL4-MENU ADMIN drawio" src="https://github.com/user-attachments/assets/f9a97b13-11e6-4e5e-9445-6098d2565b55" />

Flowchart Menu Admin berfungsi untuk mengatur kegiatan Admin dalam program rental konsol, seperti menambah, melihat, mengubah, dan menghapus data konsol, melihat transaksi, membuat laporan, serta logout.

**Opsi 1 — Tambah Konsol**
1. Admin memilih menu tambah konsol.
2. Program meminta Admin memasukkan data konsol baru.
3. Program memeriksa apakah data yang dimasukkan sudah benar.
4. Jika data tidak sesuai, proses penambahan tidak dilanjutkan.
5. Jika data benar, program menyimpan data konsol.
6. Data konsol baru berhasil ditambahkan.

**Fungsi:** Menambahkan data konsol baru ke dalam program rental.

**Opsi 2 — Lihat Konsol**
1. Admin memilih menu lihat konsol.
2. Program memeriksa data konsol yang tersimpan.
3. Jika belum ada data konsol, program menampilkan pesan bahwa data masih kosong.
4. Jika data tersedia, program menampilkan daftar konsol.
5. Admin dapat melihat informasi konsol yang tersedia.

**Fungsi:** Melihat daftar konsol yang sudah terdaftar dalam program.

**Opsi 3 — Ubah Konsol**
1. Admin memilih menu ubah konsol.
2. Program memeriksa apakah ada data konsol.
3. Jika data kosong, program menampilkan pesan bahwa tidak ada konsol yang bisa diubah.
4. Jika data tersedia, Admin memasukkan ID konsol yang ingin diubah.
5. Program memeriksa apakah ID konsol ditemukan dan data baru sudah benar.
6. Jika data tidak sesuai, perubahan tidak dilanjutkan.
7. Jika data sesuai, program meminta konfirmasi dari Admin.
8. Jika Admin membatalkan perubahan, data tetap seperti semula.
9. Jika Admin menyetujui perubahan, program menyimpan data yang sudah diperbarui.

**Fungsi:** Mengubah informasi konsol yang sudah terdaftar dalam program.

**Opsi 4 — Hapus Konsol**
1. Admin memilih menu hapus konsol.
2. Program memeriksa apakah ada data konsol.
3. Jika data kosong, program menampilkan pesan bahwa tidak ada konsol yang bisa dihapus.
4. Jika data tersedia, Admin memasukkan ID konsol yang ingin dihapus.
5. Program memeriksa apakah ID konsol ditemukan.
6. Jika ID tidak ditemukan, proses penghapusan tidak dilanjutkan.
7. Jika ID ditemukan, program meminta konfirmasi penghapusan.
8. Jika Admin membatalkan, data konsol tetap tersimpan.
9. Jika Admin menyetujui, program menghapus data konsol tersebut.
10. Program menyimpan perubahan data.

**Fungsi:** Menghapus data konsol yang sudah tidak diperlukan dari program rental.

**Opsi 5 — Lihat Daftar Penyewaan dan Transaksi**
1. Admin memilih menu daftar penyewaan dan transaksi.
2. Program memeriksa data penyewaan dan transaksi yang tersimpan.
3. Jika belum ada transaksi, program menampilkan pesan bahwa data masih kosong.
4. Jika data tersedia, program menampilkan daftar penyewaan dan transaksi.
5. Admin dapat melihat aktivitas penyewaan yang sudah tercatat.

**Fungsi:** Membantu Admin memeriksa daftar penyewaan dan transaksi yang dilakukan pengguna.

**Opsi 6 — Laporan Ringkas**
1. Admin memilih menu laporan ringkas.
2. Program memeriksa data yang diperlukan untuk membuat laporan.
3. Jika belum ada data, program menampilkan pesan bahwa laporan belum tersedia.
4. Jika data tersedia, program menampilkan laporan ringkas.
5. Laporan berisi informasi penyewaan, pemasukan, dan konsol yang sering disewa.

**Fungsi:** Membantu Admin mengetahui ringkasan kegiatan rental, termasuk pemasukan dan konsol yang paling sering disewa.

**Opsi 7 — Logout**
1. Admin memilih menu logout.
2. Program mengakhiri sesi Admin.
3. Program mengarahkan pengguna kembali ke Menu Utama.

**Fungsi:** Keluar dari akun Admin dan kembali ke Menu Utama.


**3. MENU USER**

<img width="7460" height="6688" alt="FLOWCHARTPAKEL4-MENU USER drawio" src="https://github.com/user-attachments/assets/64d056d9-7c85-4337-97c5-a6afb8cdeffa" />

Flowchart Menu User berfungsi untuk memberikan akses kepada pengguna agar dapat melihat konsol, mengecek dan mengisi saldo, menyewa konsol, melihat riwayat penyewaan, mencetak invoice, serta mengembalikan konsol.

**Opsi 1 — Lihat Konsol**
1. User memilih menu lihat konsol.
2. Program memeriksa data konsol yang tersimpan.
3. Jika data kosong, program menampilkan pesan bahwa tidak ada konsol yang tersedia.
4. Jika data tersedia, program menampilkan daftar konsol beserta stoknya.
5. User dapat melihat konsol yang bisa disewa.

**Fungsi:** Membantu pengguna mengetahui jenis konsol dan stok yang tersedia sebelum menyewa.

**Opsi 2 — Lihat dan Top Up Saldo**
1. User memilih menu lihat dan top up saldo.
2. Program menampilkan jumlah saldo yang dimiliki pengguna.
3. Program memberikan pilihan apakah pengguna ingin mengisi saldo.
4. Jika tidak ingin mengisi saldo, pengguna dapat kembali ke Menu User.
5. Jika ingin mengisi saldo, program meminta pengguna memasukkan nominal top up.
6. Program memeriksa apakah nominal yang dimasukkan sudah benar.
7. Jika nominal tidak sesuai, proses top up tidak dilanjutkan.
8. Jika nominal sesuai, program menambahkan saldo pengguna.
9. Program menampilkan jumlah saldo terbaru.
10. Program menyimpan perubahan saldo.

**Fungsi:** Memungkinkan pengguna mengecek saldo dan menambahkan saldo untuk membayar biaya penyewaan konsol.

**Opsi 3 — Sewa Konsol**
1. User memilih menu sewa konsol.
2. Program meminta pengguna memasukkan ID konsol dan lama penyewaan.
3. Program memeriksa apakah data yang dimasukkan sudah benar.
4. Jika data tidak sesuai, proses penyewaan tidak dilanjutkan.
5. Jika data benar, program memeriksa apakah stok konsol masih tersedia.
6. Jika stok habis, pengguna tidak dapat menyewa konsol tersebut.
7. Jika stok tersedia, program memeriksa apakah saldo pengguna mencukupi.
8. Jika saldo tidak cukup, pengguna perlu mengisi saldo terlebih dahulu.
9. Jika saldo cukup, program menampilkan nota penyewaan.
10. Program meminta konfirmasi pembayaran.
11. Jika pengguna menyetujui pembayaran, program memotong saldo sesuai biaya sewa.
12. Program menampilkan pesan bahwa pembayaran berhasil beserta ID transaksi.
13. Program menyimpan data penyewaan dan transaksi.

**Fungsi:** Memproses penyewaan konsol dengan memeriksa data, stok, saldo, dan pembayaran pengguna.

**Opsi 4 — Riwayat Penyewaan**
1. User memilih menu riwayat penyewaan.
2. Program memeriksa data penyewaan yang tersimpan.
3. Jika belum ada riwayat penyewaan, program menampilkan pesan bahwa data masih kosong.
4. Jika data tersedia, program menampilkan riwayat penyewaan beserta ID transaksi.
5. User dapat melihat daftar penyewaan yang pernah dilakukan.

**Fungsi:** Memungkinkan pengguna melihat catatan penyewaan yang pernah dilakukan.

**Opsi 5 — Cetak Invoice**
1. User memilih menu cetak invoice.
2. Program meminta pengguna memasukkan ID transaksi.
3. Program memeriksa apakah nomor transaksi ditemukan.
4. Jika nomor tidak ditemukan, invoice tidak dapat ditampilkan.
5. Jika nomor ditemukan, program mengambil data transaksi tersebut.
6. Program menampilkan dan mencetak invoice berdasarkan data transaksi.

**Fungsi:** Menampilkan dan mencetak bukti transaksi penyewaan berdasarkan ID transaksi.

**Opsi 6 — Pengembalian Konsol**
1. User memilih menu pengembalian konsol.
2. Program memeriksa data penyewaan yang tersimpan.
3. Jika tidak ada data penyewaan yang dapat diproses, program menampilkan pesan bahwa tidak ada konsol yang bisa dikembalikan.
4. Jika data tersedia, program menampilkan daftar konsol yang disewa.
5. User memilih nomor konsol yang ingin dikembalikan.
6. Program memeriksa apakah nomor konsol tersebut terdaftar.
7. Jika nomor tidak ditemukan, proses pengembalian tidak dilanjutkan.
8. Jika nomor ditemukan, program mengubah status penyewaan dari "Sewa" menjadi "Dikembalikan".
9. Program menyimpan perubahan data.
10. Program menampilkan pesan bahwa pengembalian berhasil.

**Fungsi:** Memproses pengembalian konsol dan memperbarui status penyewaan dalam program.

**Opsi 7 — Logout**
1. User memilih menu logout.
2. Program mengakhiri sesi pengguna.
3. Program mengarahkan pengguna kembali ke Menu Utama.

**Fungsi:** Keluar dari akun User dan kembali ke Menu Utama.
