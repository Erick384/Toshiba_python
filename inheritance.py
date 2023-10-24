class Animal:
    def speak(self):
        print("animal Speaking")


class Dog(Animal):
    def bark(self):
        print("Dog Barks")


class Dogchild(Dog):
    def eats(self):
        print("Drinking milk")

dog= Dog() #this is the object
dog.bark()
dog.speak()
dogMfupi = Dogchild()
dogMfupi.eats()
dogMfupi.bark()
dogMfupi.speak()
