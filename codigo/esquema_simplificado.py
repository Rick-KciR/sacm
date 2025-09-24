consultas = [] # lista para armazenar todas as consultas

class Especialidade:
    def __init__(self, nome):
        self.nome = nome
        self.medico = [] 
    
class Medico:
    def __init__(self, nome, crm):
        self.nome = nome
        self.crm = crm
        
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
        