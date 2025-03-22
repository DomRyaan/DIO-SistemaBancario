# O Sistema deve permitir fazer tres operações: Depositar, Sacar e ver o Extrato.
import time

class Conta:
        def __init__(self, nome: str):
              self.nome = nome
              self.saldo = 0
              self.historico = {
                "deposito": {},
                "saque": {}
                }
       
         # Operação Depositar: Não precisa se preocupar com o numero de usuario e etc. O Sistema deve registrar cada deposito em um lista, para ser usado no extrato.
        def depositar(self, valor: float):
                self.saldo += valor
                
                tempoHora = time.localtime().tm_hour
                tempoMinuto = time.localtime().tm_min
                tempoSegundo = time.localtime().tm_sec
                tempo = str(tempoHora) + ":" + str(tempoMinuto) + ":" + str(tempoSegundo)

                self.historico["deposito"][tempo] = valor
                print(f"\nVoce fez o deposito de: R$ {valor} na sua conta")


        # Operação de Saque: O Sistema deve permitir apenas 3 saques por dia
        # o limite do valor de saque é 500 R$. 
        # Se não tiver saldo disponivel, o sistema deverá informar o usuario. 
        # Todos os saques devrão ser armazenados em uma lista.
        def saque(self, valor: float):
                if valor > self.saldo:
                        print("Saldo Insuficiente!")
                else:
                        self.saldo -= valor

                        tempoHora = time.localtime().tm_hour
                        tempoMinuto = time.localtime().tm_min
                        tempoSegundo = time.localtime().tm_sec
                        tempo = str(tempoHora) + ":" + str(tempoMinuto) + ":" + str(tempoSegundo)

                        self.historico["saque"][tempo] = valor


        # Operação de Extrato: Deverá lista e exibir todos os saques e depositos feito na conta.
        # Deverá ser exibido utilizando os seguintes formatos: R$ xxx.xx
        def extrato(self):
                print("\nDepositos: ")
                for i in self.historico["deposito"]:
                        print(f"        Data: {i}, Valor: R$ {self.historico['deposito'][i]:.2f}")

                print("\nSaques: ")
                for i in self.historico["saque"]:
                        print(f"        Data: {i}, Valor: R$ {self.historico['saque'][i]:.2f}")
                print(f"\nSaldo: R$ {self.saldo:.2f}")


def programa():
    global saldo
    print("\n")
    print(" Sistema Bancario ".center(80, "-"))

    nome = input("Digite seu nome: ")
    conta1 = Conta(nome)

    while True:

        opcao = input("""
        \n\tDigite conforme a operacao que deseja fazer:
        \t"s" - Sacar\t"d" - Deposito
        \t"e" - Extrato\t"0" - Sair 
""")

        opcao.lower()

        if opcao == "s":
                valor = float(input("Digite um valor: "))
                if valor < 0:
                        print("Digite um valor valido!")
                else:
                        conta1.saque(valor)
        elif opcao == "d":
                valor = float(input("Digite o valor que deseja depositar: "))
                if valor <= 0:
                       print("Digite um valor valido!")
                else:
                       conta1.depositar(valor)
        elif opcao == "e":
                conta1.extrato()
        elif opcao == "0":
                break
        else:
                print("\nDigite uma opcao valida!\n")

    print(" Fim do Programa ".center(80, "-"))       



programa()