class Monster: 
    def __init__(self, health, energy, speed) -> None:
        self.health = health
        self.energy = energy
        self.speed = speed
        print("that is all the speed it has!")
    
    def __len__(self):
        return self.energy
    
    def __add__(self, other_number):
        return self.speed + other_number
    def __str__(self) -> str:
        return "A monster has attacked me!"
    
    def move(monster, speed):
        print(f"{speed} is too low!")
    
monster = Monster(40 , 50, 10)
monster.move(20)
print(monster.speed)
print(len(monster))
print(monster.__dict__)
print(vars(monster))
print(monster + 15)
print(str(monster)) # The str isn't a necessary function to call in the print function


#create a Monster class with a parameter called func, store this func as parameter
#create another class, called Attacks, that has 4 methods:
#bite , strike, slash , kick (each method just prints some text)
#create a monster object and give it one of the attacks methods from the Attacks class

class Monster1:
    def __init__(self, func):
        self.func = func

class Attacks:
    
    def bite(self):
        print("THIS IS BITE")
        
    def strike(self):
        print("THIS IS STRIKE")
        
    def slash(self):
        print("THIS IS SLASH")
        
    def kick(self):
        print("THIS IS KICK")
    

attacks = Attacks()
monster = Monster1(func = attacks.strike)
monster.func()

#create a Hero class with 2 parameters: damage and monster
#the Monster class should have a method that lowers the health --> get_damage(amount)
#the hero class should have an attack method that calls the get_damage method from the monster
# the amount of damage is Hero.damage
class Monster2: 
    def __init__(self, health, energy) -> None:
        self.health = health
        self.energy = energy
        
    def get_damage(self, amount):
        self.health -= amount
        self.energy += amount

class Hero:
    def __init__(self, damage, monster) -> None:
        self.damage = damage
        self.monster = monster
        
    def attack(self):
        Monster2.get_damage(Hero.damage) 
# Call Method from another class in a different class in python
# We can call the method of another class by using their class name and function with dot operator;
# for example: if the 1st class name is class a and its method is method_A and the second class is class B nad its method #is method_B, then we can call method_A from class B by the following way:
    """class A:
    method_A(self):
        {}
class B:
    method_B(self):
        A.method_A()
    """   
monster3 = Monster2(health = 60, energy = 50)
hero = Hero(damage = 15, monster = monster3)
monster3.get_damage(20)
print(monster3)
print(monster3.health)
print(monster3.energy)
print(monster3.health)