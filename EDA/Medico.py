class Medico(object):
    def __init__(self, codm, nome, idade, especialidade, cpf, cidade, nroa):
        self.codm = codm
        self.nome = nome
        self.idade = idade
        self.especialidade = especialidade
        self.cpf = cpf
        self.cidade = cidade
        self.nroa = nroa

    def getCodm(self):
        return self.codm

    def getNome(self):
        return self.nome

    def getIdade(self):
        return self.idade

    def getEspecialidade(self):
        return self.especialidade

    def getCpf(self):
        return self.cpf

    def getCidade(self):
        return self.cidade

    def getNroa(self):
        return self.nroa
