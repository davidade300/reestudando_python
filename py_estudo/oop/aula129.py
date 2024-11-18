"""
@staticmethods
são métodos que estão dentro da classe, mas não tem acesso ao "self" nem ao "cls".
Ou seja, são apenas funções que existem dentro da classe
"""


class Classe:
    @staticmethod
    def funcao_que_esta_na_classe(*args, **kwargs):
        print("oi", args, kwargs)


def funcao(*args, **kwargs):
    print("oi", args, kwargs)


c1 = Classe()
c1.funcao_que_esta_na_classe(1, 2, 3)
Classe.funcao_que_esta_na_classe(nomeado=1)
funcao(nomeado=1)
