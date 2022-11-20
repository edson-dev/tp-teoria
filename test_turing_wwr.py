from turing import *

def test_turing_wwr():
    transicoes = {"q0": {'*': ('*', DIR, 'q0'),
                         'a': ('A', DIR, 'q1'),
                         'b': ('B', DIR, 'q4'),
                         'A': ('A', DIR, 'q0'),
                         'B': ('B', DIR, 'q0'),
                         FINAL: (FINAL, DIR, 'qf')},
                  "q1": {'a': ('a', DIR, 'q1'),
                         'b': ('b', DIR, 'q1'),
                         'A': ('A', DIR, 'q1'),
                         'B': ('B', DIR, 'q1'),
                         FINAL: (FINAL, ESQ, 'q2')},
                  "q2": {'A': ('A', ESQ, 'q2'),
                         'B': ('B', ESQ, 'q2'),
                         'a': ('A', ESQ, 'q3')},
                  "q3": {'a': ('a', ESQ, 'q3'),
                         'b': ('b', ESQ, 'q3'),
                         'A': ('A', ESQ, 'q3'),
                         'B': ('B', ESQ, 'q3'),
                         '*': ('*', DIR, 'q0')},
                  "q4": {'a': ('a', DIR, 'q4'),
                         'b': ('b', DIR, 'q4'),
                         'A': ('A', DIR, 'q4'),
                         'B': ('B', DIR, 'q4'),
                         FINAL: (FINAL, ESQ, 'q5')},
                  "q5": {'A': ('A', ESQ, 'q5'),
                         'B': ('B', ESQ, 'q5'),
                         'b': ('B', ESQ, 'q3')},
                  "qf": {}}
    alfabeto = ['a', 'b']
    finais = ['qf']
    maquina = Turing(alfabeto, transicoes, 'q0', finais)
    assert maquina.avalia('babbab') is True

def test_turing_wwr_2():
    transicoes = {"q0": {'*': ('*', DIR, 'q0'),
                         'a': ('A', DIR, 'q1'),
                         'b': ('B', DIR, 'q4'),
                         'A': ('A', DIR, 'q0'),
                         'B': ('B', DIR, 'q0'),
                         FINAL: (FINAL, DIR, 'qf')},
                  "q1": {'a': ('a', DIR, 'q1'),
                         'b': ('b', DIR, 'q1'),
                         'A': ('A', DIR, 'q1'),
                         'B': ('B', DIR, 'q1'),
                         FINAL: (FINAL, ESQ, 'q2')},
                  "q2": {'A': ('A', ESQ, 'q2'),
                         'B': ('B', ESQ, 'q2'),
                         'a': ('A', ESQ, 'q3')},
                  "q3": {'a': ('a', ESQ, 'q3'),
                         'b': ('b', ESQ, 'q3'),
                         'A': ('A', ESQ, 'q3'),
                         'B': ('B', ESQ, 'q3'),
                         '*': ('*', DIR, 'q0')},
                  "q4": {'a': ('a', DIR, 'q4'),
                         'b': ('b', DIR, 'q4'),
                         'A': ('A', DIR, 'q4'),
                         'B': ('B', DIR, 'q4'),
                         FINAL: (FINAL, ESQ, 'q5')},
                  "q5": {'A': ('A', ESQ, 'q5'),
                         'B': ('B', ESQ, 'q5'),
                         'b': ('B', ESQ, 'q3')},
                  "qf": {}}
    alfabeto = ['a', 'b']
    finais = ['qf']
    maquina = Turing(alfabeto, transicoes, 'q0', finais)
    assert maquina.avalia('abaaba') is True

def test_turing_wwr_fail():
    transicoes = {"q0": {'*': ('*', DIR, 'q0'),
                         'a': ('A', DIR, 'q1'),
                         'b': ('B', DIR, 'q4'),
                         'A': ('A', DIR, 'q0'),
                         'B': ('B', DIR, 'q0'),
                         FINAL: (FINAL, DIR, 'qf')},
                  "q1": {'a': ('a', DIR, 'q1'),
                         'b': ('b', DIR, 'q1'),
                         'A': ('A', DIR, 'q1'),
                         'B': ('B', DIR, 'q1'),
                         FINAL: (FINAL, ESQ, 'q2')},
                  "q2": {'A': ('A', ESQ, 'q2'),
                         'B': ('B', ESQ, 'q2'),
                         'a': ('A', ESQ, 'q3')},
                  "q3": {'a': ('a', ESQ, 'q3'),
                         'b': ('b', ESQ, 'q3'),
                         'A': ('A', ESQ, 'q3'),
                         'B': ('B', ESQ, 'q3'),
                         '*': ('*', DIR, 'q0')},
                  "q4": {'a': ('a', DIR, 'q4'),
                         'b': ('b', DIR, 'q4'),
                         'A': ('A', DIR, 'q4'),
                         'B': ('B', DIR, 'q4'),
                         FINAL: (FINAL, ESQ, 'q5')},
                  "q5": {'A': ('A', ESQ, 'q5'),
                         'B': ('B', ESQ, 'q5'),
                         'b': ('B', ESQ, 'q3')},
                  "qf": {}}
    alfabeto = ['a', 'b']
    finais = ['qf']
    maquina = Turing(alfabeto, transicoes, 'q0', finais)
    assert maquina.avalia('ababa') is False