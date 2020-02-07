# DICTIONARY
# Menggunakan kurung kurawal {}
# Tidak menggunakan index, melainkan key
# Penulisan nama key bersifat case-sensitive
# Nama property ditulis menggunakan kutip (seperti string)

# price = {
#     'apple' : 10000,
#     "grape" : 15000,
#     'orange' : 15000
# }

# price['grape'] // 15000

# d = {
#     'numInt' : 123,
#     'numList' : [0, 1, 2],
#     'numStr' : 'Hello',
#     'numDict' : {'insideKey' : 100}
# }

# d['numList'] # [0, 1, 2]
# d['numDict'] # {'insideKey' : 100}
# d['numDict']['insideKey'] # 100

# heroes = {
#     'batman' : {'name' : 'Bruce', 'age' : 41}, 
#     'ironman' : {'name' : 'Tony', 'age' : 42}, 
#     'thor' : {'name' : 'Thor', 'age' : 39} 
# }

# heroes['ironman'] # {'name' : 'Tony', 'age' : 42}
# heroes['ironman']['name'] # 'Tony

########
# KEYS #
########

# Untuk mendapatkan semua key dari dictionary
# keys = heroes.keys()

# keys # dict_keys(['batman', 'ironman', 'thor'])

# for i in keys:
#     print(i)

##########
# VALUES #
##########

# Untuk mendapatkan semua value dari dictionary
# values = heroes.values()
# values    {'name' : 'Bruce', 'age' :41}
#           {'name' : 'Tony', 'age' :43}
#           {'name' : 'Thor', 'age' :39}

# i = {'name' : 'Bruce', 'age' :41}
# for i in values :
#     print(
#         'Name: ' + i['name']
#     )


#########
# ITEMS #
#########

hero = {
    'Batman' : {'name' : 'Bruce', 'age' : 41},
    'IronMan' : {'name' : 'Tony', 'age' : 42},
    'SpiderMan' : {'name' : 'Peter', 'age' : 27}
}

items = hero.items()
# [
#   ('Batman', {'name': 'Bruce', 'age': 41}),
#   ('IronMan', {'name': 'Tony', 'age': 42}),
#   ('SpiderMan', {'name': 'Peter', 'age': 27})
# ]

key = hero.keys() # 
# [
#   'Batman',
#   'IronMan',
#   'SpiderMan'
# ]

values = hero.values() 
# [
#   {'name': 'Bruce', 'age': 41},
#   {'name': 'Tony', 'age': 42},
#   {'name': 'Peter', 'age': 27}
# ]

