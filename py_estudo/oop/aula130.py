# method vs @classmethod vs @staticmethod
# method - self, método de instância
# @classmethod - cls, método de classe
# @staticmethod - método estático (não recebe self nem cls), não acessa nada


class Connection:
    def __init__(self, host="localhost"):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        self.user = user

    def set_password(self, password):
        self.password = password

    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password

        return connection

    @staticmethod
    def soma(x, y):
        return x + y


# c1 = Connection()
c1 = Connection.create_with_auth()

c1.set_user("David")
c1.set_password("123")
print(c1.user)
