
class Parent(object):

    def altered(self):
        print("parent altered")

class Child(Parent):

    def tered(self):
        print("Child, before altered")
        super(Child, self).altered()
        print("child after altered")

dad = Parent()
son = Child()

dad.altered()
son.tered()
