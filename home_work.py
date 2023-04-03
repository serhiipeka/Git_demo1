class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print("I can run")

dog1 = Dog("Jack", 5)
dog2 = Dog("Snooppy", 7)
print(dog2.name)
dog2.run()


