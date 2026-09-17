# Buatlah program yang meminta user memasukkan usia seseorang, lalu kategorikan usia 
# tersebut berdasarkan kriteria berikut:

# Kriteria Umur
    # a. 0 - 12 tahun      : Anak-anak 
    # b. 13 - 17 tahun     : Remaja 
    # c. 18 - 59 tahun     : Dewasa 
    # d. 60 tahun ke atas  : Lansia 

UsiaUser = int(input("Berapa umurmu?"))

if UsiaUser == UsiaUser >=0 and UsiaUser <=12 :
    print("Anak-anak")
elif UsiaUser == UsiaUser >=13 and UsiaUser <=17 :
    print("Remaja")
elif UsiaUser == UsiaUser >=18 and UsiaUser<=59 :
    print("Dewasa")
else :
    print("Lansia")








