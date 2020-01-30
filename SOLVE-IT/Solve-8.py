# Input berat badan (kg)
weight = int(input('Masukkan massa (kg) : '))

# Input tinggi (cm)
heightCm = int(input('Masukkan tinggi (cm) : '))
heightM = heightCm / 100

# Hitung IMT
# berat / tinggi ^ 2
imt = weight / pow(heightM, 2)

# Tentukan status
if imt < 18.5 :
    status = 'kurang'
elif imt >= 18.5 and imt <= 24.9 : # 18.5 <= imt <= 24.9
    status = 'ideal'
elif 25.0 <= imt <= 29.9 :
    status = 'berlebih'
elif 30.0 <= imt <= 39.9 :
    status = 'sangat berlebih'
else:
    status = 'obesitas'

# Print
print(
    f'Massa {weight} kg & tinggi {heightM} m\n' +
    f'IMG = {imt}, berat badan {status}'
)