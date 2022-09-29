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
def arg(p,t,r):
    return (p + t - r)/100
p = float(input("Enter  a principal amt:"))
r =  float(input("Enter  a rate of interest:"))
t =  float(input("Enter  the time in years:"))
print("the simple interest value is ",arg(p,t,r))
"""
def string(name, age, sex):
    print(" this is your information ", name, age, sex)
    return string
n = "Joshua Yamoah"
a = 27
s = "male"
string(s,a,n)

def string1(name = "JOSHUA", age = 27, sex = "Male"):
    print(" this is your information ", name, age, sex)
    return string
#n = "Joshua Yamoah"
#a = 27
#s = "male"
string1()