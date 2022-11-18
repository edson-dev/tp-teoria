from turing import *

if __name__ == '__main__':
    # transições é um dicionario onde o primeiro indice
    # é o nome do estado e o segundo é o caracter de leitura
    transicoes = {"q0": {'*': ('*', DIR, 'q0'),
                         'a': ('A', DIR, 'q1'),
                         'B': ('B', DIR, 'q3'),
                         FINAL: (FINAL, DIR, 'q4')},
                  "q1": {'a': ('a', DIR, 'q1'),
                         'b': ('B', ESQ, 'q2'),
                         'B': ('B', DIR, 'q1')},
                  "q2": {'a': ('a', ESQ, 'q2'),
                         'A': ('A', DIR, 'q0'),
                         'B': ('B', ESQ, 'q2')},
                  "q3": {'B': ('B', DIR, 'q3'),
                         FINAL: (FINAL, DIR, 'q4')},
                  "q4": {}}
    alfabeto = ['a', 'b']
    finais = ['q4']
    maquina = Turing(alfabeto, transicoes, 'q0', finais)
    maquina.avalia('aabb')
    maquina.avalia('ab')
    maquina.avalia('aab')
