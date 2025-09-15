from datetime import datetime
from typing import List

class Especialidade:
    def __init__(self, idEspecialidade: int, especialidade: str):
        self.idEspecialidade = idEspecialidade
        self.especialidade = especialidade

    def listarEspecialidade(self) -> List[str]:
        return [self.especialidade]


class Pessoa:
    def __init__(self, idPessoa: int, nome: str, dataNascimento: str, sexo: str, email: str, telefone: str):
        self.idPessoa = idPessoa
        self.nome = nome
        self.dataNascimento = datetime.strptime(dataNascimento, "%Y-%m-%d").date()
        self.sexo = sexo
        self.email = email
        self.telefone = telefone


class Medico(Pessoa):
    def __init__(self, idPessoa: int, nome: str, dataNascimento: str, sexo: str, email: str, telefone: str, crm: str,
                 especialidade: Especialidade):
        super().__init__(idPessoa, nome, dataNascimento, sexo, email, telefone)
        self.crm = crm
        self.especialidade = especialidade

    def listarMedico(self) -> List[str]:
        return [f"Dr(a). {self.nome} - CRM: {self.crm} - Especialidade: {self.especialidade.especialidade}"]


class Paciente(Pessoa):
    def __init__(self, idPessoa: int, nome: str, dataNascimento: str, sexo: str, email: str, telefone: str,
                 numeroCarteira: str):
        super().__init__(idPessoa, nome, dataNascimento, sexo, email, telefone)
        self.numeroCarteira = numeroCarteira

    def listarPaciente(self) -> List[str]:
        return [f"{self.nome} - Carteira: {self.numeroCarteira}"]


class Consulta:
    def __init__(self, idConsulta: int, dataHora: str, local: str, medico: Medico, paciente: Paciente,
                 observacao: str = "", status: str = "Agendada"):
        self.idConsulta = idConsulta
        self.dataHora = datetime.strptime(dataHora, "%Y-%m-%d %H:%M")
        self.local = local
        self.medico = medico
        self.paciente = paciente
        self.observacao = observacao
        self.status = status

    def listarConsulta(self) -> List[str]:
        return [
            f"Consulta {self.idConsulta} - {self.dataHora} - {self.local} - Médico: {self.medico.nome} - Paciente: {self.paciente.nome} - Status: {self.status}"]

    def agendar(self):
        self.status = "Agendada"

    def cancelarConsulta(self):
        self.status = "Cancelada"

# Instanciando Especialidade

cardiologia = Especialidade(idEspecialidade=1, especialidade="Cardiologia")

# Instanciando Medico

medico1 = Medico(
    idPessoa=101,
    nome="João Silva",
    dataNascimento="1980-05-20",
    sexo="Masculino",
    email="joao.silva@hospital.com",
    telefone="(81) 99999-1234",
    crm="CRM12345",
    especialidade=cardiologia
)

# Instanciando Paciente

paciente1 = Paciente(
    idPessoa=202,
    nome="Maria Oliveira",
    dataNascimento="1990-08-15",
    sexo="Feminino",
    email="maria.oliveira@gmail.com",
    telefone="(81) 98888-5678",
    numeroCarteira="PAC98765"
)

# Instanciando Consulta

consulta1 = Consulta(
    idConsulta=301,
    dataHora="2025-09-20 14:30",
    local="Hospital Central - Sala 5",
    medico=medico1,
    paciente=paciente1,
    observacao="Primeira consulta de rotina"
)

print(cardiologia.listarEspecialidade())
print(medico1.listarMedico())
print(paciente1.listarPaciente())
print(consulta1.listarConsulta())



