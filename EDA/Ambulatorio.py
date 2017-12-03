class Ambulatorio(object):
    def __init__(self, nroa, andar, capacidade):
        self.nroa = nroa
        self.capacidade = capacidade
        self.andar = andar

    def getNroa(self):
        return self.nroa

    def getCapacidade(self):
        return self.capacidade

    def getAndar(self):
        return self.andar
