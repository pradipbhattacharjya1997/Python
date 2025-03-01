class Animal:
    def speak(self):
        print('Animals make sounds')
        
class Dog(Animal):
    def bark(self):
        print('Dogs bark')
        
dog = Dog()
dog.speak()
dog.bark()