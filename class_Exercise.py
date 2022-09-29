#create a scorpion class that inherits from monster
# health and energy from the parent
# poison_damage attribute
# overwrite the damage method to show poison damage

class Monster:
    
    def __init__(self, health, energy, **kwargs):
        self.health = health
        self.energy = energy
        super().__init__(**kwargs)
     
    def damage(self, damage):
        print(f'The damage caused in value is {damage}') 
        #self.damage = self.poison_damage
class Child:
    def __init__(self, speed, power): 
        self.speed = speed
        self.power = power
        
        
    def move(self, speed):
        print("The monster has moved!")
        print(f"It moved with a speed of {speed}")

class Scorpion(Monster, Child):
    def __init__(self, poison_damage, health, energy, speed, power) -> None:
        self.poison_damage = poison_damage
        super().__init__(health = health, energy = energy, speed = speed, power = power)
        #super().damage(15)
    
    def damage(self):
        print(f"This is the new damage in value {self.poison_damage}")

scorpion = Scorpion(poison_damage = 300, health = 150, energy = 250, speed = 200, power = 500)
print(scorpion.poison_damage)
monster = Monster(health = 200, energy = 300)
print(monster.damage(20))
print(scorpion.damage())
#print(Scorpion.mro())
print(scorpion.power)
print(scorpion.speed)