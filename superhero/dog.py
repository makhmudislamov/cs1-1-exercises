class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print("Woof")


my_dog = Dog("Rex", "SuperDog")
# print(my_dog)
print(my_dog.breed)

