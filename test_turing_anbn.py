from turing import *

def test_turing_anbn_3():
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
   assert maquina.avalia('aaabbb') is True

def test_turing_anbn_2():
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
   assert maquina.avalia('aabb') is True

def test_turing_anbn_1():
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
   assert maquina.avalia('ab') is True

def test_turing_anbn_Fail():
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
   assert maquina.avalia('aab') is False