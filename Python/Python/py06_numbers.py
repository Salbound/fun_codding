#!/usr/bin/python

import sys
import math
import random

class Number:
    def tipos_variaveis_numericas_e_entradas ():
        print('''int\t\t\tlong\t\t\t\tfloat\t\t\tcomplex
10\t\t\t51924361L\t\t\t0.0\t\t\t3.14j
100\t\t\t-0x19323L\t\t\t15.20\t\t\t45.j
-786\t\t\t0122L\t\t\t\t-21.9\t\t\t9.322e-36j
080\t\t\t0xDEFABCECBDAECBFBAEL\t\t32.3+e18\t\t.876j
-0490\t\t\t535633629843L\t\t\t-90.\t\t\t-.6545+0J
-0x260\t\t\t-052318172735L\t\t\t-32.54e100\t\t3e+26J
0x69\t\t\t-4721885298529L\t\t\t70.2-E12\t\t4.53e-7j\n''')

    def conversao_numericas ():
        print('''Type int(x) -> to convert x to a plain integer.
Type long(x) -> to convert x to a long integer.
Type float(x) -> to convert x to a floating-point number.
Type complex(x) -> to convert x to a complex number with real part x and imaginary part zero.
Type complex(x, y) -> to convert x and y to a complex number with real part x and imaginary part y. x and y are numeric expressions\n''')
    
    def funcoes_matematica ():
        list_ = [5, 2, 3, 7, 1]
        int_ = -42
        float_ = 36.4215

        print("\n@@@ É importante importar a biblioteca 'math' para algumas das funções abaixo. @@@")
        print(f"abs({int_}) ==> {abs(int_)}\t\tThe absolute value of x: the (positive) distance between x and zero.")
        print(f"ceil({int_}) ==> {math.ceil(int_)}\tThe ceiling of x: the smallest integer not less than x.")
        print(f"exp({int_}) ==> {math.exp(int_)}\tThe exponential of x: ex.")
        print(f"fabs({float_}) ==> {math.fabs(float_)}\tThe absolute value of x.")
        print(f"floor({float_}) ==> {math.floor(float_)}\tThe floor of x: the largest integer not greater than x.")
        print(f"log(100.12) ==> {math.log(100.12)}\tThe natural logarithm of x, for x> 0.")
        print(f"log10(100.12) ==> {math.log10(100.12)}\tThe natural logarithm of x, for x> 0.")
        print(f"max({list_}) ==> {max(list_)}\tThe largest of its arguments: the value closest to positive infinity.")
        print(f"min({list_}) ==> {min(list_)}\tThe smallest of its arguments: the value closest to negative infinity.")
        print(f"modf({float_}) ==> {math.modf(float_)}\tThe fractional and integer parts of x in a two-item tuple. \
Both parts have the same sign as x. The integer part is returned as a float.")
        print(f"pow({int_}, 3) ==> {math.pow(int_, 3)}\tThe value of x**y.")
        print(f"round({float_}, 3) ==> {round(float_, 3)}\tThis method returns x rounded to n digits from the decimal point.")
        print(f"sqrt(100) ==> {math.sqrt(100)}\tPython number method sqrt() returns the square root of x for x > 0.")

    def funcoes_random ():
        list_ = [5, 2, 3, 7, 1]

        print("\n@@@ É importante importar a biblioteca 'random' para as funções abaixo. @@@")
        print(f"choice({list_}) ==> {random.choice(list_)}\tPython number method choice() returns a random item from a list, tuple, or string.")
        print(f"randrange({100, 1000, 7}) ==> {random.randrange(100, 1000 ,7)}\tPython number method randrange() returns a randomly selected element\
from range(min, max, step).")
        print(f"random() ==> {random.random()}\Python number method random() returns a random float r, such that 0 is less than or equal to r and r is less than 1.")
        random.shuffle(list_)
        print(f"shuffle([5, 2, 3, 7, 1]) ==> {list_}\tPython number method shuffle() randomizes the items of a list in place. Obs: This method don't return value, it changes the original variable.")
        print(f"uniform(5, 8) ==> {random.uniform(5, 8)}\tPython number method uniform() returns a random float r, such that x is less than or equal to r and r is less than y.")

    def funcoes_trigonometria ():
        print("\n@@@ É importante importar a biblioteca 'math' para algumas das funções abaixo. @@@")
        print(f"cos(3) ==> {math.cos(3)}\tPython number method choice() returns a random item from a list, tuple, or string.")
        print(f"sin(3) ==> {math.sin(3)}\tPython number method sin() returns the sine of x, in radians.")
        print(f"tan(3) ==> {math.tan(3)}\tPython number method tan() returns the tangent of x radians.")
        print(f"hypot(3, 2) ==> {math.hypot(3, 2)}\tPython number method hypot() return the Euclidean norm, sqrt(x*x + y*y).")
        print(f"degrees(pi) ==> {math.degrees(math.pi)}\tPython number method degrees() converts angle x from radians to degrees.")



if __name__ == "__main__":
    print("Você não deveria estar aqui. Execute o 'main.py' da pasta raiz.")
    sys.exit()