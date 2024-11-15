# mantendo estados dentro da classe


class Camera:
    def __init__(self, nome, filmando=False) -> None:
        self.nome = nome
        self.filmando = filmando

    def filmar(self):
        if self.filmando:
            print(f"{self.nome} já está filmando!")
            return

        print(f"{self.nome} está filmando...")
        self.filmando = True

    def para_filmar(self):
        if not self.filmando:
            print(f"{self.nome} não está filmando!")
            return

        print(f"{self.nome} parou de filmar.")
        self.filmando = False

    def fotografar(self):
        if self.filmando:
            print(f"{self.nome} não pode fotografar enquanto estiver filmando!")
            return

        print(f"{self.nome} está fotografando...")
        self.filmando = True


c1 = Camera("Camera 1")
c2 = Camera("Camera 2")

c1.filmar()

print(c1.filmando)
print(c2.filmando)

c1.filmar()
c1.fotografar()
c1.para_filmar()
c1.fotografar()
print()
c2.para_filmar()
c2.filmar()
c2.para_filmar()
c2.fotografar()
c2.fotografar()
