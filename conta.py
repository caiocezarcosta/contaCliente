
class Conta:

    def __init__(self, numero, titular, saldo, limite ):
        print("Construindo Objeto")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    #Retorna o extrato do dono da conta
    def extrato(self):
        print("Saldo {} do titular {}".format(self.__saldo,self.__titular))

    #Realiza o depósito em uma conta
    def deposito(self,valor):
        self.__saldo += self.__valor

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    #Realiza o saque de uma conta
    def sacar(self,valor):
        if(self.__pode_sacar(valor)):
            self.__saldo-=self.__valor
        else:
            print("O valor {} passou o limite ".format(valor))

    #Realiaza a transferência de valor entre contas
    def transferir(self,valor,destino):
        self.sacar(valor)
        destino.deposito(valor)
        print(self.extrato())

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite
    @property
    def titular(self):
        return self.__titular
    @property
    def numero(self):
        return self.__numero
    @limite.setter
    def limite(self,limite):
        self.__limite = limite
    @titular.setter
    def titular(self,titular):
        self.__titular = titular
    @numero.setter
    def numero(self, numero):
        self.__numero = numero

    @staticmethod
    def codigos_bancos():
        return {'BB':'01', 'Caixa' : '104', 'Bradesco':'237'}