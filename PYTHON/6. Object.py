####################
# CLASS and OBJECT #
####################

# Hampir semua yang ada di dalam python merupakan sebuah object
# Didalam object akan memiliki properties dan method
# Property : variable yang ada di dalam object
# Method : function yang ada di dalam object

#  Class merupakan sebuah blue print / cetakan untuk membuat object

class Person:
    def __init__(self, _name, _age):
        self.name = _name
        self.age = _age
        self.pets = ['Molly', 'Kitten']
        self.job = {'position' : 'Manager', 'sallary' : 100000}

    def greet(self, _time):
        print(f'Good {_time}, My name is {self.name}')

obj = Person('Karen', 28)

obj.name # 'Karen'
obj.age # 28
print(obj.__dict__) # {'name' : 'Karen', 'age': 28}
obj.__dict__["name"] # 'Karen'
obj.greet('Evening') # Good Evening, I'Am Karen
obj.pets[0] # Molly
print(obj.job["position"]) # Manager
print(obj.__dict__['job']['position']) # Manager


# Obj merupakan sebuah object yang memiliki peroperty dan method
# Property :
#       Buatan : name, age
#       Bawaan : __dict__

# Method :
#      Buatan : greet

