# position, name, age, level, salary
se1 = ["Software Engineer", "Max", 20, "Junior", 5000]
se2 = ["Software Engineer", "Lisa", 25, "Senior", 7000]
se3 = ["Software Engineer", "Lisa", 25, "Senior", 7000]
d1 = ["Designer", "Philipp"]



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

    # Instance method
    def code(self):
        print(f"{self.name} is writing code...")

    def code_in_language(self, language):
        print(f"{self.name} is writing code in {language}")

    #Função do Python, __str__ o qual transforma o __name__ do arquivo e devolve como tipo "String"
    #Dunder method
    def __str__(self):
        information = f"name = {self.name}, age = {self.age}, level = {self.level}"
        return information

    #Função do Ptthon, __eq __ verifica se parâmetros são iguais e retorno True ou False como valor
    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    def entry_salary(age):
        if age < 25:
            return 5000
        if age < 30:
            return 7000
        return 9000

    @staticmethod
    def entry_salary_static(age):
        if age < 25:
            return 5000
        if age < 30:
            return 7000
        return 9000


#instance
se1 = SoftwareEngineer("Max", 20, "Junior", 5000)
se2 = SoftwareEngineer("Lisa", 25, "Senior", 70)
se3 = SoftwareEngineer("Lisa", 25, "Senior", 70)


#method call
se1.code()
se2.code()
se1.code_in_language("Python")
se2.code_in_language("Java")


#Métodos específicos do python
print(se1)                  #__str___
print(se2.__eq__(se3))      #__eq__


# print(se1.entry_salary(24))  <-- Method sem self não funciona instanciado, pois essa função só funciona dentro da classe
print(SoftwareEngineer.entry_salary(27))    #sem o self pode ser chamado sem instanciar a classe

print(se1.entry_salary_static(24))                  #Como método estático, funciona em ambos casos, porém não é possível chamar nenhum atributo da classe (ex: self.age)
print(SoftwareEngineer.entry_salary_static(27))     

#Recap
#Instance method(self)
#Methods can take Arguments and can return values
#special "dunder" methos (_)_str__ and __eq__)
#@staticmethod

# ---------------------------------------------------------------------------------------------------------------------------------------

# @staticsmethod são extensões de funções (extend em outras linguagens)
# Exemplo

import functools

def my_decorator(func):

    @functools.wraps(func)
    def add_value(*args, **kwargs):
        # faça algo...
        result = func(*args, **kwargs)
        return result
    return add_value

@my_decorator
def add(x):
    return x + 5

print(add(5))

#Função add(5), está agora extendendo a função my_decorator, chamando ela e retornando resultado.
# https://www.youtube.com/watch?v=FXUUSfJO_J4&ab_channel=PythonEngineer