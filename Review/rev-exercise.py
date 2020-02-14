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

##################################################################
# tentukan apakah sebuah kata memiliki perulangan huruf atau tidak
# buatlah function untuk mendeteksi itu
# Hello -> false
# Sunday -> true
# ini -> false
# Sunkis -> false
#################################################################