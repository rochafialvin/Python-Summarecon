# SOLVE IT - 6

# A : 60 km/h
# B : 40 km/h
# distance : 120 km
# waktu yang dibutuhkan untuk bertemu ?

speedA = 60
speedB = 40
speedTotal = speedA + speedB
distance = 120

# Waktu tabrakan dalam hitungan jam
timeCrash = distance / speedTotal
# Cari tahu berapa jam
timeInHour = int(timeCrash)
# Cari tahu berapa menit
timeInMinute = int((timeCrash * 60) % 60)

print(
    f"Akan bertemu setelah {timeInHour} jam {timeInMinute} menit"
)