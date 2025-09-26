"""
Nesse cenário consideramos que um médico tem apenas uma especialidade e que
esta pode ter um ou mais médicos.
"""

class Especialidade:
    def __init__(self, nome):
        self.nome = nome
        self.medicos = [] # lista de médicos
        
    def __repr__(self):
        return f"{self.nome}"
    
class Medico:
    def __init__(self, nome, crm, especialidade):
        self.nome = nome
        self.crm = crm
        self.especialidade = especialidade
    
    def __str__(self):
        return f"Dr(a): {self.nome} | CRM: {self.crm} | Especialidade: {self.especialidade}"
        
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

# Especialidade
# Criação de especialidades
cardiologista = Especialidade("Cardiologista")
neurologista = Especialidade("Neurologista")
pediatra = Especialidade("Pediatra")
psiquiatra = Especialidade("Psiquiatra")

# Médico
# Criação do médico neurologistao com uma especialidade
dra_sophia = Medico("Sophia Henrick", "12345PE",  neurologista)
# adicionar à lista de medicos 
neurologista.medicos.append(dra_sophia)

print(dra_sophia)