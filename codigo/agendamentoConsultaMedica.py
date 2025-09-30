from datetime import datetime

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
    def __init__(self, medico, especialidade, paciente, local):
        self.idConsulta = len(consultas) + 1
        self.medico = medico
        self.especialidade = especialidade
        self.paciente = paciente
        self.local = local
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
                if consulta.status == "Agendada":
                    return consulta
                else:
                   print(f"A consulta de Nº {idConsulta} já está cancelada.") 
            
    def __str__(self):
        return f"Nº{self.idConsulta}| Paciente:{self.paciente}| Medico:{self.medico}| Data:{self.dataAgendamento}| Local:{self.local}| Situação: {self.status}"

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
paciente4 = Paciente("369.456.741.8", "Jonathan Davis")
paciente5 = Paciente("159.357.789.6", "Guaraci Oliveira")

# Agendar consulta
## Instancias de Consulta e agendamento de consultas
print("\n",50*" ","** Consultas agendadas **\n")
consulta1 = Consulta(medico1, neurologista, paciente2, "Hospital Esperança")
consulta1.agendarConsulta()
print("-" * 135)
consulta2 = Consulta(medico4, ortopedista, paciente1, "Hospital São Marcos")
consulta2.agendarConsulta()
print("-" * 135)
consulta3 = Consulta(medico5, oftamologista, paciente3, "Hospital Geral de Areias")
consulta3.agendarConsulta()
print("-" * 135)
consulta4 = Consulta(medico5, oftamologista, paciente4, "Real Hospital Português")
consulta4.agendarConsulta()
print("-" * 135)
consulta5 = Consulta(medico5, oftamologista, paciente5, "Hospital Agamenon Magalhães")
consulta5.agendarConsulta()
print("-" * 135)

# Cancelar Consulta
print("\n",50*" ","** Consultas canceladas **\n")
consulta1.cancelarConsulta(1)
print("-" * 135)
consulta3.cancelarConsulta(3)
print("-" * 135)

print("\n",50*" ","** Lista de consulta atualizada após cancelamento **\n")
for c in consultas:
    if c.status == "Agendada":
        print(c)
        print("-" * 135)

print("\n",50*" ","** Buscando uma consulta já cancelada **\n")
busca1 = consulta1.buscarConsulta(1)
print(busca1)
print("-" * 135)
busca3 = consulta3.buscarConsulta(3)
print(busca3)
print("-" * 135)


print("\n",50*" ","** Buscando uma consulta **\n")
busca2 = consulta2.buscarConsulta(2)
print(busca2)
print("-" * 135)