# FOR IN LOOP
# Sebuah block kode yang akan di terus di running dalam jumlah tertentu
# For in akan dibarengi dengan tipe data yang sifatnya 'iterable'
#   iterable :
#       string : 'Hello from the otherside'
#       list : [1, 2, 3] / ['Senin', 'Selasa'] / [{"name" : "Hulk"}, {"name" : "Thor"}]
#       tuple : (1, 2, 3) / ('Senin', 'Selasa') / ({"name" : "Hulk"}, {"name" : "Thor"})

###############
# S T R I N G
##############
lorem = 'Ipsum'
count = 1

# nama variable setelah keyword 'for' adalah bebas
for alphabet in lorem:
    print(f'Huruf ke - {count} : {alphabet}')
    count += 1

###########
# L I S T
##########

# FIRST
numbers = [2, 4, 6, 8]
powNumbers = []

for number in numbers:
    resPow = pow(number, 2)
    powNumbers.append(resPow)

print(powNumbers)

# SECOND
cars = [
    {"name": "Avanza", "color": "Grey", "price":139000},
    {"name": "Xpander", "color": "Black", "price":299000},
    {"name": "Fortuner", "color": "Silver", "price":172000}
]

carName, carColor, carPrice = [], [], []

for car in cars:
    carName.append(car["name"])
    carColor.append(car["color"])
    carPrice.append(car["price"])

print(carName) # ['Avanza', 'Xpander', 'Fortuner']
print(carColor) # ['Grey', 'Black', 'Silver']
print(carPrice) # [139000, 299000, 172000]

#########
# TUPLE #
########

buuleans = (True, False, True , True, False)

for buul in buuleans:
    if buul :
        print(f'Aku yakin besok ujian akan mudah')
    else :
        print(f'Aku yakin besok ujian akan sulit.')