from log import log

INICIO, FINAL = '*', None
ESQ, DIR = -1, 1

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
                prev_state = state
                prev_fita = self.fita[index]
                self.fita[index], next_mov, state = self.transicoes[state][self.fita[index]]
                log.debug(f"estado:{prev_state}->{state}-move:{'DIR' if next_mov == DIR else 'ESQ'} -ler:{prev_fita} escrever:{self.fita[index]} ")
            else:
                log.info(f"rejeita cadeia (estado invalido) '{texto}'!")
                log.info(f"fita: {self.fita}")
                return False
                break
            if self.fita[index] == FINAL:
                break
            else:
                index += next_mov
        if state in self.finais and self.fita[index] == FINAL:
            log.info(f"aceita cadeia '{texto}'!")
            log.info(f"fita: {self.fita}")
            return True
        else:
            log.info(f"rejeita cadeia(ñ final) '{texto}'!")
            log.info(f"fita: {self.fita}")
            return False

