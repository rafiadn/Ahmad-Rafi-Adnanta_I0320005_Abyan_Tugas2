#Judul
print("Identitas Diri")

#Data
nama = str("Ahmad Rafi Adnanta")
nim = str("I0320005")
kelas = str("A")
prodi = str("Teknik Industri")
fakultas = str("Teknik")
univ = str("Universitas Sebelas Maret")
jalur = str("Mandiri")
alamat = str("Jalan Cemara 2, No. 9, RT 2 RW 3, Gumpang, Kartasura, Sukoharjo")
gender = str("Laki-laki")
agama = str("Islam")
te_lahir = str("Sukoharjo")
ta_lahir = str("11 September 2002")
t_badan = int("160")
b_badan = float("48.5")
u_sepatu = int("41")
no_hp = str("085156376753")
email = str("adnantarafi@gmail.com")
instagram = str("@rafi_adn")

#Data Umur
tanggal_sekarang = 12
bulan_sekarang = 3
tahun_sekarang = 2021
tanggal_lahir = 11
bulan_lahir = 9
tahun_lahir = 2002
umur_dalambulan = float((tanggal_sekarang - tanggal_lahir)/30) + (bulan_sekarang - bulan_lahir) + ((tahun_sekarang - tahun_lahir)*12)
umur_dalamtahun = float(umur_dalambulan / 12)
umur_dalamhari = float(umur_dalambulan * 30)

#Output
print("Nama Lengkap: ", nama)
print("NIM: ", nim)
print("Kelas: ", kelas)
print("Program Studi: ", prodi)
print("Fakultas: ", fakultas)
print("Universitas: ", univ)
print("Jalur Masuk Perguruan Tinggi: ", jalur)
print("Alamat: ", alamat)
print("Tempat Lahir: ", te_lahir)
print("Tanggal Lahir: ", ta_lahir)
print("Umur dalam Tahun: ", umur_dalamtahun)
print("Umur dalam Bulan: ", umur_dalambulan)
print("Umur dalam Hari: ", umur_dalamhari)
print("Jenis Kelamin: ", gender)
print("Agama: ", agama)
print("Tinggi Badan: ", t_badan, "cm")
print("Berat Badan: ", b_badan, "kg")
print("Ukuran Sepatu: ", u_sepatu)
print("Nomor HP: ", no_hp)
print("Email: ", email)
print("Instagram: ", instagram)
