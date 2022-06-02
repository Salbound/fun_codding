# https://www.youtube.com/watch?v=LTXnQdrwyrw&list=PLqnslRFeH2UqLwzS0AwKDKLrpYBKzLBy2&index=3&ab_channel=PythonEngineer

# Dictionary: Key-Value pairs, Unordered, Mutable

#declaração
mydict = {"name": "Max", "age": 28, "city": "New York"}
print(mydict)

mydict2 = dict(name="Mary", age=27, city="Boston")
print(mydict2)


#resgtando por index
print(mydict["name"])

#value = mydict["lastname"]             # Retorno error por não existir no dicionário
#print(value)


#adicionando no dicionário
mydict["email"] = "max@gyiz.com"        # Adiciona se não existe
print(mydict)

mydict["email"] = "maxwell@gyiz.com"    # Atualiza valor se não existe
print(mydict)

#deletando umindex dicionário
del mydict2["name"]
print(mydict2)

mydict2.pop("age")
print(mydict2)


# encontrar algo
if "name" in mydict:            # "var" devolve valor
    print(mydict["name"])

for key in mydict:              # var devolve o nome index
    print(key)

for key in mydict.keys():              
    print(key)

for key in mydict.values():              
    print(key)

for key, value in mydict.items():              
    print(key, value)


# Copiando um dicionário
mydict = {"name": "Max", "age": 28, "city": "New York"}
mydict_ponteiro = mydict                    # ponteiro, não copiando
mydict_cpy = mydict.copy()                  # copiando dicionário
mydict_cpy = dict(mydict)                   # copiando dicionário

mydict_ponteiro["email"] = "max@gasdf.com"
mydict_cpy["email"] = "max@gasdfsdfwef.com"

print(mydict)
print(mydict_ponteiro)
print(mydict_cpy)


# Merging dicionários 
#   (atualiza o que tem, adiciona o que não tem, deixa como está o que não mexeu)

mydict = {"name": "Max", "age": 28, "city": "New York", "email": "max@gdhjsf.com"}
mydict2 = dict(name="Mary", age=27, city="Boston")

mydict.update(mydict2)
print(mydict)


# Index é um nome/valor? Não, é um objeto! Assim como seu valor também.

my_dict = {3: 9, 6: 36, 9: 81}
print(my_dict)
#print(my_dict[0])                  # erro, pois o index não é número como vertor
print(my_dict[3])

mytuple = (8, 7)
my_dict = {mytuple: 15}
print(my_dict)

my_dict = {"index": mytuple}
print(my_dict)

# OBS: Não aceita lista, pois não é um objeto hashable
# OBS*: https://stackoverflow.com/questions/14535730/what-does-hashable-mean-in-python