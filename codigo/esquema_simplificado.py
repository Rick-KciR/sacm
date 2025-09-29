from datetime import datetime
"""
Nesse cenário consideramos que um médico tem apenas uma especialidade e que
esta pode ter um ou mais médicos.
"""
consultas = []

class Especialidade:
    def __init__(self, nome):
        self.nome = nome
        self.medicos = [] # lista de médicos
        
    def __str__(self):
        return f"{self.nome}"
    
class Medico:
    def __init__(self, nome, crm, especialidade):
        self.nome = nome
        self.crm = crm
        self.especialidade = especialidade
    
    def __str__(self):
        return f"Dr(a):{self.nome}| CRM:{self.crm}| Especialidade:{self.especialidade}"
        
class Paciente:
    def __init__(self, cpf, nome):
        self.cpf = cpf
        self.nome = nome
        
    def __str__(self):
        return f"{self.nome}"
    
class Consulta:
    def __init__(self, medico, especialidade, paciente):
        self.idConsulta = len(consultas) + 1
        self.medico = medico
        self.especialidade = especialidade
        self.paciente = paciente
        self.dataAgendamento = datetime.now()
        self.status = "Pendente"        
        
        
    def agendarConsulta(self):
        consultas.append(self) # add objeto 'consulta' atual à lista consulta
        self.status = "Agendada"
        print(self)
        
    def cancelarConsulta(self, idConsulta):
        consulta = self.buscarConsulta(idConsulta)
        consulta.status = "Cancelada"
        print(self)
        
    def buscarConsulta(self, idConsulta):
        for consulta in consultas:
            if consulta.idConsulta == idConsulta:         
                return consulta

    def listarCancelada(self):
        for consulta in consultas:
            if consulta.status == "Cancelada":
                return consulta
        
    def __str__(self):
        return f"Nº{self.idConsulta}| Paciente:{self.paciente}| Medico:{self.medico}| Data:{self.dataAgendamento}| Situação: {self.status}"

# Especialidade
# Instâncias de Especialidade
cardiologista = Especialidade("Cardiologista")
neurologista = Especialidade("Neurologista")
pediatra = Especialidade("Pediatra")
psiquiatra = Especialidade("Psiquiatra")
oncologista = Especialidade("Oncologista")
ortopedista = Especialidade("Ortopedista")
oftamologista = Especialidade("Oftamologista")

# Médico
# Instâncias de Medico com atribuição de especialidade
medico1 = Medico("Sophia Henrick", "12345PE",  neurologista)
neurologista.medicos.append(medico1)# adiciona o médico à lista medicos em Especialidade
medico2 = Medico("Renata Lee", "43210PE",  oncologista)
oncologista.medicos.append(medico2)
medico3 = Medico("Julio", "45678PE",  oncologista)
oncologista.medicos.append(medico3)
medico4 = Medico("Romero", "14785PE",  ortopedista)
ortopedista.medicos.append(medico4)
medico5 = Medico("Cesar", "36985PE",  oftamologista)
ortopedista.medicos.append(medico5)

# Paciente
## Instancias de Paciente
paciente1 = Paciente("123.456.789.1", "Monica Maria")
paciente2 = Paciente("785.569.124.3", "Astrid Leonora")
paciente3 = Paciente("456.159.357.2", "Carlos Fernandes")


# Agendar consulta
## Instancias de Consulta e agendamento de consultas
print("Consultas agendadas")
print("-" * 25)

consulta1 = Consulta(medico1, neurologista, paciente2)
consulta1.agendarConsulta()
print("-" * 135)
consulta2 = Consulta(medico4, ortopedista, paciente1)
consulta2.agendarConsulta()
print("-" * 135)
consulta3 = Consulta(medico5, oftamologista, paciente3)
consulta3.agendarConsulta()
print("-" * 135)

# Cancelar Consulta
consulta1.cancelarConsulta(1)
print("-" * 135)

print("\nConsultas canceladas")
print("-" * 35)
cancelada = consulta2.listarCancelada()
print(cancelada)

print("\nBuscando uma consulta")
print("-" * 35)
busca2 = consulta2.buscarConsulta(2)
print(busca2)
print("-" * 135)

"""
for c in consultas:
    print(c)
    
print()

for c in consultas:
    print(c)
"""