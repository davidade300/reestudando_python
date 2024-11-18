# Atributos de classe
# atributos primeiro são buscados na instancia da classe e posteriormente na classe em sí


class Pessoa:
    ano_atual = 2024  # atributo da classe

    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade
        # self.ano_atual = 2022 -> isso alteraria a conta

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade
        # return self.ano_atual - idade -> altera resultado


p1 = Pessoa("João", 35)
p2 = Pessoa("Helena", 12)

print(Pessoa.ano_atual)


# altera para todas as instancias pois o valor foi alterado antes
# da chamada de método
Pessoa.ano_atual = 0

print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())


# representação em dicionario da classe
print(p1.__dict__)
print(vars(p1))


# é possível adicionar KV's que não existem na declaração da classe
p1.__dict__["outra"] = "coisa"
p1.__dict__["outra"] = "coisa"

print(p1.__dict__)


# o código abaixo gera erro, pois o dict dados possui uma chave que não corresponde
# a um parametro da classe
"""
dados = {"idade": 45, "outra": "coisa"}
p3 = Pessoa(**dados)  # desempacotamento de dicionários
print(p3.__dict__)
"""

dados = {"nome": "Maria", "idade": 44}
p3 = Pessoa(**dados)
print(p3.__dict__)


# Redefinindo P1
p1 = Pessoa("João_2", 40)
print(vars(p1))
