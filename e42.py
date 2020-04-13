#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-02-22 21:34:07
# @Author  : ZubinGou (zebgou@gmail.com)
# @Link    : https://github.com/ZubinGou
# @Version : $Id$

import os


# Animal is a object
class Animal(object):
    pass


class Dog(Animal):

    def __init__(self, name):
        self.name = name


class Cat(Animal):
    """docstring for Cat"""
    def __init__(self, name):
        self.name = name


class Person(object):
    def __init__(self, name):
        self.name = name
        self.pet = None


class Employee(Person):

    def __init__(self, name, salary):
        super(Employee, self).__init__(name)
        self.salary = salary

class Fish(object):
    pass

class Salmon(Fish):
    pass

class Halibut(Fish):
    pass

rover = Dog("Rover")

satan = Cat("Satan")

mary = Person("Mary")
mary.pet = satan

frank = Employee("Frank", 999999)
frank.pet = rover

flipper = Fish()
crouse = Salmon()
harry = Halibut()


# super

class FooParent(object):
    def __init__(self):
        self.parent = "I'm the parent."
        print("Parent")

    def bar(self, message):
        print(f"{message} from Parent")


class FooChild(FooParent):
    def __init__(self):
        super(FooChild, self).__init__()
        print("Child")

    def bar(self, message):
        super(FooChild, self).bar(message)
        print("Child bar function")
        print(self.parent)

fooChild = FooChild()
fooChild.bar("Hell super()")

