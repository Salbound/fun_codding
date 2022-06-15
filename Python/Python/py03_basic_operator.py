#!/usr/bin/python

import sys

class BasicOperator:
    def basico ():
        a = 21
        b = 10
        c = 0

        c = a + b
        print ("Line 1 - Value of c is ", c)

        c = a - b
        print ("Line 2 - Value of c is ", c )

        c = a * b
        print ("Line 3 - Value of c is ", c )

        c = a / b
        print ("Line 4 - Value of c is ", c )

        c = a % b
        print ("Line 5 - Value of c is ", c)

        a = 2
        b = 3
        c = a**b 
        print ("Line 6 - Value of c is ", c)

        a = 10
        b = 5
        c = a//b 
        print ("Line 7 - Value of c is ", c)

    def comparacao ():
        a = 21
        b = 10
        c = 0

        if ( a == b ):
            print ("Line 1 - a is equal to b")
        else:
            print ("Line 1 - a is not equal to b")

        if ( a != b ):
            print ("Line 2 - a is not equal to b")
        else:
            print ("Line 2 - a is equal to b")

        if ( a < b ):
            print ("Line 4 - a is less than b" )
        else:
            print ("Line 4 - a is not less than b")

        if ( a > b ):
            print ("Line 5 - a is greater than b")
        else:
            print ("Line 5 - a is not greater than b")

        a = 5
        b = 20
        if ( a <= b ):
            print ("Line 6 - a is either less than or equal to  b")
        else:
            print ("Line 6 - a is neither less than nor equal to  b")

        if ( b >= a ):
            print ("Line 7 - b is either greater than  or equal to b")
        else:
            print ("Line 7 - b is neither greater than  nor equal to b")


    def assignment_operators ():
        a = 21
        b = 10
        c = 0

        c = a + b
        print ("Line 1 - Value of c is ", c)

        c += a
        print ("Line 2 - Value of c is ", c)

        c *= a
        print ("Line 3 - Value of c is ", c)

        c /= a 
        print ("Line 4 - Value of c is ", c)

        c  = 2
        c %= a
        print ("Line 5 - Value of c is ", c)

        c **= a
        print ("Line 6 - Value of c is ", c)

        c //= a
        print ("Line 7 - Value of c is ", c)

    def identity ():
        a = 20
        b = 20

        if ( a is b ):
            print ("Line 1 - a and b have same identity")
        else:
            print ("Line 1 - a and b do not have same identity")

        if ( id(a) == id(b) ):
            print ("Line 2 - a and b have same identity")
        else:
            print ("Line 2 - a and b do not have same identity")

        b = 30
        if ( a is b ):
            print ("Line 3 - a and b have same identity")
        else:
            print ("Line 3 - a and b do not have same identity")

        if ( a is not b ):
            print ("Line 4 - a and b do not have same identity")
        else:
            print ("Line 4 - a and b have same identity")


if __name__ == "__main__":
    print("Você não deveria estar aqui. Execute o 'main.py' da pasta raiz.")
    sys.exit()