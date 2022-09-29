
# List Comprehension

#syntax

#list = [expression for item in iterable]
num_square = [i * i for i in range(1 , 11)]
print(num_square)

# list comprehension involving condition
#list2 = [expression for item in iterable if condition]
students_grade = [100,90,80,70,60,50,40,30,20,0]
passed_grade = [x for x in students_grade if x >= 60]
print(passed_grade)

phone_list = ["iPhone12", "iPhone12pro", "iPhone13" ]
phone_prices = [5000 , 5500, 6000]

combined_phone = [(phone_l, phone_p) for phone_l in phone_list for phone_p in phone_prices]
print(combined_phone)

iPhone_and_prices = [f"{phone_list} {phone_prices}" for phone_list , phone_prices in zip(phone_list, phone_prices)]
print(iPhone_and_prices)
iphone_model = ["Iphone11", "iPhone12", "iPhone13", "iphone14"]

for i in iphone_model:
    #for i in phone_list:
    if i in phone_list:
        print(i)

list_comp = [phone for phone in phone_list if phone in iphone_model]
print(list_comp)

First_name = ["Joshua", "Barbara", "Hyrum"]
Sur_name = ["Yankson", "Otoo", "Yankson"]
age = [27, 27, 2]

family_info = [f"{First_name}, {Sur_name} - {age}" for First_name, Sur_name, age in zip(First_name, Sur_name, age)]
print(family_info)


#list3 =  [expression (if/else) for item in iterable]
"""
passed_grade = [x if x >= 60 else "FAILED" for x in students_grade]
print(passed_grade)
squares = int(len(range(1 , 5)))
for i in range(1 , 11):
    i = i * squares
    print(i)
    """
