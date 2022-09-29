class Parent:
    def __init__(self, health, energy) -> None:
        self.health = health
        self.energy = energy
        super().__init__(health, energy)
        
    def attack(self, amount):
        print("The animal has a high attacking speed!")
        print(f"Such an amount: {amount} is too small!")
        self.energy -= 20
        
    def move(self, speed):
        print("The monster has moved!")
        print(f"It moved with a speed of {speed}")
        
class Child(Parent):
    def __init__(self,speed, health, energy) -> None: 
        #Parent.__init__(self, health, energy)
        super().__init__(health, energy)
        super().move(15)
        self.speed = speed
        
    def move(self):
        print("It has changed its move up high!")
        print(f'It has has a speed of {self.speed}')
        
child = Child(speed = 100, health = 150, energy = 200)
print(child.attack(20))
parent = Parent(health = 55 , energy = 75)
print(parent.attack(15))
print(parent.energy)