# position, name, age, level, salary
se1 = ["Software Engineer", "Max", 20, "Junior", 5000]
se2 = ["Software Engineer", "Lisa", 25, "Senior", 7000]

#class
class SoftwareEngineer:
    # class attribute
    alias = "Keyboard Magician"

    def __init__(self, name, age, level, salary):
        # instance atributes
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary





#instance
se1 = SoftwareEngineer("Max", 20, "Junior", 5000)
print(se1.name, se1.age)
print(se1.alias)
print(SoftwareEngineer)
print(SoftwareEngineer.alias)
se2 = SoftwareEngineer("Lisa", 25, "Senior", 70)
print(se2.name, se2.age)
print(se2.alias)

# Recap
# Create a class (blueprint)
# Create a instance (object)
# Class vs instance
# Instance attributes: defined in __init__(self)