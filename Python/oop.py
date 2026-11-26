# object, class
# polymerphesiom
# encapsulation
# inheritance 
# abstraction

# area of triangle
# area of circle
# area of rectangle
#  area of square


# class Area:
#     def triangle(self, height, base):
#         self.base = base
#         self.height = height
#         print("Area of Triangle is: ", 0.5 * self.base * self.height)

# a1 = Area()
# a1.triangle(22,30)

# # Polymorphisom (poly means multiple same fun or same method it is having some differnent differnet meaning each and every class implemention is differnent)
# class Cat:
#     def __init__(self, name):
#         self.name = name
#     def display(self):
#         print("Cat's name is", self.name )

# class Dog:
#     def __init__(self, name):
#         self.name = name
#     def display(self):
#         print("Dog's name is", self.name )

# def Show(Animal):
#     Animal.display()

# c1 = Cat("Pinky")
# d1 = Dog("Mani")
# Show(c1)
# Show(d1)

# method overloading and method overriding


# # encapsulation
# class encap:
#     def __init__(self,a):
#         self.__a = a 
#         # private (without __ is public)
#     def display(self):
#         print("Value for a is: ", self.__a)
# e1 = encap(10)
# e1.display()
# e1.a = 100
# e1.display()

# # #  task using (encapsulation)
# # bank == acname
# #         acno
# #         bal === prvt
# # deposit
# # withdraw

# class Bank:
#     def __init__(self,acname, acno, balance):
#         self.acname = acname
#         self.acno = acno
#         self.__balance = balance
#     def deposit(self):
#         print("Account details: ", self.__balance)
#     def withdraw(self):
#         print("Account details: ", self.__balance)

# BANK = Bank('Sneha', 2300 ,58000)



# # Inheritance 
# # Single == single parent, single child
# # multiple == multiple parant, multiple children 
# #  multilevel == A>>B, B<<C
# # hierarical == single parent, multiple children
# #  hybrid ====


# class Employee:
#     def __init__(self, empname, empno):
#         self.empname = empname
#         self.empno = empno
#     def display(self):
#         print("Employee name is: ", self.empname)
#         print("Employee number is: ", self.empno)

# class 





# inheritance


# class Animal():
#     def __init__(self,name):
#         self.name = name
#     def info(self):
#         print("Animal Name is: ", self.name)
# class Dog(Animal):
#     def sound(self):
#         print(self.name, "Barking")

# d = Dog("Buddy")
# d.info()
# d.sound()


# # super()
# class Parent:
#     def show(self):
#         print("this is parent")
# class Child(Parent):
#     def show(self):
#         super().show()
#         print("this is child class")
# obj = Child()
# obj.show()


# from abc import ABC, abstractmethod
# class Absclass(ABC):
#     def print(self,x):
#         print("Passed value: ", x)
#     @abstractmethod
#     def task(self):
#         print("We are inside Absclass task")
 
# class test_class(Absclass):
#     def task(self):
#         print("We are inside test_class task")
 
# class example_class(Absclass):
#     def task(self):
#         print("We are inside example_class task")
 
# #object of test_class created
# test_obj = test_class()
# test_obj.task()
# test_obj.print(100)
 
# #object of example_class created
# example_obj = example_class()
# example_obj.task()
# example_obj.print(200)
 
# print("test_obj is instance of Absclass? ", isinstance(test_obj, Absclass))
# print("example_obj is instance of Absclass? ", isinstance(example_obj, Absclass))

##properties Methods Accessing Properties

# class Person:
#     def __init__(self,name, age):
#         self.name = name
#         self.age = age
#     def get_info(self):
#         return f"{self.name} is {self.age} years old"

# p1 = Person("Tobias", 28)
# print(p1.get_info())

# # methods modify the property
# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def cele_birthday(self):
#         self.age += 1
#         print(f"Happy Birthday {self.name} you are now {self.age}")
# p1 = Person('Sneha', 26)
# p1. cele_birthday()

# # With the __str__() method:
# class new_person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def __str__(self):
#         return f"{self.name} age is {self.age}"
# p1 = new_person('sneha',26)
# print(p1)


# # multiple methods

# class Playlist:
#     def __init__(self,name):
#         self.name = name
#         self.songs = []
#     def add_song(self,song):
#         self.songs.append(song)
#         print(f"Song added - {self.name}")
#     def remove_song(self,song):
#         if self.songs in song:
#             self.songs.remove(song)
#             print(f"Removed: {song}")
#     def show_songs(self):
#         print(f"Playlist '{self.name}':")
#         for song in self.songs:
#              print(f"- {song}")

# my_playlist = Playlist("Favorites")
# my_playlist.add_song("Bohemian Rhapsody")
# my_playlist.add_song("Stairway to Heaven")
# my_playlist.show_songs()



# # __contains__()
# # 
# class person:
#     def __init__(self,name):
#         self.name = name
#     def __contains__(self, name):
#         return name in self.name
# c1 = (['sneha','hema','kashvi'])
# print('prabha' in c1)

# # __call__()
# class click:
#     def __init__(self):
#         self.click = 0
#     def __call__(self):
#         self.click += 1
#         return self.click
# Click = click()
# print(Click(),Click(), Click())
        

# # # Encapsulation - 

# # set private value
# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.__age = age
#     def get_age(self):
#         return self.__age
#     def set_age(self,age):
#         if age > 0:
#             self.__age = age
#         else:
#             print("Age Must me positive")
# a1 = Person('Sneha',27)
# print(a1.get_age())
# a1.set_age(28)
# print(a1.get_age())

# # Protect validating data
# class Student:
#     def __init__(self,name):
#         self.name = name
#         self.__grade = 0
#     def set_grade(self,grade):
#         if 0 <= self.__grade <= 100:
#             self.__grade = grade
#         else:
#             print("Grade must be between 0 to 100 ")
#     def get_grade(self):
#         return self.__grade
#     def get_status(self):
#         if self.__grade >=35:
#             return f"{self.name} is Pass"
#         else:
#             return f"{self.name} is Fail"
# PF = Student("Sneha")
# PF.set_grade(60)
# print(PF.get_grade())
# print(PF.get_status())


# class Person:
#     def __init__(self,age):
#         self.__age = age
#     def page(self):
#         return self.__age
# c1 = Person(26)
# # defalute method
# print(c1.page())
# # mangling
# print(c1._Person__age)




# # Inheritance 

# class Animal:
#     def dog(self):
#         return "Dog is barking"
# class Dog(Animal):
#     pass

# c1 = Dog()
# print(c1.dog())

# # inheritance super()
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def sneha(self):
#         return self.name, self.age
# class employee(Person):
#     def __init__(self,name,age):
#         super().__init__(name,age)

# i1 = employee('sneha',26)
# print(i1.sneha())



# # Polymorphisum
# class car:
#     def __init__(self,model,name):
#         self.model = model
#         self.name = name
#     def tier(self):
#         print("4 wheel")

# class two_wheeler:
#     def __init__(self,model,name):
#         self.model = model
#         self.name = name
#     def tier(self):
#         print("2 wheel")

# class truck:
#     def __init__(self,model,name):
#         self.model = model
#         self.name = name
#     def tier(self):
#         print("n+ wheel")

# car1 = car("Ford", "Mustang")       #Create a Car object
# two_wheeler1 = two_wheeler("Ibiza", "Touring 20") #Create a two_wheeler object
# truck1 = truck("Boeing", "747")     #Create a truck object

# for x in (car1,two_wheeler1,truck1):
#     x.tier()


# # Abstraction
# from abc import ABC, abstractmethod
# class Animal:
#     def sound(self):
#         pass
# class Dog(Animal):
#     def sound(self):
#         print("bark")
# x  = Dog()
# x.sound()

        





