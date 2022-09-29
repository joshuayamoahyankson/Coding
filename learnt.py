import time
import os
import multiple_assignments
"""user_input = input("Enter your name: ")
print(user_input.lower())
while user_input:
    if user_input.lower() != user_input.upper():
        print("That is  not good!")
        break
    else:
        print("That is okay!")
    """


time1 = time.asctime()
for x in range(1 , 4):
    time2 = time.sleep(0.01)
    print(x)
    
print(time1)
#print(time2)

#source = "word.txt"
#destination = "C:\\Users\\Joshua Yankson\\Desktop\\word.txt"
"""
if os.path.exists(destination):
    print("Hurray it's here!")
else:
    os.replace(source , destination)
    print("The file is no longer here...it's moved to the desktop!")
    """
source = "C:\\Users\\Joshua Yankson\\Desktop\\somefolder"  
destination = "C:\\Users\\Joshua Yankson\\Desktop\\CODING"

if os.path.exists(destination):
    print("Yea")
    if os.path.isfile(source):
        print("it os a file")
    elif os.path.isdir(source):
        print("it is a folder")
else:
    os.replace(source , destination)
    print("received")
"""
os.remove("new.txt") # the remove function here only removes files not folders
print()
"""
#os.rmdir("somefolder") # rmdir removes folders from a path
#print()

multiple_assignments.hello()
multiple_assignments.greetings()



