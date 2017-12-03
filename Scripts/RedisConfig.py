import redis
from EDA.Ambulatorio import Ambulatorio
from EDA.Consulta    import Consulta
from EDA.Funcionario import Funcionario
from EDA.Medico      import Medico
from EDA.Paciente    import Paciente

def getAmbulatoriosFromRedis(sv):
    ambulatorios = []
    table = sv.lrange('Ambulatorios', 0, sv.llen('Ambulatorios'))
    for item in table:
        item = item.split(':')
        ambulatorios.append(Ambulatorio(item[0], item[1], item[2]))

    return ambulatorios

def getPacientesFromRedis(sv):
    pacientes = []
    table = sv.lrange('Pacientes', 0, sv.llen('Pacientes'))
    for item in table:
        item = item.split(':')
        pacientes.append(Paciente(item[0], item[1], item[2], item[3], item[4], item[5]))

    return pacientes

def getMedicosFromRedis(sv):
    medicos = []
    table = sv.lrange('Medicos', 0, sv.llen('Medicos'))
    for item in table:
        item = item.split(':')
        medicos.append(Medico(item[0], item[1], item[2], item[3], item[4], item[5], item[6]))

    return medicos

def getConsultasFromRedis(sv):
    consultas = []
    table = sv.lrange('Consultas', 0, sv.llen('Consultas'))
    for item in table:
        item = item.split(':')
        consultas.append(Consulta(item[0], item[1], item[2], item[3]))

    return consultas

def getFuncionariosFromRedis(sv):
    funcionarios = []
    table = sv.lrange('Funcionarios', 0, sv.llen('Funcionarios'))
    for item in table:
        item = item.split(':')
        funcionarios.append(Funcionario(item[0], item[1], item[2], item[3], item[4], item[5]))

    return funcionarios

def salvarRedis(sv, Ambulatorios, Consultas, Funcionarios, Medicos, Pacientes):
    for amb in Ambulatorios:
        strAux  = ''
        strAux += amb.nroa + ':'
        strAux += amb.capacidade + ':'
        strAux += amb.andar
        sv.rpush('Ambulatorios', strAux)

    for con in Consultas:
        strAux  = ''
        strAux += con.codm + ':'
        strAux += con.codp + ':'
        strAux += con.data + ':'
        strAux += con.hora
        sv.rpush('Consultas', strAux)

    for fun in Funcionarios:
        strAux  = ''
        strAux += fun.codf + ':'
        strAux += fun.nome + ':'
        strAux += fun.idade + ':'
        strAux += fun.cpf + ':'
        strAux += fun.cidade + ':'
        strAux += fun.salario
        sv.rpush('Funcionarios', strAux)

    for med in Medicos:
        strAux = ''
        strAux += med.codm + ':'
        strAux += med.nome + ':'
        strAux += med.idade + ':'
        strAux += med.especialidade + ':'
        strAux += med.cidade + ':'
        strAux += med.cpf + ':'
        strAux += med.nroa + ':'
        sv.rpush('Medicos', strAux)

    for pac in Pacientes:
        strAux = ''
        strAux += pac.codp + ':'
        strAux += pac.nome + ':'
        strAux += pac.idade + ':'
        strAux += pac.cidade + ':'
        strAux += pac.cpf + ':'
        strAux += pac.doenca
        sv.rpush('Pacientes', strAux)
