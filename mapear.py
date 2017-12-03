import redis
from EDA.Ambulatorio import Ambulatorio
from EDA.Consulta    import Consulta
from EDA.Funcionario import Funcionario
from EDA.Medico      import Medico
from EDA.Paciente    import Paciente
from Scripts.RedisConfig import *

ambulatorios = []
table = open('DataBase/Ambulatorios.txt', 'r')
for line in table.readlines():
    if(line != ''):
        line = line.replace('\n', '').split(',')
        ambulatorios.append(Ambulatorio(line[0], line[1], line[2]))
table.close()

consultas = []
table = open('DataBase/Consultas.txt', 'r')
for line in table.readlines():
    if(line != ''):
        line = line.replace('\n', '').split(',')
        consultas.append(Consulta(line[0], line[1], line[2], line[3]))
table.close()

consultas = []
table = open('DataBase/Consultas.txt', 'r')
for line in table.readlines():
    if(line != ''):
        line = line.replace('\n', '').split(',')
        consultas.append(Consulta(line[0], line[1], line[2], line[3]))
table.close()

funcionarios = []
table = open('DataBase/Funcionarios.txt', 'r')
for line in table.readlines():
    if(line != ''):
        line = line.replace('\n', '').split(',')
        funcionarios.append(Funcionario(line[0], line[1], line[2], line[3], line[4], line[5]))
table.close()

medicos = []
table = open('DataBase/Medicos.txt', 'r')
for line in table.readlines():
    if(line != ''):
        line = line.replace('\n', '').split(',')
        medicos.append(Medico(line[0], line[1], line[2], line[3], line[4], line[5], line[6]))
table.close()

pacientes = []
table = open('DataBase/Pacientes.txt', 'r')
for line in table.readlines():
    if(line != ''):
        line = line.replace('\n', '').split(',')
        pacientes.append(Paciente(line[0], line[1], line[2], line[3], line[4], line[5]))
table.close()

sv = redis.StrictRedis(host="localhost", charset="utf-8", port=6379, db=0, decode_responses=True)
redis.Redis.flushdb(sv)
salvarRedis(sv, ambulatorios, consultas, funcionarios, medicos, pacientes)
print("Banco de dados mapeado para o Servidor Redis!")
