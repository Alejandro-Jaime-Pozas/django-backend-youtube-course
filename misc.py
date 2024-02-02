class ParentClass:
    attribute = "Parent attribute"

class SubClass(ParentClass):
    attribute = "Subclass attribute"
    def __init__(self, ):
        print(super())

# Creating an instance of SubClass
instance = SubClass()

# Accessing the attribute
print(instance.attribute)
