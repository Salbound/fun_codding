# _salary = protected variable, que significa pode ser acessada fora da classe mas não alterada
# __salary = private variable, que significa que não pode ser acessada fora da classe

class SoftwareEngineer:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._salary = None
        self._num_bug_resolved = 0

    # Getter
    def get_salary(self):
        return self._salary

    # Setter
    def set_salary(self, base_value):
        self._salary = self._calculated_salary(base_value)

    def _calculated_salary(self, base_value):
        if self._num_bug_resolved < 10:
            return base_value
        if self._num_bug_resolved < 100:
            return base_value * 2
        return base_value * 3

    def code(self):
        self._num_bug_resolved += 1


# Instanciar a classe e verificar os dados
se = SoftwareEngineer("Max", 25)
#print(se.name, se.age, se._salary)          # Por ser protegido é acessada. Privado não é acessado


# Vamos alimentar o valor da classe por fora para testar
for i in range(70):
    se.code()
# print(se._num_bug_resolved)


# Salário do set está passando por uma regra de negócio antes de ser setado.
se.set_salary(6000)
print(se.get_salary())

# Abstraction: 
# A abstração é o ponto de partida para a criação de programas utilizando POO. 
# Trata-se da capacidade de extrair dos personagens ou dos itens presentes no contexto, 
# suas principais características, criando, dessa forma, objetos.

# set_salary(6000) retorna 12000 por ser >10 erros e <100 erros concertados. 
# A pessoa que informa não sabe como o código funciona, mas compreende sua funcionalidade em relação ao mundo real, 
# fazendo assim a abstração da informação.


#Recap:
# Encapsulation
# Abstraction
# public, protected and private (ex: _foo(), _x)
# getter and setter
