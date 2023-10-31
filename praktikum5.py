list = ['3868','vario','125 CC','merah']
print(list)

list.append('12ribu')
list.append('roda 2')
print(list)

list.insert(2,'honda')
list.insert(3, 'matic')
print(list)

# membuat program menghitung dengan bahasa python 
#   pilihan 1 menghitung luas persegi
#   pilihan 2 menghitung luas lingkaran
#   pilihan 3 menghitung luas segitiga


pesan = """
menu:
1. menghitung luas persegi
2. Menghitung luas lingkaran
3. Menghitung luas segitiga
masukan angka:
"""
pilihan = input(pesan)
match pilihan:
    case "1":
     sisi_persegi = int(input ("silahkan masukan sisi persegi\n"))
     luas_persegi = sisi_persegi * sisi_persegi
     print(luas_persegi)

    case "2":
      jari_jari = int(input("masukan jari-jari\n"))
      luas_lingkaran = 3.14 * jari_jari * jari_jari
      print(luas_lingkaran)
    
    case "3":
        alas = int(input("masukan nilai alas\n"))
        tinggi = int(input("masukan nilai tinggi\n"))
        luas_segita = 0.5 * alas * tinggi
        print(luas_segita)

    case _:
      print("input tadak valid")
      
        


