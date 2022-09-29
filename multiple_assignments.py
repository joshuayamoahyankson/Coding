
import time
import random
import os
import shutil
info = name , age , sex , colour = "Joshua Yamoah Yankson" , 21 , "male" , "Black"
print(name,age,sex,colour)
print(info)

Joshua = Barbara = str(27) + "years"
print(Joshua)
print(Barbara)
#strings
name = "joshua yamoah yankson"
print(len(name))
print(name.find("Y"))
print(name.capitalize())
print(name.upper())
print(name.lower())
print(name.isdigit())
print(name.isalpha())
print(name.count("y"))
print(name.replace("o" , "a"))
print(name * 2)
print(name.islower())
print(name.isupper())
print(name.isnumeric)
print(name.isprintable)
print(name.isspace)
print(name.startswith("y", 6))
print(name.endswith("son" , 18))
# math module
import math
number = 6524154.125
x , y , z = 3 , 5 , 8
print(round(number))
print(math.ceil(number))
print(math.floor(number))
print(abs(number)) # turns negative numbers to positive!
print(pow(number, 2))
print(math.sqrt(number))
print(max(x,y,z))
print(min(x,y,z))

#indexing and slicing
website = "http://google.com"
slice1 = slice(7 , 13 )
slice2 = slice(7 , -4)
print(website[slice2])
print(website[slice1])


for seconds in range(20 , 0 , -2):
    print(seconds) 
    time.sleep(.2)
print("Happy Coding")
"""
columns = int(input("Enter the number of columns: "))
rows = int(input("Enter the number of rows: "))
symbol = input("Enter the symbol to use: ")

for x in range(columns):
    for y in range(rows):
        print(symbol, end="")
    print()
    """
phone_number = "054-955-1404"
for i in phone_number:
    if i == "-":
        continue
    print(i , end="")
    
print()
food = ["Rice" , "Fufu" , "kokonte" , "Banku" , "Etew"] 
print(food.append("Omotuo"))
print(food.count("Rice"))

#2D list---list with other list

breakfast = ["koko" , "wheat" , "oat"]
lunch = ["rice" , "banku" , "yam"]
dinner = ["fufu" , "kokonte" , "omotuo"]
diet = [breakfast, lunch, dinner]
print(diet)
print(diet[1][2])

#tuples
tuple = ("dark" , "bright" , 12)
print(tuple.count("dark"))
print(tuple.index(12))

#sets
games = {"table-tennis", "soccer", "basket-ball", "draft", "Race" , "Race"}
domestic_game = {"ludu", "ampe", "oware" , "soccer"}
games.add("Boxing")
games.add("Wrestling")
#games.update(domestic_game)
print(games)
all = domestic_game.union(games)
print(all)
print(domestic_game.difference(games))
print(games.intersection(domestic_game))

#dictionary
dict = {"Eastern Reg": "Koforidua", "Greater Accra" :"Accra", "Ashanti Reg": "Kumasi"}
print(dict.keys())
dict["Eastern Reg"] = "Manfe"
print(dict.values())
dict.update({"Ashanti Reg":"Manso"})
print(dict)

#index operator
name = "joshua Yamoah Yankson"
if (name[2] .islower):
    print("huh I found it")
    name = name.capitalize()
print(name)
first_name = name[:6].upper()
middle_name = name[7:13].lower()
last_name = name[14:].upper()

print(first_name , middle_name, last_name)

def add(*args):
    sum = 0
    for i in args:
        sum += i
    print(sum)
add(2,4,6,8)

#str.format
first_name = "Joshua"
middle_name = "Yamoah"
last_name = "Yankson"
Wife_name = "Barbara Otoo"
name = "My full name is {} {} {}"
#name(first_name="Joshua", middle_name="Yamoah", last_name="Yankson")
print("my name is {0} " "{1}".format(first_name , last_name))# positional argument
print("my name is {} {}".format("Joshua", "Yankson"))#positional argument
print("my name is {first_name} " "{last_name}".format(first_name = "Joshua", last_name = "Yankson"))#keyword argument
print(name.format(first_name, middle_name, last_name))
print("my Wife's name is {:10} Akosua".format(Wife_name))
print("my Wife's name is {:>10}  Akosua".format(Wife_name))
print("my Wife's name is {:^10}  Akosua".format(Wife_name))

#STR FORMAT WITH NUMBERS!
number = 2016
decimal = 0.25
print("this is my number {:.1f}".format(decimal))
print("this is my number {:,}".format(number))
print("this is my number {:b}".format(number))
print("this is my number {:o}".format(number))
print("this is my number {:x}".format(number))
print("this is my number {:e}".format(number))
print("this is my number {:X}".format(number))

x = random.randint(1 , 10)
y = random.random()
my_list = ["fufu", "banku", "rice", "omotuo"]
cards = [1,2,3,4,5,6,7,8,9,"J","Q","K","A"]
z = random.choice(my_list)
random.shuffle(cards)
print(x)
print(y)
print(z)
print(cards)

#Using the OS module to find if a file or folder exist on your computer!
path = "C:\\Users\\Joshua Yankson\\Desktop\\text.txt"
if os.path.exists(path):
    print("It is an existing file")
    if os.path.isfile(path):
        print("O yes that is an available file")
    elif os.path.isdir(path):
        print("It isn't an available file")
else:
    print("Not at all")
    
#working with files!
"""
with open("text.txt") as file:
    print(file.read()) #reading a file
print(file.closed)
"""


write = "\nMake sure to go with your health card!"
with open("write.txt" , "a") as file: #writing a file by appending
    file.write(write)
    
#shutil.copy2("text.txt" , "copy.txt") # using shutil to either copyfile , copy or copy2  a file!

#more on the OS module
source = "text.txt"
destination = "C:\\Users\\Joshua Yankson\\Desktop\\text.txt"
if os.path.exists(destination):
    print("it's already there Dude!")
else:
    os.replace(source , destination)
    print(f"{source} was moved")
    
"""
os.remove("new.txt") # the remove function here only removes files not folders
print()
"""
#os.rmdir("folder") # rmdir removes folders that do not contain any files inside it from a path
#print()
try:
    shutil.rmtree("folder") # the shutil.rmtree function deletes a folder containig a file. rmtree is considered quite a dangerous function.
    print("I can delete that")
except:
    print("the folder has been deleted successfully")

def hello():
    print("hi friend")
    print("I am okay")
def greetings():
    print("goodmorning")
    print("goodafternoon")
def something():
    print("hello")
something()