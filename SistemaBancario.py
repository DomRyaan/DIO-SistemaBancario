# O Sistema deve permitir fazer tres operações: Depositar, Sacar e ver o Extrato.
from datetime import datetime


class Endereco:
        def __init__(self, cidade, estado):
              self.cidade = cidade
              self.estado = estado

        def getCidade(self):
              return self.cidade
        
        def getEstado(self):
               return self.estado

class Cliente:
        clientes = {}
        
        def __init__(self, nome: str, cpf: str, endereco: object, dataNascimento: str):
              self.nome = nome
              self._cpf = cpf
              self.endereco = endereco
              self.dataNascimento = dataNascimento
              self.clientes[cpf] = [nome, endereco.getCidade(), endereco.getEstado(), dataNascimento]


        def getNome(self):
              return self.nome
        
        def getCpf(self):
               return self._cpf
        
        def listaClientes(self):
                for x in self.cliente:
                       print(x)

class Conta:
        def __init__(self, cliente: object):
              self.client = cliente
              self.saldo = 0
              self.historico = {
                "deposito": {},
                "saque": {}
                }
              self.limite = 0
              self.UltimoDiaTransacao = datetime.today().day
       
         # Operação Depositar: Não precisa se preocupar com o numero de usuario e etc. O Sistema deve registrar cada deposito em um lista, para ser usado no extrato.
        def depositar(self, valor: float):
                self.saldo += valor
                
                dataAtual = datetime.now()
                mascara = dataAtual.strftime("%d/%m/%y %H:%M:%S")
                checagem = int(mascara.split('/')[0])
                
                if self.limiteDiario(checagem):
                        self.historico["deposito"][mascara] = valor
                        print(f"\nVoce fez o deposito de: R$ {valor} na sua conta")
                else:
                        print("Deposito atingido o limite diario!")
              


        # Operação de Saque: O Sistema deve permitir apenas 3 saques por dia
        # o limite do valor de saque é 500 R$. 
        # Se não tiver saldo disponivel, o sistema deverá informar o usuario. 
        # Todos os saques devrão ser armazenados em uma lista.
        def saque(self, valor: float):
                if valor > self.saldo:
                        print("Saldo Insuficiente!")
                else:
                        self.saldo -= valor

                        dataAtual = datetime.now()
                        mascara = dataAtual.strftime("%d/%m/%y %H:%M:%S")
                        checagem = int(mascara.split('/')[0])

                        if self.limiteDiario(checagem):
                                self.historico['saque'][mascara] = valor
                        else:
                               print("Saque atingido o limite diario!")
                
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


        def limiteDiario(self, diaTransacao: int):
                if diaTransacao != self.UltimoDiaTransacao:
                        self.limite = 0
                        self.UltimoDiaTransacao = diaTransacao

                if diaTransacao == self.UltimoDiaTransacao:
                      if self.limite < 10:
                             self.limite += 1
                             return True
                      else:
                             return False
        
def programa():
    global saldo
    print("\n")
    print(" Sistema Bancario ".center(80, "-"))

    nome = input("Digite seu nome: ")
    cpf = input("Digite seu CPF: ")
    dataNascimento = input("Digite sua data de nascimento: ")
    cidade = input("Digite sua Cidade: ")
    estado = input("Digite seu estado: ")
    endereco = Endereco(cidade=cidade, estado=estado)
    cliente1 = Cliente(nome, cpf, endereco=endereco, dataNascimento=dataNascimento)
    conta1 = Conta(cliente=cliente1)   

    while True:

        opcao = input("""
        \n\tDigite conforme a operacao que deseja fazer:
        \t"s" - Sacar\t"d" - Deposito
        \t"e" - Extrato\t"c" - Criar Conta
        \t"sair" - Sair 
        """)

        opcao.lower()

        if opcao == "s":
                valor = float(input("Digite um valor: "))
                if valor < 0:
                        print("Digite um valor valido!")
                else:
                        conta1.saque(valor)
        elif opcao == 'l':
               for x in Cliente.clientes:
                      print(f"CPF: {x}, Dados: {Cliente.clientes.get(x)}")
        elif opcao == "d":
                valor = float(input("Digite o valor que deseja depositar: "))
                if valor <= 0:
                       print("Digite um valor valido!")
                else:
                       conta1.depositar(valor)
        elif opcao == "e":
                conta1.extrato()
        elif opcao == "sair":
                break
        else:
                print("\nDigite uma opcao valida!\n")

    print(" Fim do Programa ".center(80, "-"))       


programa()