## You can Inherits, extend, override
## Obs: 'CTRL + ;' comenta e descomenta blocos no VisualCode
## Obs2: O código final não está comentado e possui as funcionalidades. Os códigos divididos em bloco é para ajudar a estudar no futuro e compreender de forma simples

# # @Inherits example.
# class Employee:
#     def __init__(self, name, age, salary):
#         self.name = name
#         self.age = age

#     def work(self):
#         print(f"{self.name} is working...")

# class SoftwareEngineer(Employee):
#     pass

# class Designer(Employee):
#     pass

# se = SoftwareEngineer("Max", 25, 5000)
# se.work()

# d = Designer("Philipp", 27, 7000)
# d.work()

# -----------------------------------------------------------------------------------------

# # @Extend example.
# class Employee:
#     def __init__(self, name, age, salary):
#         self.name = name
#         self.age = age
#         self.salary = salary

#     def work(self):
#         print(f"{self.name} is working...")

# class SoftwareEngineer(Employee):
#     def __init__(self, name, age, salary, level):
#         super().__init__(name, age, salary)         # super() significa que está chamando o método da herança pai como extensão
#         self.level = level

#     def debug(self):
#         print(f"{self.name} is debugging...")

# class Designer(Employee):
#     def draw(self):
#         print(f"{self.name} is drawing...")

# se = SoftwareEngineer("Max", 25, 5000, "Junior")
# se.work()
# print(se.level)
# se.debug()

# d = Designer("Philipp", 27, 7000)
# d.work()
# d.draw()

# -----------------------------------------------------------------------------------------

# @Override example (polymorphismo)
class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def work(self):
        print(f"{self.name} is working...")

class SoftwareEngineer(Employee):
    def __init__(self, name, age, salary, level):
        super().__init__(name, age, salary)         # super() significa que está chamando o método da herança pai como extensão e adicionando os demais atributos abaixo
        self.level = level

    def work(self):                                 # Método sobrescrito polymorphismo (Override)
        print(f"{self.name} is coding...")

    def debug(self):
        print(f"{self.name} is debugging...")

class Designer(Employee):
    def work(self):                                 # Método sobrescrito polymorphismo (Override)
        print(f"{self.name} is designing...")

    def draw(self):
        print(f"{self.name} is drawing...")

se = SoftwareEngineer("Max", 25, 5000, "Junior")
# se.work()

d = Designer("Philipp", 27, 7000)
# d.work()


# Polymorphismo na prática

employees = [SoftwareEngineer("Max", 25, 5000, "Junior"),
            SoftwareEngineer("Lisa", 30, 6000, "Senior"),
            Designer("Philipp", 27, 7000)]

# longe do código.... Alguém resolve chamar as funções da lista criada

def motivate_employees(employees):
    for employer in employees:
        employer.work()

motivate_employees(employees)

#Recap:
# Inheritance, ClildClass(BaseClass)
# Inherit, extend, overrid
# super().__init__() para extender uma classe junto com conceito da herança
# Polymorphismo