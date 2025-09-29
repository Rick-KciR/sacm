from abc import ABC, abstractmethod

lista_funcionarios = []
# Classe Abstrata: Rep
# representa a abstração de um funcionário genérico
class Funcionario(ABC):
    def __init__(self, nome, salario_base):
        # Encapsulamento: Atributos privados
        self.__matricula = len(lista_funcionarios) + 1
        self.__nome = nome
        self.__salario_base = salario_base
        self.__imposto_renda = 0.11
        self.__inss = 0.08
        self.__sindicato = 0.05
        self.__total_imposto = 0.24
        
    
    def get_imposto_renda(self):
        return self.__imposto_renda
    
    def get_inss(self):
        return self.__inss
    
    def get_sindicato(self):
        return self.__sindicato
    
    def get_total_imposto(self):
        return self.__total_imposto
    
    def get_matricula(self):
        return self.__matricula
    
    def get_nome(self):
        return self.__nome
        
    def get_salario_base(self):#Precisa usar ele para evitar o erro
        return self.__salario_base

    @abstractmethod
    def calcular_salario_bruto(self):
        pass

# Herança: Classe Gerente herda de Funcionario
class Gerente(Funcionario):
    def __init__(self, nome, salario_base, bonus):
        super().__init__(nome, salario_base)
        self.__bonus = bonus

    def calcular_salario_bruto(self):
        # Polimorfismo: Implementação específica para Gerente
        return self.get_salario_base() + self.__bonus

# Herança: Classe Desenvolvedor herda de Funcionario
class Desenvolvedor(Funcionario):
    def __init__(self, nome, salario_base, horas_extras):
        super().__init__(nome, salario_base)
        self.__horas_extras = horas_extras
        self.__valor_hora = 50.0
        
    def calcular_salario_bruto(self):
        # Polimorfismo: Implementação específica para Desenvolvedor
        return self.get_salario_base() + (self.__horas_extras * self.__valor_hora)

# Agregação: A Empresa "agrega" vários funcionários
class Empresa:
    def __init__(self, nome):
        self.nome = nome

    def adicionar_funcionario(self, funcionario):
        lista_funcionarios.append(funcionario)
        

    def processar_folha_pagamento(self):
        print(f"Processando folha de pagamento da {self.nome}:")
        for funcionario in lista_funcionarios:
            try:
                # Polimorfismo em ação: cada objeto chama seu próprio método
                salario = funcionario.calcular_salario_bruto()
                salario_liquido = salario - (salario * funcionario.get_total_imposto)
                print(f" {funcionario.get_matricula()}-{funcionario.get_nome()}: R${salario:.2f}")
                print(f"Inss(8%): R${salario*funcionario.get_inss()}")
                print(f"Iposto de renda(11%): R${salario*funcionario.get_imposto_renda()}")
                print(f"Sindicato(5%): R${salario*funcionario.get_sindicato()}")
                print(f"Salário líquido: {salario_liquido:.2f}")
            except Exception as e:
                # Tratamento de Exceções
                print(f"Erro ao processar salário de {funcionario.get_nome()}: {e}")
                    
# Exemplo de uso
empresa = Empresa("Tech Solutions")
gerente = Gerente("Ana", 8000, 2000)
empresa.adicionar_funcionario(gerente)
dev = Desenvolvedor("João", 5000, 10)
empresa.adicionar_funcionario(dev)
dev2 = Desenvolvedor("Pedro", 5000, 10)
empresa.adicionar_funcionario(dev2)
dev3 = Desenvolvedor("Nick", 7000, 6)
empresa.adicionar_funcionario(dev3)

empresa.processar_folha_pagamento()







