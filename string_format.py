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
