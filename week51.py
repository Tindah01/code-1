class Smartphone:
    def __init__(self, brand, model, storage_gb, battery_mah):
        self.brand = brand
        self.model = model
        self.storage = storage_gb
        self.battery = battery_mah
        self.is_on = False
        self.apps = []
    
    def power_on(self):
        self.is_on = True
        return f"{self.brand} {self.model} is now powered on!"
    
    def install_app(self, app_name):
        if self.is_on:
            self.apps.append(app_name)
            return f"Installed {app_name} successfully!"
        return "Cannot install apps when phone is off"
    
    def check_storage(self):
        used = len(self.apps) * 0.5  # Assuming each app takes 0.5GB
        available = self.storage - used
        return f"Storage: {used:.1f}GB used, {available:.1f}GB available"
    
    def __str__(self):
        return f"{self.brand} {self.model} ({self.storage}GB, {self.battery}mAh)"


# Inheritance - PremiumSmartphone extends Smartphone
class PremiumSmartphone(Smartphone):
    def __init__(self, brand, model, storage_gb, battery_mah, has_5g, has_water_resistance):
        super().__init__(brand, model, storage_gb, battery_mah)
        self.has_5g = has_5g
        self.has_water_resistance = has_water_resistance
    
    def take_underwater_photo(self):
        if self.has_water_resistance:
            return "📸 Splash! Underwater photo taken!"
        return "This phone isn't waterproof!"
    
    def check_network(self):
        return "5G ready!" if self.has_5g else "4G network available"


# # Example usage
# my_phone = Smartphone("Apple", "iPhone 13", 128, 3095)
# premium_phone = PremiumSmartphone("Samsung", "Galaxy S22", 256, 3700, True, True)

# print(my_phone.power_on()) #checks if phone is ON
# print(my_phone.install_app("Instagram"))# installs app only when phone is ON
# print(my_phone.check_storage())# checks used storage and gives output of remaining storage


#print(premium_phone.take_underwater_photo())# checks if it has taken underwater photo
#print(premium_phone.check_network())# shows if phone is running on 5G


#QUESTION 2:
class Animal:
    def __init__(self, name):
        self.name = name
    
    def move(self):
        raise NotImplementedError("Subclasses must implement move()")


class Dog(Animal):
    def move(self):
        return f"{self.name} the dog is running! 🐕"
    
    def bark(self):
        return "Woof! Woof!"


class Cat(Animal):
    def move(self):
        return f"{self.name} the cat is playing gracefully!"
    
    def bubble(self):
        return "Meow Meow..."


class Bird(Animal):
    def move(self):
        return f"{self.name} the bird is flying high! 🦅"
    
    def tweet(self):
        return "Tweet tweet!"


# Polymorphism in action
animals = [
    Dog("Bosco"),
    Cat("Milo"),
    Bird("Pingu")
]

for animal in animals:
    print(animal.move())
    
    if isinstance(animal, Dog):
        print(animal.bark())
    elif isinstance(animal, Cat):
        print(animal.bubble())
    elif isinstance(animal, Bird):
        print(animal.tweet())
    print()

