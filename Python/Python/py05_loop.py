#!/usr/bin/python

import sys

class Loops:
    def while_enquanto ():
        count = 0
        while (count < 9):
            print (f'The count is: {count}')
            count = count + 1

    def while_comElse ():
        count = 0
        while count < 5:
            print (f"{count} is  less than 5")
            count = count + 1
        else:
            print (f"{count} is not less than 5")

    def for_para ():
        # For informar o próximo nível abaixo. Passandro uma String, é separado por letra.
        for letter in 'Python':
            print ('Current Letter :', letter)

        # Passando uma lista, o próximo nível é a String.
            fruits = ['banana', 'apple',  'mango']
        for fruit in fruits:        # Second Example
            print ('Current fruit :', fruit)

    def for_complex_example_prime_number ():
        for num in range(10,20):            #to iterate between 10 to 20
            for i in range(2,num):          #to iterate on the factors of the number
                if num%i == 0:              #to determine the first factor
                    j=num/i                 #to calculate the second factor
                    print (f'{num} equals {i} * {j}')
                    break                   #to move to the next number, the #first FOR
            else:                           # else part of the loop
                print (f'{num} is a prime number')
                break

    def while_complex_example_prime_number ():
        i = 2
        while(i < 100):
            j = 2
            while(j <= (i/j)):
                if not(i%j): break
                j = j + 1
            if (j > i/j) : print (f"{i} is prime.")
            i = i + 1

    def ex_break ():
        for letter in 'Python':     # First Example
            if letter == 'h':
                break
            print (f'Current Letter : {letter}')
            
            var = 10                    # Second Example
            while var > 0:              
                # print (f'Current variable value : {var}')
                var = var -1
                if var == 5:
                    break
        print("\n")

    def ex_continue ():
        for letter in 'Python':     # First Example
            if letter == 'h':
                continue
            print (f'Current Letter : {letter}')

            var = 10                    # Second Example
            while var > 0:              
                var = var -1
                if var == 5:
                    continue
                # print (f'Current variable value : {var}')
        print("\n")

    def ex_pass ():
        for letter in 'Python': 
            if letter == 'h':
                pass
                print ('This is pass block')
            print (f'Current Letter : {letter}')
        print("\n")



if __name__ == "__main__":
    print("Você não deveria estar aqui. Execute o 'main.py' da pasta raiz.")
    sys.exit()