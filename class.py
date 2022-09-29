
#an attribute deals with what something is/has(eg, name , colour, age etc)
#it describes what an object is
#a Method = Action(eg,eat,sleep,walk etc)
#An object can have some combination of both methods and attributes
#An object is an instance of a class
#The "self" parameter allows us to access the attributes and methods of a class.
#The "__init__()" function allows us to provide values for the attributes of a class
#each object is a different instance of a class
#class is the template
#object is the instance
#self is a reference to the current instance of a class
#self is used to access variables that belong to the class
#whenever a new object is created,the specific values would be assigned to the specified variables.
# the specific values would be passed into the constructor as parameters
class Humans:
    
    body_part = "many"
    
    def __init__(self, head , hand, eye, ear):
        self.head = head
        self.hand = hand
        self.eye = eye
        self.ear = ear
    def eating(self):
        print("this boy is eating with his " +self.hand + " hand")
    def think(self):
        print("He can think very well with his " +self.head + " head")
    def sight(self):
        print("My Wife doesn't see well with her "+self.eye + " eyes")
    def hearing(self):
        print("I wish you could hear well with your "+self.ear + " ears")
        
parts = Humans ("big" ,"right", "brown", "dumb" ) #An Instance in python
name = Humans("Joshua" , 27 , "Dark" , "Tall")
parts.body_part = 2
print(parts.head) # Acessing Object Properties.
print(parts.hand)
print(parts.eye)
print(parts.ear)
print(Humans.body_part) 
print(parts.body_part)
print(name.body_part)

parts.eating()
parts.hearing()
parts.think()
parts.sight()
