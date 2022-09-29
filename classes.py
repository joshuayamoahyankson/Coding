class Person:
    def __init__(self , name):
        self.name = name
        print(self.name)
    def age(self):
        print('you have an age')
        
    def name(self):
        pass
    
    def talk(self):
        print('talk')

class Joe(Person):
    pass
    
john = Person("Joshua")
print(john.name)
john.talk()
joe = Joe('Joshua')
print(joe.age())