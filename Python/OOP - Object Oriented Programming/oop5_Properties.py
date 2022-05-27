# _salary = protected variable, que significa pode ser acessada fora da classe mas não alterada
# __salary = private variable, que significa que não pode ser acessada fora da classe

# ___________________________________________________________________________________________________________________________
#OBS: Esse conceito existe em Python para ser utilizado, porém nunca é utilizado. Serve mais esse tópico como uma curiosidade
# ___________________________________________________________________________________________________________________________

class SoftwareEngineer:
    def __init__(self):
        self._salary = None

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        self._salary = value

    # @salary.deleter
    # def salary(self, value):
    #     del self._salary



se = SoftwareEngineer()

se.salary = 6000
print(se.salary)
#del se.salary
print(se.salary)        # descomentando buga o código, pois apagou a propriedade salary da classe


# Recape:
# Forma diferente através de propriedade para getter and setter
# getter -> @property
# setter -> @x.setter