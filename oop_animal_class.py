class Animal():
    def __init__(self,name, age): #constructor method runs whenever an instances is created
        self.name = name
        self.species = 'Lizzard'
        self.age = age
        self.alive = True
        self.number_animal_eaten = 0

# class are the basis of OOP.
# They are cookie cutters for objects
# from classes you initialize individual instances od this class
# classes hold methods
# methods are functions that depend on instances of classes. They can only be called on instances of a class

#method for class object - instances
    def sleep(self):
        return "zzzzzz"#self refers to the instance if get called upon - self populated the self populates the self with the instance


    def eat(self,food):
        return 'nom NOM nom NOM this was some good ' + food

    def potty(self):
        return "...... ..... uhhh 0.o --- SLPoGH!"

animal_1 = Animal() #creating one instance of class animal
#print(animal_1)
#print(type(animal_1))


print(animal_1.sleep())
print(animal_1.eat('meat salad'))
print(animal_1.potty())

#Accsseing properties of instancea of animal

print(animal_1.name)
print(animal_1.age)