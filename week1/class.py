



string = 'hello python world'

# string function

print(string.upper())
print(string.lower())
print(string.capitalize())
print(string.title())
print(string.find('e'))  #searching index

print(string.replace('h', 'H')) # replace word



# Data Structure

#list()
var_list = [1, 2, 3]
print(var_list)

var_list = list([1, 2, 3])
print(var_list)

list_of_all_dt = ['Alpha', 1, 1.22, True, [1,2]]
print(list_of_all_dt)


var_list_main = [2, 4, 6, 8, 10] # even number
print(var_list_main)
var_list_copy = var_list_main.copy()
print(var_list_copy)
var_list_copy.pop() # last value remove
print(var_list_copy)
print(var_list_main)


# accessing elements in a list

bicycles = ['trek', 'cannondale']
print(bicycles[1])

names= ['string', 1, True, 1.0, ['list', 'one'], {'age':20}]
print(names[4][5])


name = 'fayyaz ahmed'
print(f"hi, my name is: {name} {names[0]}")

# string range
list_ = [1,2,3,4]
print(name[0:5])
print(list_[0:2])


# loop iterate over something

for i in name(1, 10): # print 1 to 9
    print(f"this is index {i}")

#print list
names1 = ['fayyaz', 'usama', 'danish']
for i in names1: 
    print(f"{i}")


# character
for char in 'fayyaz'[2]:
    print(char)

for i in range(2, 10, 2): # print 0 to 9
      print(f"this is index {i}")

for i in range(len(names1)):
    print(f" index: {i}, value: {names1[i]}")

# list with index
names1 = ['fayyaz', 'usama', 'danish']
for names1 in enumerate(names1):
    print(names1)

names2 = ['fayyaz', 'usama', 'danish']
for index, name in enumerate(names2):
    if index <=2:
        continue
    print(index, names2)

#multiple assignment
a, b = 'aa', 'bb'
print(a)
print(b)




#tuple

var_tuple = (1, 'awais', 3, [])
var_tuple.index(1)
var_tuple.count(1)

#distinct

var_list2 = [144,222,333,444]
set(var_list2)


#if

cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car.lower() == 'bmw':
        print(car.upper())
    else:
        print(car.title())

age_0 =22
age_1 = 18

True or (age_0>=21) and (age_1>=21)

'audi' in cars
'audi2' in cars


for i in cars:
    if i == 'bmw':
        continue



#a simple dictionary
#like json

var_dict = dict()
var_dict ={}
print(var_dict)

var_dict = {"name":"Awais", "class":"CDE"} # key and : value
print(var_dict)

var_dict['name']
var_dict.get('name') #good tareeka

var_dict.keys()
var_dict.values()
var_dict.items() # list of tupple / array of json

for k in var_dict.keys():
    print(k, var_dict[k])

for v in var_dict.items():
    print(v)

alien_0 = {
    "color" : "[red]"
}


alien_0['color'] = "blue"

print(alien_0)



var_str = 'fayyaz ahmed'
print(var_str)
type(var_str)


int_var = 12
print(int_var)
int('12345')
type(int_var)

float_var = 12.0
print(float_var)
type(float_var)
float('123')
float('123.344')


bool_var = True
bool_var = False

print(bool_var)
type(bool_var)
bool(0)
bool(1)





favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': 'c#',
    'awais': 'c',
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    print(f"{name} fav languages are:")
    for i, lang in enumerate(languages):
        print(f"{lang}")


#function

def fuction_one():
    print('hello')

fuction_one()

def fun():
    pass


def greet_user():
    """ hiiiii """
    print("hello")

greet_user()


def des_pet(animaltype, petname):
    print(animaltype)
    print(petname)

des_pet("harry", "cat")

#arbitary tupple

def make_pizza(size, *topping):
    print(size)
    print(topping)

make_pizza(10, 'hi', 'hello')


#arbitary dictionary

def make_pizza(size, **topping):
    print(size)
    print(topping)

make_pizza(size=10, top='1', top='2')



# a = 100
# b = 2

# if a <= 100:
#     print("less then")
# else:
#      print("greater")



# print(a*b)

# print(h)