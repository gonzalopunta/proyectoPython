
class PlazasAparcamiento():
    def __init__(self, numPlazas, plazasLibres, fechaYHora):
        self.numPlazas = numPlazas
        self.plazasLibres = plazasLibres
        self.fechaYHora = fechaYHora

    def numPlazasTurismo(self):
        return self.numPlazas * 0.7

    def numPlazasMotocicleta(self):
        return self.numPlazas * 0.15

    def numPlazasMinusvalidos(self):
        return self.numPlazas * 0.15

    @property
    def numPlazas(self):
        self._numPlazas

    @numPlazas.setter
    def numPlazas(self, numPlazas):
        self._numPlazas = numPlazas

    @property
    def plazasLibres(self):
        self._plazasLibres

    @plazasLibres.setter
    def plazasLibres(self, plazasLibres):
        self._plazasLibres = plazasLibres

    @property
    def fechaYHora(self):
        self._fechaYHora

    @fechaYHora.setter
    def fechaYHora(self, fechaYHora):
        self._fechaYHora = fechaYHora
