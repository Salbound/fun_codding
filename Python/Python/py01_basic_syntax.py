#!/usr/bin/python

import sys

class BasicSyntax:
    def string_variables ():
        word = 'word\n'
        sentence = "This is a sentence.\n"
        paragraph = """This is a paragraph. It is
made up of multiple lines and sentences.\n"""
        print(word, sentence, paragraph)
    
    # First comment
    '''
    This is a multiline
    comment.
    '''

    def inputs ():
        resposta = input("\nDigite seu nome: ")
        #on python 2.* it's used 'raw_input()'
        print(f"Respostas: {resposta}")



if __name__ == "__main__":
    print("Você não deveria estar aqui. Execute o 'main.py' da pasta raiz.")
    sys.exit()