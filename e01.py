#-*-coding=utf-8-*-
import os
my_name = 'zeb'
my_height = 78
my_age = 19
my_eyes = 'Blue'

print(f"Let's talk about {my_name}.")
tatal = my_age * 3
print(f"if i {my_name} and age is {my_age}")

types_of_people = 10
x = f"there are {types_of_people} types of people."
binary = "binary"
do_not = "don't"
y = f"those who know {binary} adnd those who {do_not}."

print(x)
print(f"I said: {y}")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"
print(joke_evaluation.format(hilarious))

print(x + y)

print("." * 20)
print("its fleece was white as {}".format("snow"))
print("this end changed", end=' ')
print("see")
