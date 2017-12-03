class Funcionario(object):
    def __init__(self, codf, nome, idade, cpf, cidade, salario):
        self.codf = codf
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.cidade = cidade
        self.salario = salario

    def getCodf(self):
        return self.codf

    def getNome(self):
        return self.nome

    def getIdade(self):
        return self.idade

    def getCpf(self):
        return self.cpf

    def getCidade(self):
        return self.cidade

    def getSalario(self):
        return self.salario
