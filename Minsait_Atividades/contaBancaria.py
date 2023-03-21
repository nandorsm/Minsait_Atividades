class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        

    def sacar(self, valor):
        # EU NÃO POSSO SACAR UM VALOR MAIOR QUE O MEU SALDO
        if (valor <= self.saldo):
            self.saldo -= valor
        else:
            print("Valor do saldo insuficiente")
        

    def consultar_saldo(self):
        print(f"Saldo atual: R${self.saldo:.2f}")

pessoa = ContaBancaria(titular="fernando", saldo=0)
pessoa.depositar(40)
pessoa.consultar_saldo()
pessoa.sacar(20)
pessoa.consultar_saldo()
pessoa.sacar(50)
pessoa.consultar_saldo()
