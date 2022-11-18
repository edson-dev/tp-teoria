from log import log

INICIO = '*'
FINAL = None
DIR = 1
ESQ = -1
class Turing():
    fita = []
    def __init__(self, alfabeto, estados, inicial, finais):
        self.alfabeto = alfabeto
        self.estados = estados
        self.inicial = inicial
        self.finais = finais

    def avalia(self, texto):
        self.fita = [INICIO, *list(texto), FINAL]
        index, state = 0, maquina.inicial
        while True:
            if state in transicoes and maquina.fita[index] in transicoes[state]:
                next_mov, maquina.fita[index], state = transicoes[state][maquina.fita[index]].get(state, maquina.fita[index])
            else:
                log.debug("rejeita!")
                return False
                break
            if maquina.fita[index] == FINAL:
                break
            else:
                index += next_mov
        if state in finais and maquina.fita[index] == FINAL:
            log.debug("aceita!")
            log.debug(maquina.fita)
            return True

class estado():
    def __init__(self, escrever, movimento, proximo):
        self.escrever = escrever
        self.movimento = movimento
        self.proximo = proximo


    def get(self, estado, letra):
        log.debug(f"estado:{estado} ,ler:{letra} escrever:{self.escrever} "
                  f"proximo:{self.proximo} move: {'Direita' if self.movimento == DIR else 'Esquerda' }")
        letra = self.escrever
        return self.movimento, letra, self.proximo


if __name__ == '__main__':
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
    maquina.avalia('abab')

