# input data
nama = input ("Nama: ")
nilai = int (input ("Nilai: "))
output = "Halo, " + nama + "!" + " Nilai Anda setelah dikonversi adalah "

if 85 <= nilai <= 100:
    print(output, 'A')
elif 80 <= nilai <= 84:
    print(output, 'A-')
elif 75 <= nilai <= 79:
    print(output, 'B+')
elif 70 <= nilai <= 74:
    print(output, 'B')
elif 65 <= nilai  <= 69:
    print(output, 'C+')
elif 60 <= nilai <= 64:
    print(output, 'C-')
elif 60 > nilai:
    print(output,'E')
else:
    pass