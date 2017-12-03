import redis
from EDA.Ambulatorio import Ambulatorio
from EDA.Consulta    import Consulta
from EDA.Funcionario import Funcionario
from EDA.Medico      import Medico
from EDA.Paciente    import Paciente
from Scripts.RedisConfig import *

sv = redis.StrictRedis(host="localhost", charset="utf-8", port=6379, db=0, decode_responses=True)
ambulatorios = getAmbulatoriosFromRedis(sv)
consultas    = getConsultasFromRedis(sv)
Funcionarios = getFuncionariosFromRedis(sv)
medicos      = getMedicosFromRedis(sv)
pacientes    = getPacientesFromRedis(sv)

print('SELECT *  FROM Ambulatórios WHERE nroa=2;')
print('nroa', 'andar', 'capacidade')
for amb in ambulatorios:
    line = '{:>4} {:>5} {:>10}'.format(amb.getNroa(), amb.getCapacidade(), amb.getAndar())
    if(amb.getNroa() == '2'):
        print(line)

print('\n')

print('SELECT p.nome, m.nome, c.data FROM Pacientes p, Medicos m, Consultas c WHERE p.codp=c.codp AND m.codm=c.codm AND p.cidade="Joinville";')
print('p.nome', 'm.nome', 'c.data')
for con in consultas:
    codp = con.getCodp()
    codm = con.getCodm()
    pnome = ''
    mnome = ''
    cdata = con.getData()
    for pac in pacientes:
        if(pac.getCodp() == codp and pac.getCidade() == 'Joinville'):
            pnome = pac.getNome()
            break

    for med in medicos:
        if(med.getCodm() == codm):
            mnome = med.getNome()
            break

    if(pnome != '' and mnome != ''):
        line = '{:>6} {:>6} {:<6}'.format(pnome, mnome, cdata)
        print(line)
