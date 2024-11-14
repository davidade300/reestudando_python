# Escopo da classe e de metodos de classe
# a não ser que algo seja passado no escopo do self,
# não é possível utilizar parametros de outras funções em uma função de classe


class Animal:
    # nome = "Leão"

    def __init__(self, nome):
        self.nome = nome

        variavel = "valor"
        print(variavel)

    # def acao(self):
    # print(variavel)  a variavel no contexto do init so é acessavel no init
    # já o self.nome é do contexto da classe
    #
    def acao(self):
        return f"{self.nome} está executando uma ação!"

    def comendo(self, alimento):
        return f"{self.nome} esta comendo {alimento}"

    def executar(self, *args, **kwargs):
        self.comendo(*args, **kwargs)


leao = Animal("Leão")
print(leao.nome)
leao.acao()
