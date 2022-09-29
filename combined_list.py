def main():
    # Create a list that contains five student numbers.
    numbers = ["42-039-4736", "61-315-0160",
            "10-450-1203", "75-421-2310", "07-103-5621"]

    # Create a list that contains five student names.
    names = ["Clint Huish", "Amelia Davis",
            "Ana Soares", "Abdul Ali", "Amelia Davis"]

    # Convert the numbers list and names list into a dictionary.
    student_dict = dict(zip(numbers, names))

    # Print the entire student dictionary.
    print("Dictionary:", student_dict)
    print()

    # Convert the student dictionary into
    # two lists named keys and values.
    keys = list(student_dict.keys())
    values = list(student_dict.values())

    # Print both lists.
    print("Keys:", keys)
    print()
    print("Values:", values)

numbers = ["42-039-4736", "61-315-0160",
            "10-450-1203", "75-421-2310", "07-103-5621"]

nums = [1,2,3,4,5]

nums_new = [x+1 for x in nums]
print(nums_new)


for x in numbers:
    print(x)
    print(list(x))
    if x[0] == "4":
        print("yea")
    else:
        print("No")
     
    # k = list(x) 
    # if k[0] == ['4', '2', '-', '0', '3', '9', '-', '4', '7', '3', '6']:
    # 	print(k)
    # else:
    # 	print("Not available")

y = numbers[0]
print(y)

# Call main to start this program.
if __name__ == "__main__":
    main()
