from datetime import datetime

consultas = []
medicos = {}
pacientes = {}
especialidades = {}

class  Especialidade:
    def __init__(self, idEspecialidade, nomeEspecialidade):
        self.idEspecialidade = idEspecialidade
        self.nomeEspecialidade = nomeEspecialidade
        
    def __str__(self):
         return  f"-- {self.nomeEspecialidade}"
    
class Medico:
    def __init__(self, crm, nome, telefone, email):
        self.crm = crm
        self.nome = nome
        self.telefone = telefone
        self.email = email
        
    def __str__(self):
        return  f"Crm: {self.crm} -- {self.nome}"

class Paciente:
    def __init__(self, cpf, nome, telefone, email):
        self.cpf = cpf
        self.nome = nome
        self.telefone = telefone
        self.email = email

class Consulta:
    def __init__(self, medico, paciente, local):
        self.idConsulta = idConsulta
        self.medico = medico
        self.paciente = paciente
        self.dataConsulta = datetime.now()
        self.local = local
        

especialidade1 = Especialidade("1001","Neorologista")
especialidade2 = Especialidade("1002","Dermatologista")
especialidade3 = Especialidade("1003","Cardiologista")
especialidade4 = Especialidade("1004","Nutricionista")
especialidade5 = Especialidade("1005","Psiquiatra")

ramo = [especialidade1, especialidade2, especialidade3, especialidade4, especialidade5]

for esp in ramo:
    especialidades[esp.idEspecialidade] = esp
    print(especialidades[esp.idEspecialidade])

medico1 = Medico("CRM132456","Nicolas Henrick", "(81)9 1234-5678","nicolashenrickalpha@sa")

print(medico1, especialidade1)
#print(especialidade1)
        
        