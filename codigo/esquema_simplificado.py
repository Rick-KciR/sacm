"""
Nesse cenário consideramos que um médico tem apenas uma especialidade e que
esta pode ter um ou mais médicos.
"""

class Especialidade:
    def __init__(self, nome):
        self.nome = nome
        self.medico = [] # uma lista de médicos
        
    def __str__(self):
        return f"{self.nome}: {self.medico}"
    
class Medico:
    def __init__(self, nome, crm):
        self.nome = nome
        self.crm = crm
    
    def __str__(self):
        return f"Médico(a): {self.nome} | CRM: {self.crm}"
        
class Paciente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        
class Consulta:
    def __init__(self, medico, especialidade, paciente):
        self.idConsulta = len(consultas) + 1
        self.medico = medico
        self.especialidade = especialidade
        self.paciente = paciente
        self.dataInscricao = datetime.now()
        self.status = False        
        
     
    def agendarConsulta():
        consultas.append(self) # add objeto 'consulta' atual à lista consulta
        
    def cancelarConsulta(self):
        self.status = False
        
    def resumirConsulta(self):
        return {
            "idConsulta": self.idConsulta,
            }

# 1º instacia teste da classe Medico
medica = Medico("Sophia","13245PE")

# 1º instacia teste da classe Especialidade
neurologia = Especialidade("Neurologista")

neurologia.medico.append(medica)

print(neurologia)