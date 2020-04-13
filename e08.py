#-*-coding=utf-8-*-
import os

formatter = "{} {} {} {}"
print(formatter.format(1, 2, 3, 8))
print(formatter.format("try your",
                        "and this",
                        "but not all",
                        "great"
))
print(formatter.format(formatter, formatter, formatter, formatter))

print("""
There's three
line
here
""")


tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* cat food
\t* fishies
\t* catnip\n\t* grass
"""
print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

age = input("how old are you? ")
print(f"so you are {age} old")
