# create 2 classes, Ninja and Pet. Ninjas can have a pet, we can even practice inheritance by creating sub-classes of pets

class Ninja:
    def __init__(self, first_name, last_name, pet, treats, pet_food,):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet
    
    def walk(self):
        self.pet.play()
        print(f"I'm walking my pet {self.pet.name}")
        return self
    
    def feed(self):
        if len(self.pet_food) > 0:
            pup_snacks = self.pet_food.pop()
            print(f"I'm Feeding {self.pet.name} {pup_snacks}")
        return self

    def bathe(self):
        self.pet.noise()
        print(f"I'm bathing my pet {self.pet.name}")
        return self


class Pet:
    def __init__(self, name, type, tricks, health, energy, sound):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy
        self.sound = sound

    def sleep(self):
        self.energy += 25
    
    def eat(self):
        self.energy += 5
        self.health += 10
    
    def play(self):
        self.health += 5
    
    def noise(self):
        print(f"{self.sound}")

pet_treats = ['puppy chow', 'cat nip', 'grass', 'fish food']
my_pet_food = ['peanut butter']
Cash_tricks = ['sit', 'lay down', 'speak!', ]

Cash = Pet("Cash", "dog", Cash_tricks, 100, 100, 'woof!')
Garrett = Ninja("Garrett", "Turner", Cash, pet_treats, my_pet_food, )

# Garrett.feed();
Garrett.walk();
# Garrett.bathe();

