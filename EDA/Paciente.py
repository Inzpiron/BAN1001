class Paciente(object):
    def __init__(self, codp, nome, idade, cidade, cpf, doenca):
        self.codp = codp
        self.nome = nome
        self.idade = idade
        self.cidade = cidade
        self.cpf = cpf
        self.doenca = doenca

    def getCodp(self):
        return self.codp

    def getNome(self):
        return self.nome

    def getIdade(self):
        return self.idade

    def getCidade(self):
        return self.cidade

    def getCpf(self):
        return self.cpf

    def getDoenca(self):
        return self.doenca
