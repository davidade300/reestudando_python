"""
Métodos de classe + factories são métodos onde "self" será "cls", ou seja,
em vez de receber a instancia no primeiro parâmetro, receberemos a própria
classe
"""


class Pessoa:
    ano = 2024  # atributo da classe

    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano - self.idade

    @classmethod  # com esse decorator, o método passa a ser um método de classe
    def metodo_de_classe(cls):
        print("hey")

    @classmethod
    def criar_com_50_anos(cls, nome: str):  # factory method
        """
        cria uma nova Pessoa com um nome=nome e idade de 50 anos
        pode ser utilizado para criar objetos a partir de lógica arbitraria
        """
        return cls(nome, 50)

    @classmethod
    def criar_sem_nome(cls, idade: int):
        return cls("Anônimo", idade)


p1 = Pessoa("João", 34)
p2 = Pessoa.criar_com_50_anos("Helena")
p3 = Pessoa.criar_sem_nome(23)
print(p1.nome, p1.idade)
print(p2.nome, p2.idade)
print(p3.nome, p3.idade)
