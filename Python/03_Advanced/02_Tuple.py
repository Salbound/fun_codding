# Tuple: ordered, immutable, allows duplicate elementes

mytuple = ("Max", 28, "Boston")
print(mytuple)

mytuple1 = ("Max",)                     # Criar tupla com tipo, é preciso por a virgula ou ele entende como String
print(mytuple1)

mytuple = tuple(["Max", 28, "Boston"])  # Outra forma de criar
print(mytuple)

item = mytuple[0]
print(item)

item = mytuple[-1]
print(item)

for x in mytuple:
    print(x)

#mytuple[0] = "Tim"                # Tupla é imutavel, não é permitido mudar informação

if "Max" in mytuple:
    print("Yes")
else:
    print("No")


##### Métodos

mytuple = ('a', 'p', 'p', 'l', 'e')
print(len(mytuple))                     # Tamanho do objeto
print(mytuple.count('p'))               # Quantas vezes repete valor
print(mytuple.index('p'))               # Index do primeiro encontrado
#print(mytuple.index('o'))               # valor inexistente da error


##### Converter tupla -> list <-> list -> tupla
mytuple = ('a', 'p', 'p', 'l', 'e')
my_list = list(mytuple)
print(f"Agora é uma lista: {my_list}")

my_tuple = tuple(my_list)
print(f"Agora é uma tupla: {my_tuple}")



### Percorrer tuppla

# O método é igual para lista, copiando os valores para uma nova variavel \
# e assim permitindo escolher o tipo de dados, e intervalo
# [ini:fim]
# [::saltos]
# [:-invertido]

percorrer_tupla = mytuple[:]
percorrer_tupla = mytuple[1:3]
percorrer_tupla = mytuple[:3]
percorrer_tupla = mytuple[2:]
percorrer_tupla = mytuple[::1]
percorrer_tupla = mytuple[::2]
percorrer_tupla = mytuple[::-1]
percorrer_tupla = mytuple[::-2]
print(f"Modelo escolhido: {percorrer_tupla}")

### Unpack a tupla
mytuple = ("Max", 28, "Boston")
name, age, city = mytuple
print(name)
print(age)
print(city)