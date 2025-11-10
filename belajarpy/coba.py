# angka = 3
# angka2 = 5 + angka
# print(angka)

# #DataList
# nama = ["Ade","Aira","Bagus","Boby"]
# nama.append("Beny")
# print(nama) 
# print(len(nama))

#[ Variabel dan Tipe Data ]======================(Tugas 1)========================#
variabel_int = 12345
variabel_str = "coba"
variabel_bool= True
variabel_list= ["rosi","gesang"]

print("Value : ",variabel_int," Class : ",type(variabel_int))
print("Value : ",variabel_str," Class : ",type(variabel_str))
print("Value : ",variabel_bool," Class : ",type(variabel_bool))
print("Value : ",variabel_list," Class : ",type(variabel_list))

print("===========================================================")

#[ List dan Manipulasi ]======================(Tugas 1)========================#

barang = ["beras","minyak","telur"]
harga = [12000,17000,24000]

barang.extend (["Gula","Kopi"])
harga.extend ([15000,20000])

for item in barang,harga:
    print(item)

print("===========================================================")

#[ Dictionary ]======================(Tugas 1)========================#

harga_belanjaan = {
    "beras": 12000,
    "minyak": 17000,
    "telur": 24000,
    "gula": 15000,
    "kopi": 20000
}
import roman
for i, (barang,harga) in enumerate (harga_belanjaan.items(),start=1):
    print(f"{roman.toRoman(i)} . {barang} = Rp{harga}") 

# value = harga / key = barang
total = sum(harga_belanjaan.values())
print(f"Total harga = Rp{total}")

print("===========================================================")

#[ Fungsi ]======================(Tugas 1)========================#

def hitung_persegi (panjang,lebar):
    luas = panjang * lebar
    keliling = 2 * (panjang + lebar)
    return luas, keliling

panjang = int(input("Masukan panjang = "))
lebar   = int(input("Masukan Lebar   = "))

luas,keliling = hitung_persegi(10,5)
print(f"Luas persegi panjang = {luas}")
print(f"Keliling persegi panjang = {keliling}")

print("===========================================================")

#[ Percabangan ]======================(Tugas 1)========================#

usia = int(input("Masukan usia anda = "))
if usia <= 13 :
    print("“Anak”")
elif usia <= 24 :
    print("“Remaja”")
elif usia <= 29 :
    print("“Dewasa”")
elif usia <= 50:
    print("“Lansia”")
else:
    print("Anda terlalu tua wkwk")