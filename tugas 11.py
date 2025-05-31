#1. Mereverse setiap kata dalam kalimat

def reverse_per_kata(kalimat):
    list_kata = kalimat.split() #split digunakan untuk memisahkan kalimat menjadi daftar kata
    reverse_kata = [kata[::-1] for kata in list_kata] #Menggunakan list comprehension untuk membalik setiap kata
    return ' '.join(reverse_kata) #Menggabungkan kembali daftar kata menjadi kalimat 
print(reverse_per_kata("AKU CINTA KAMU"))
# Output: "UKA ATNIC UMAK"
    
#2. Mengurutkan kata berdasarkan indeks list

def urutkan_kalimat(kalimat, urutan):
    list_kata = kalimat.split() #split digunakan untuk memisahkan kalimat menjadi daftar kata
    urutan_kalimat = [list_kata[i - 1] for i in urutan]#Menyesuaikan indeks karena karena Python menggunakan indeks mulai dari 0  maka harus mengurangi 1 (i - 1)
    return ' '.join(urutan_kalimat) #Menggabungkan kembali daftar kata menjadi kalimat 
print (urutkan_kalimat(" HARI INI SEDANG BELAJAR PYTHON ", [5, 1, 4, 3, 2]))
# Output: "PYTHON HARI BELAJAR SEDANG INI"

#3. Mengganti huruf vokal dengan simbol tertentu

def ganti_vokal(kalimat, opsi):
    vokal_kecil = {'a': '4', 'i': '1', 'u': '|_|', 'e': '3', 'o': '0'} #mengganti huruf vokal kecil
    vokal_kapital = {'A': '4', 'I': '1', 'U': '|_|', 'E': '3', 'O': '0'} #mengganti huruf vokal kapital
    hasil = "" #menampung hasil kalimat setelah diubah
    for huruf in kalimat:
        if opsi == 1 and huruf in vokal_kecil: #jika menggunakan huruf kecil
            hasil += vokal_kecil[huruf]  #menambahkan versi simbol ke hasil
        elif opsi == 2 and huruf in vokal_kapital: ##jika menggunakan huruf kapital
            hasil += vokal_kapital[huruf] #menambahkan versi simbol ke hasil
        else:
            hasil += huruf
    return hasil
print(ganti_vokal("Aku Cinta Kamu", 1))
# Output: "Ak|_| C1nt4 K4m|_|"
print(ganti_vokal("Aku Cinta Kamu", 2))
# Output: "4ku Cinta Kamu"