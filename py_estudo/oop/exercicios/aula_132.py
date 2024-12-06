# atributos que começam com um ou dois "_" não devem ser usados fora da classe.


class Caneta:
    def __init__(self, cor: str) -> None:
        # privte protected
        self._cor = cor
        # /\ se  refere a property, indica que o atributo é privado (convenção)

    @property  # faz um método se comportar como atributo, ações podem ser executadas
    def cor(self):
        # print("@property")
        return self._cor

    @cor.setter
    def cor(self, valor):
        self._cor = valor
        # print("setter \n" + valor)

    def mostrar(caneta):
        return caneta.cor


caneta = Caneta(cor="Azul")

caneta.cor = "rosa"
print(caneta.cor)
