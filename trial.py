numbers_list = [1,2,3,4,6,5,2,8,9,"name", 12.4]

def list_num(num):
    numbers_list1 = numbers_list.copy()
    numbers_list1.append("hello world")
    numbers_list1.append(0)
    numbers_list1.append("cat")
    print(numbers_list1)
list_num(numbers_list)
print(numbers_list)