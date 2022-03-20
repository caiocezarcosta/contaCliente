
class Cliente:

    def __init__(self,nome):
        self.nome = nome

    @property
    def nome(self):
        print("Chamando @propety nome()")
        return self.nome.title()
    @nome.setter
    def nome(self,nome):
        print("Chamando Nome")
        self.nome = nome