# https://www.youtube.com/watch?v=QLTdOEn79Rc&list=PLqnslRFeH2UqLwzS0AwKDKLrpYBKzLBy2&index=2&ab_channel=PythonEngineer

# Lists: ordered, mutable, allows duplicate elements

#declarações de listas
data_suport_list = [5, True, "text"]
empty_list = list()
mylist = ["first", "middle", "last"]
List_in_for = [i for i  in range(10)]




print(f"Tipos de dados suportado: {data_suport_list}")
print(f"Lista com função vazia: {empty_list}")
print(f"Lista com dados: {mylist}")
print(f"Lista criada com for: {List_in_for}")


#Impressões básicas
print("\nImprimir por ordem.")
print(mylist[0])

for i in mylist:
    print(i)

print("\nImprimir por ordem inversa.")
print(mylist[-1])
print(mylist[-2])

print("\nLista possui item?")
if "first" in mylist:
    print("yes")
else:
    print("no")


######### COMANDOS COM LISTA

print(f"Tamanho da lista: {len(mylist)}")

mylist.append("lemon")
print(mylist)
mylist.insert(2, "apple")
print(mylist)

item_removido = mylist.pop()                #remove último item e armazena se desejar
print(mylist)
print(item_removido)

mylist.remove("apple")                      #remove um dado específico
print(mylist)

mylist.reverse()                            #inverte a ordem da lista
print(mylist)

data_suport_list.clear()                    #Esvazia lista
print(data_suport_list)


num_list = [-5, 4, 2, -6, 2, 1, 0]
print(num_list)
new_num_List = sorted(num_list)             #ordena a nova lista (não altera os valores originais)
print(num_list)
print(new_num_List, "\n")

print(num_list)
num_list.sort()                             #ordena lista (altera dados original)
print(num_list, "\n")

list_preenchida = [0] * 5                   #cria uma lista com a quantidade de valores pré-preenchidos
print(list_preenchida,"\n\n")


######### NAVEGANDO LISTA

print("Navegando e copiando uma lista por index")
big_list = []
for i in range(10):
    big_list.append(i)

new_big_list = big_list[1:5]                #do index 1 ao 5
print(f"Lista -velha{big_list}")
print(f"Lista nova{new_big_list}\n")

new_big_list = big_list[:]                  # do index * até *
print(f"Lista -velha{big_list}")
print(f"Lista nova{new_big_list}\n")

new_big_list = big_list[3:]                 # do index 3 até tudo
print(f"Lista -velha{big_list}")
print(f"Lista nova{new_big_list}\n")

new_big_list = big_list[::1]                # pular de 1 em 1 casa
print(f"Lista -velha{big_list}")
print(f"Lista nova{new_big_list}\n")

new_big_list = big_list[::2]                # pular de 2 em 2 casa
print(f"Lista -velha{big_list}")
print(f"Lista nova{new_big_list}\n")

new_big_list = big_list[::-1]                # pular de 1 em 1 casa invertido
print(f"Lista -velha{big_list}")
print(f"Lista nova{new_big_list}\n")

new_big_list = big_list[::-2]                # pular de 2 em 2 casa invertido
print(f"Lista -velha{big_list}")
print(f"Lista nova{new_big_list}\n")


######### COPIANDO LISTA

# Ponteiro de lista e copiado lista
lista_copiar = ["banana", "cherry", "apple"]
lista_ponteiro = lista_copiar

print(lista_copiar)
print(lista_ponteiro)

lista_ponteiro.append("lemon")              #tanto faz em qual lista adicionar (ponteiro)
print(lista_copiar)
print(lista_ponteiro)

#copiar uma lista (tanto faz o jeito que preferir utilizar)
lista_copia = list(lista_copiar)
lista_copia = lista_copiar[:]

lista_copiar.append("avocado")              
print(lista_copiar)
print(lista_copia)

#copiando valores e realizando calculo antes
big_lista_quadrada = [i*i for i in big_list]
print(big_list)
print(big_lista_quadrada)