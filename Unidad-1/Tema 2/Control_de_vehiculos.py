from abc import ABC, abstractmethod

# Clase abstracta (Abstracción)
class Vehiculo(ABC):
    def __init__(self, identificador, modelo, velocidad_maxima, capacidad_carga):
        self._id = identificador
        self._modelo = modelo
        self._velocidad_maxima = velocidad_maxima
        self._capacidad_carga = capacidad_carga

    @abstractmethod
    def acelerar(self):
        pass

    @abstractmethod
    def frenar(self):
        pass

    def informar_estado(self):
        return f"{self._modelo} (ID: {self._id}) - Velocidad máxima: {self._velocidad_maxima} km/h"

# Subclase Automóvil
class Automovil(Vehiculo):
    def acelerar(self):
        return f"{self._modelo} acelera suavemente."

    def frenar(self):
        return f"{self._modelo} frena con ABS."

# Subclase Camión
class Camion(Vehiculo):
    def acelerar(self):
        return f"{self._modelo} acelera lentamente con carga pesada."

    def frenar(self):
        return f"{self._modelo} frena con frenos neumáticos."

    def engranar_remolque(self):
        return f"{self._modelo} ha enganchado un remolque."

# Subclase Motocicleta
class Motocicleta(Vehiculo):
    def acelerar(self):
        return f"{self._modelo} acelera rápidamente."

    def frenar(self):
        return f"{self._modelo} frena con freno de disco."

    def maniobra_evasiva(self):
        return f"{self._modelo} realizó una maniobra evasiva."

if __name__ == "__main__":
    auto = Automovil("A001", "Toyota Corolla", 180, 500)
    camion = Camion("C001", "Volvo FH", 120, 10000)
    moto = Motocicleta("M001", "Yamaha R3", 200, 150)

    print(auto.informar_estado())
    print(auto.acelerar())
    print(auto.frenar())
    print()

    print(camion.informar_estado())
    print(camion.acelerar())
    print(camion.frenar())
    print(camion.engranar_remolque())
    print()

    print(moto.informar_estado())
    print(moto.acelerar())
    print(moto.frenar())
    print(moto.maniobra_evasiva())
