class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def description(self):
        print(f"Name: {self.name}, \nAge: {self.age}")

    def get_info(self):
        print(f"Coat Color: {self.coat_color}")

class JackRussellTerrier(Dog):
    def __init__(self, name, age, coat_color, energy_level):
        super().__init__(name, age, coat_color)
        self.energy_level = energy_level

    def special_ability(self):
        print(f"{self.name} has a special ability: High Energy Level")

    def play_fetch(self):
        print(f"{self.name} loves to play fetch!")

class Bulldog(Dog):
    def __init__(self, name, age, coat_color, wrinkles):
        super().__init__(name, age, coat_color)
        self.wrinkles = wrinkles

    def snore(self):
        print(f"{self.name} is known for its snoring.")

    def guard_dog(self):
        print(f"{self.name} makes an excellent guard dog.")

# Create Dog objects

dog1 = JackRussellTerrier("Buddy", 2, "White", "Very High")
dog2 = Bulldog("Max", 5, "Fawn", "Lots of Wrinkles")



print("\nJack Russell Terrier:")
dog1.description()
dog1.get_info()
dog1.special_ability()
dog1.play_fetch()

print("\nBulldog:")
dog2.description()
dog2.get_info()
dog2.snore()
dog2.guard_dog()
