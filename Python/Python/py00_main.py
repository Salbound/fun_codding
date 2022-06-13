#!/usr/bin/python

import sys
from py01_basic_syntax import basicSyntax
from py02_variable import variable
from py03_basic_operator import basicOperator

def run():
    '''Conceitos básicos de Python, diferença de palavra/texto/paragrafo em uma var string e informar valores de entrada.'''
    # bs = basicSyntax
    # bs.string_variables()
    # bs.inputs()

    '''Conceitos básicos sobre variavél, e seus tipos.'''
    # var = variable
    # var.var_string()
    # var.var_list()
    # var.var_tuple()
    # var.var_dicionario()
    # var.converter_variavel_para_outra()

    '''Conceitos básicos sobre operadores.
    Operações básicas: + - * / % ** //
    Comparação: == != < > >= <=
    Assignments: = += -= *= /= %= **= //=
    Logicos:
        Lógicos: and or not
        Membership: in not in
        Identiyy: is is not'''
    # oper = basicOperator
    # oper.basico()
    # oper.comparacao()
    # oper.assignment_operators()
    # oper.identity()

if __name__ == "__main__":
    run()
    sys.exit()