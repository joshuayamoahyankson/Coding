



dictionary = {
    "full_name" : "Joshua Yamoah Yankson",
    "age" : 27,
    "height" : 5.8,
    "colour" : "Dark",
    "interest" : "Computer science"  
}
dictionary["level"] = "100"
print(dictionary)
weight = dictionary.get("weight")
print(weight)
print(dictionary["full_name"])
dictionary["height"] = 6
print(dictionary)

dictionary["age"] += (1)
print(dictionary["age"])
weight = "weight" in dictionary
print(weight)
counts = dict()
names = ["Joshua", "Yamoah", "Yankson", "Hyrum", "Fiifi", "Barbara", "Otoo","Joshua"]
for i in names:
    if i not in counts:
        #counts[i] = counts.get(i, 0) + 1
        counts[i] = 1
    else:
        counts[i] += 1
        print(counts)
#del dictionary["age"]
#dictionary.clear()
#del dictionary
dictionary3 = {
    "Job" : "Plumber",
    "salary" : 270,
    "work_years" : 10,
    "company" : "Jobab",
    "rank" : "senior", 
    "hours" : 8 
}
new_list = list(dictionary.items())
print(new_list [4])

dictionary_2 = dict(name = "Joshua", age = 25, sex = "male", married = "yes", )
print(dictionary_2)

updated = dictionary.update(dictionary3)
print(updated)

weather_in_G = {"Eastern" : "rainy",
                "Accra" :"Sunny",
                "Kumasi" : "rainy",
                "North" : "sunny",
                "Central" : "rainy"
                }
weather_in_H = {key: value for (key,value) in weather_in_G.items() if value == "rainy"} #dictionary comprehension suntax = {key : expression for (key,value) in iterable} or {key : expression for (key,value) in iterable if condition}
print(weather_in_H) 

weather_in_G = {"Eastern" : 28,
                "Accra" : 30,
                "Kumasi" : 31,
                "North" : 36,
                "Central" : 25
                } 
weather_in_J = { key: ("Warm" if value <= 30 else ("Cold")) for (key,value) in weather_in_G.items()}
print(weather_in_J) # {key : (if/else) for (key,value) in iterable}

# {key : (if/else) for (key,value) in iterable}

def check_temp (value):
    if value <= 25:
        return "Cold"
    elif 30 >= value <= 31:
        return "Warm"
weather_in_W = {key : check_temp(value) for (key,value) in weather_in_G.items()}
print(weather_in_W)
        
        
        
        
school = {
    "student_name" : "Kwame Ansah",
    "student_age" : 19,
    "student_class" : "JHS2",
    "student_course" : "science"
}

details = {key : value for(key, value) in school.items() if value == "JHS2" or value == "science"}
print(details)

def school_info(value):
    for value in school.values():
        if value == "Kwame Ansah" or value == 19:
            return("You fished that out")
        elif value == "JHS2":
            return("that too is part")
        else:
            return("didn't find the requested info")
details = {key : school_info(value) for (key,value) in school.items()}
print(details)
