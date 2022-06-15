#!/usr/bin/python

import sys

class Variable:
    def var_string ():
        str = 'Hello World!'

        print (str)          # Prints complete string
        print (str[0])       # Prints first character of the string
        print (str[2:5])     # Prints characters starting from 3rd to 5th
        print (str[2:])      # Prints string starting from 3rd character
        print (str * 2)      # Prints string two times
        print (str + "TEST") # Prints concatenated string

    def var_list ():
        '''Lista são valores mutaveis, porém com consumo de memória e processamento maior'''
        list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
        tinylist = [123, 'john']

        print (list)          # Prints complete list
        print (list[0])       # Prints first element of the list
        print (list[1:3])     # Prints elements starting from 2nd till 3rd 
        print (list[2:])      # Prints elements starting from 3rd element
        print (tinylist * 2)  # Prints list two times
        print (list + tinylist) # Prints concatenated lists

    def var_tuple ():
        '''Tupla são valores imutáveis, porém com consumo memória e processamento menor '''
        tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
        tinytuple = (123, 'john')

        print (tuple)               # Prints the complete tuple
        print (tuple[0])            # Prints first element of the tuple
        print (tuple[1:3])          # Prints elements of the tuple starting from 2nd till 3rd 
        print (tuple[2:])           # Prints elements of the tuple starting from 3rd element
        print (tinytuple * 2)      # Prints the contents of the tuple twice
        print (tuple + tinytuple)   # Prints concatenated tuples

    def var_dicionario ():
        '''Comumente utilizando como retorno de APIs.'''
        dict = {}
        dict['one'] = "This is one"
        dict[2]     = "This is two"

        tinydict = {'name': 'john','code':6734, 'dept': 'sales'}

        print (dict['one'])       # Prints value for 'one' key
        print (dict[2])           # Prints value for 2 key
        print (tinydict)          # Prints complete dictionary
        print (tinydict.keys())   # Prints all the keys
        print (tinydict.values()) # Prints all the values
    
    def converter_variavel_para_outra ():
        print('''1	int(x [,base])
Converts x to an integer. base specifies the base if x is a string.

2	long(x [,base] )
Converts x to a long integer. base specifies the base if x is a string.

3	float(x)
Converts x to a floating-point number.

4	complex(real [,imag])
Creates a complex number.

5	str(x)
Converts object x to a string representation.

6	repr(x)
Converts object x to an expression string.

7	eval(str)
Evaluates a string and returns an object.

8	tuple(s)
Converts s to a tuple.

9	list(s)
Converts s to a list.

10	set(s)
Converts s to a set.

11	dict(d)
Creates a dictionary. d must be a sequence of (key,value) tuples.

12	frozenset(s)
Converts s to a frozen set.

13	chr(x)
Converts an integer to a character.

14	unichr(x)
Converts an integer to a Unicode character.

15	ord(x)
Converts a single character to its integer value.

16	hex(x)
Converts an integer to a hexadecimal string.

17	oct(x)
Converts an integer to an octal string.''')

if __name__ == "__main__":
    print("Você não deveria estar aqui. Execute o 'main.py' da pasta raiz.")
    sys.exit()