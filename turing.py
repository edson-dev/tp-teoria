from log import log

INICIO = '*'
FINAL = None
DIR = 1
ESQ = -1

class Turing():
    fita = []
    def __init__(self, alfabeto, transicoes, inicial, finais):
        self.alfabeto = alfabeto
        self.transicoes = transicoes
        self.inicial = inicial
        self.finais = finais

    def avalia(self, texto):
        self.fita = [INICIO, *list(texto), FINAL]
        index, state = 0, self.inicial
        while True:
            if state in self.transicoes and self.fita[index] in self.transicoes[state]:
                next_mov, self.fita[index], state = self.transicoes[state][self.fita[index]].get(state, self.fita[index])
            else:
                log.debug("rejeita!")
                return False
                break
            if self.fita[index] == FINAL:
                break
            else:
                index += next_mov
        if state in self.finais and self.fita[index] == FINAL:
            log.debug("aceita!")
            log.debug(f"fita: {self.fita}")
            return True
        else:
            log.debug("rejeita!")
            log.debug(f"fita: {self.fita}")
            return False

class estado():
    def __init__(self, escrever, movimento, proximo):
        self.escrever = escrever
        self.movimento = movimento
        self.proximo = proximo


    def get(self, estado, letra):
        log.debug(f"estado:{estado} -ler:{letra} escrever:{self.escrever}- "
                  f"move: {'Direita' if self.movimento == DIR else 'Esquerda'},proximo:{self.proximo}")
        letra = self.escrever
        return self.movimento, letra, self.proximo

