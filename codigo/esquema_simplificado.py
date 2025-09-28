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
        return f"Dr(a):{self.nome}|CRM:{self.crm}|Especialidade:{self.especialidade}"
        
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
        self.status = False        
        
     
    def agendarConsulta(self):
        self.status = True
        consultas.append(self) # add objeto 'consulta' atual à lista consulta
        
        print("Confirmação de agendamento:")
        print(f"Agendamento:{self.idConsulta}|paciente:{self.paciente}|Epecialidade:{self.especialidade}" )
        
    def cancelarConsulta(self, idConsulta):
        for consulta in consultas:
            if consulta.idConsulta == idConsulta:
                consultas.remove(consulta)
        print("Consulta cancelada.")
        self.status = False
        
    def buscarConsulta(self):
        return {
            "idConsulta": self.idConsulta,
            }

    def __str__(self):
        return f"Nº{self.idConsulta}|Paciente:{self.paciente}|Medico:{self.medico}|Data:{self.dataAgendamento}"
# Especialidade
# Criação de especialidades
cardiologista = Especialidade("Cardiologista")
neurologista = Especialidade("Neurologista")
pediatra = Especialidade("Pediatra")
psiquiatra = Especialidade("Psiquiatra")
oncologista = Especialidade("Oncologista")
ortopedista = Especialidade("Ortopedista")
oftamologista = Especialidade("Oftamologista")
# Médico
# Criação do médico neurologistao com uma especialidade
medico1 = Medico("Sophia Henrick", "12345PE",  neurologista)
# adicionar à lista de medicos 
neurologista.medicos.append(medico1)

medico2 = Medico("Renata Lee", "43210PE",  oncologista)
oncologista.medicos.append(medico2)

medico3 = Medico("Julio", "45678PE",  oncologista)
oncologista.medicos.append(medico3)

medico4 = Medico("Romero", "14785PE",  ortopedista)
ortopedista.medicos.append(medico4)

medico5 = Medico("Cesar", "36985PE",  oftamologista)
ortopedista.medicos.append(medico5)
# Paciente
# Criação do paciente
paciente1 = Paciente("123.456.789.1", "Monica Maria")
paciente2 = Paciente("785.569.124.3", "Astrid Leonora")
paciente3 = Paciente("456.159.357.2", "Carlos Fernandes")

# !implementar a função de listar médico!
print(medico1)
print(medico2)
print(medico3)
print(medico4)
print(medico5)

# agendamento
consulta1 = Consulta(medico1, neurologista, paciente2)
consulta1.agendarConsulta()
consulta2 = Consulta(medico4, ortopedista, paciente1)
consulta2.agendarConsulta()
consulta3 = Consulta(medico5, oftamologista, paciente3)
consulta3.agendarConsulta()

# cancelar consulta
consulta1.cancelarConsulta(1)

for c in consultas:
    print(c)
    
print()

for c in consultas:
    print(c)