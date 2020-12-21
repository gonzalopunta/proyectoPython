import PlazasAparcamiento
import Parking
import pickle

class Cliente():
    def __init__(self, nombre, apellidos, fechNac, email, matriculaVehiculo):
        self.nombre = nombre
        self.apellido = apellidos
        self.fechNac = fechNac
        self.email = email
        self.matriculaVehiculo = matriculaVehiculo

    def depositarVehiculo(self, matriculaVehiculo, tipoVehiculo):
        print("El numero de plazas para turismos es de " + PlazasAparcamiento.numPlazasTurismo())
        print("El numero de plazas para motocicletas es de " + PlazasAparcamiento.numPlazasTurismo())
        print("El numero de plazas para minusválidos es de " + PlazasAparcamiento.numPlazasMinusvalidos())

        i = 0
        plazas = []
        if PlazasAparcamiento.numPlazas() < PlazasAparcamiento.plazasLibres():
            for i in range(len(plazas)):
                if len(plazas) < PlazasAparcamiento.numPlazas():
                    plazas[i] = matriculaVehiculo, tipoVehiculo
                    vehiculo=open('plazasVehiculos.pckl', 'wb')
                    pickle.dump(plazas, vehiculo)
                    vehiculo.close
                break


        Parking.generarTicket()

    def retirarVehiculo(self):
        pass

    def depositarAbonados(self):
        pass

    def retirarAbonados(self):
        pass

    @property
    def numPlazas(self):
        self._numPlazas

    @numPlazas.setter
    def numPlazas(self, numPlazas):
        self._numPlazas = numPlazas

    @property
    def numPlazas(self):
        self._numPlazas

    @numPlazas.setter
    def numPlazas(self, numPlazas):
        self._numPlazas = numPlazas

    @property
    def numPlazas(self):
        self._numPlazas

    @numPlazas.setter
    def numPlazas(self, numPlazas):
        self._numPlazas = numPlazas

    @property
    def numPlazas(self):
        self._numPlazas

    @numPlazas.setter
    def numPlazas(self, numPlazas):
        self._numPlazas = numPlazas

    @property
    def numPlazas(self):
        self._numPlazas

    @numPlazas.setter
    def numPlazas(self, numPlazas):
        self._numPlazas = numPlazas
