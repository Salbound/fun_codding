#!/usr/bin/python

import sys
from py01_basic_syntax import BasicSyntax
from py02_variable import Variable
from py03_basic_operator import BasicOperator
from py04_decision import DecisaoIfElse
from py05_loop import Loops
from py06_numbers import Number

def run():
    '''Conceitos básicos de Python, diferença de palavra/texto/paragrafo em uma var string e informar valores de entrada.'''
    # bs = BasicSyntax
    # bs.string_variables()
    # bs.inputs()

    '''Conceitos básicos sobre variavél, e seus tipos.'''
    # var = Variable
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
    # oper = BasicOperator
    # oper.basico()
    # oper.comparacao()
    # oper.assignment_operators()
    # oper.identity()

    '''Conceitos básicos sobre tomada de decisões (IF ELIF ELSE).'''
    # seSenao = DecisaoIfElse
    # seSenao.ifelse()
    # seSenao.ifelifelse()
    # seSenao.if_dentroDeIf()

    '''Conceitos básicos de loop (while e for).
            break: interrompe próximas iterações do for/while;
            continue: quebra essa iteração e vai direto para próxima iteração;
            pass: não faz nada relacionado a essa iteração, e pode executar demais códigos dentro no local.'''
    # loop = Loops
    # loop.while_enquanto()
    # loop.while_comElse()
    # loop.for_para()
    # loop.for_complex_example_prime_number()
    # loop.while_complex_example_prime_number()
    # loop.ex_break()
    # loop.ex_continue()
    # loop.ex_pass()

    '''Conceitos básicos sobre números.
            números: tipos de variavbeis numéricas (int, long, float e complex);
            matemática: principais funções envolvendo matemática;
            random: números randômicos, embaralhar list/tuples e intervalos
            trigonometria: sen, cos, tan, hipot e ângulo'''
    # nb = Number
    # nb.tipos_variaveis_numericas_e_entradas()
    # nb.conversao_numericas()
    # nb.funcoes_matematica()
    # nb.funcoes_random()
    # nb.funcoes_trigonometria()


if __name__ == "__main__":
    run()
    sys.exit()