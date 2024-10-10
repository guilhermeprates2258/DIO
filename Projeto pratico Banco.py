class ContaBancaria:
    def __init__(self):
        self.saldo = 0.0
        self.depositos = []
        self.saques = []
        self.saques_realizados = 0
        self.limite_saque = 500.00
        self.limite_diario_saque = 3

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.depositos.append(valor)
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        if self.saques_realizados < self.limite_diario_saque:
            if valor <= self.saldo and valor <= self.limite_saque:
                self.saldo -= valor
                self.saques.append(valor)
                self.saques_realizados += 1
                print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
            elif valor > self.saldo:
                print("Não é possível sacar. Saldo insuficiente.")
            else:
                print("O valor do saque deve ser até R$ 500,00.")
        else:
            print("Limite de saques diários atingido.")
            print("")

    def visualizar_extrato(self):
        if not self.depositos and not self.saques:
            print("Não foram realizadas movimentações.")
        else:
            print("Extrato:")
            for deposito in self.depositos:
                print(f"Depósito: R$ {deposito:.2f}")
            for saque in self.saques:
                print(f"Saque: R$ {saque:.2f}")
            print(f"Saldo atual: R$ {self.saldo:.2f}")


def menu():
    conta = ContaBancaria()
    while True:
        print("\n--- Sistema Bancário ---")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Visualizar Extrato")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            valor_deposito = float(input("Digite o valor do depósito: R$ "))
            conta.depositar(valor_deposito)
        elif opcao == "2":
            valor_saque = float(input("Digite o valor do saque: R$ "))
            conta.sacar(valor_saque)
        elif opcao == "3":
            conta.visualizar_extrato()
        elif opcao == "4":
            print("Saindo do sistema. Até mais!")
            break
        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    menu()
