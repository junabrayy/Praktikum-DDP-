def profil(nama, alamat, gender, umur, hobi):
  print("Nama Saya Adalah :", nama)
  print("Alamat Saya Dijalan :", alamat)
  print("Gender Saya Adalah :", gender)
  print("Umur Saya Adalah :", umur)
  print("Hobi Saya Adalah:", hobi)

#pemanggilan fungsi
profil("Muhammad Raffi Arjuna","Jl.Situ Indah Kelapa Dua Depok", "Laki-laki", "18 Tahun", "Futsal")

def cek_kelulusan(nilai):
    if nilai < 60:
        return "maka gagal"
    elif 61 < nilai <70:
        return "maka baik"
    elif 71 < nilai <80: 
        return "maka sangat baik"
    elif 81 < nilai <100:
        return "maka istimewa"
    else:
        return "nilai tidak valid" 

#pemanggilan fungsi

print(cek_kelulusan(75))
print(cek_kelulusan(93))
print(cek_kelulusan(66))
print(cek_kelulusan(55))



def cetak_ganjil(n):
    for i in range(1, 101, 2):
        print(i, end="  ")

cetak_ganjil(100)
