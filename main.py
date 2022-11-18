from turing import *

if __name__ == '__main__':
    #hash
    #transiçoes é um dicionario onde o primeiro indice é o nome do estado e o segundo é o caracter de leitura
    transicoes = {"q0": {'*': estado('*', DIR, 'q0'), 'a': estado('A', DIR, 'q1'), 'B': estado('B', DIR, 'q3'), FINAL: estado(FINAL, DIR, 'q4')},
                  "q1": {'a': estado('a', DIR, 'q1'), 'B': estado('B', DIR, 'q1'), 'b': estado('B', ESQ, 'q2')},
                  "q2": {'a': estado('a', ESQ, 'q2'), 'B': estado('B', ESQ, 'q2'), 'A': estado('A', DIR, 'q0')},
                  "q3": {'B': estado('B', DIR, 'q3'), FINAL: estado(FINAL, DIR, 'q4')},
                  "q4": {}}
    alfa = ['a', 'b']
    finais = ['q4']
    maquina = Turing(alfa, transicoes, 'q0', finais)
    maquina.avalia('aabb')
    maquina.avalia('ab')
    maquina.avalia('aab')

