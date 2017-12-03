class Consulta(object):
    def __init__(self, codm, codp, data, hora):
        self.codm = codm
        self.codp = codp
        self.data = data
        self.hora = hora

    def getCodm(self):
        return self.codm

    def getCodp(self):
        return self.codp

    def getData(self):
        return self.data

    def getHora(self):
        return self.hora
