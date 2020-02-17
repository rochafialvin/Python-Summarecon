# Buatlah sebuah function yang menerima string
# akan menghilangkan semua huruf vokal
# dan me return string yang masuk setelah di hilangkan huruf vokalnya

# CLUE :
# filter
# ... not in ...
# join

# Today is friday
def check(x):
    # hasil evaluasi dari .. not in .. adalah boolean
    # sehingga bisa langsung kita return
    return x not in ['a', 'i', 'u', 'e', 'o']

def no_vowel(string):
    resFilter = list(filter(check, string))
    return "".join(resFilter)
    
no_vowel('Today is friday')

# resVowel = no_vowel('Today is friday')
# print(resVowel)


# Happy weekend

####################################################################
# Berapa jumlah perkalian yang dapat dilakukan untuk sebuah integer
# 399 -> 3*9*9 = 243 -> 2*4*3 = 24 -> 2*4 = 8 (3 kali)
# 39 -> 3*9 = 27 -> 2*7 = 14 -> 1*4 = 4 (3 kali)
# 24 -> 2*4 = 8 (1 kali)
# 4 -> nol kali
####################################################################

def mult(numb):
    # numb : 399
    numb = str(numb)

    # numb = '399'
    listInt = []
    for i in numb: # '3', '9', '9'
        listInt.append(int(i))

    #listInt = [3, 9, 9]

    count = 0
    while len(listInt) > 1:
        # Mengalikan semua angka pada list
        res = 1
        for i in listInt: # listInt = [3, 9, 9]
            res *= i 

        # res = 8
        
        # Hasil akhir dari perkalian akan diubah menjadi list lagi
        # Untuk kemudian dilakukan perkalian seperti di atas
        res = str(res)
        # res = '243'
        listInt = []
        for i in res:
            listInt.append(int(i))

        # listInt = [8]

        count += 1

    return count


print('Banyaknya perkalian : ', mult(8))



##################################################################
# tentukan apakah sebuah kata memiliki perulangan huruf atau tidak
# buatlah function untuk mendeteksi itu
# Hello -> false
# Sunday -> true
# ini -> false
# Sunkis -> false
#################################################################