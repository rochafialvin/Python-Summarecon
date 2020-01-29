# SOLVE IT - 6

# A : 60 km/h
# B : 40 km/h
# distance : 120 km
# waktu yang dibutuhkan untuk bertemu ?

speedA = 60
speedB = 40
speedTotal = speedA + speedB
distance = 120

timeCrash = distance / speedTotal
timeInHour = int(timeCrash)
timeInMinute = int((timeCrash * 60) % 60)

print(
    f"Akan bertemu setelah {timeInHour} jam {timeInMinute} menit"
)