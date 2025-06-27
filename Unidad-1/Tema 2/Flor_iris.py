from abc import ABC, abstractmethod
import math

# Clase que representa una flor del dataset Iris
# Tiene los atributos: largo y ancho del sépalo, largo y ancho del pétalo, y su tipo (especie)
class Flor:
    def __init__(self, largo_sepalo, ancho_sepalo, largo_petalo, ancho_petalo, tipo):
        # Todos los atributos son privados (con doble guion bajo)
        self.__largo_sepalo = largo_sepalo
        self.__ancho_sepalo = ancho_sepalo
        self.__largo_petalo = largo_petalo
        self.__ancho_petalo = ancho_petalo
        self.__tipo = tipo

    # Métodos getter para obtener cada atributo
    def get_largo_sepalo(self): return self.__largo_sepalo
    def get_ancho_sepalo(self): return self.__ancho_sepalo
    def get_largo_petalo(self): return self.__largo_petalo
    def get_ancho_petalo(self): return self.__ancho_petalo
    def get_tipo(self): return self.__tipo

    # Métodos setter para modificar los atributos de forma controlada
    def set_largo_sepalo(self, valor): self.__largo_sepalo = valor
    def set_ancho_sepalo(self, valor): self.__ancho_sepalo = valor
    def set_largo_petalo(self, valor): self.__largo_petalo = valor
    def set_ancho_petalo(self, valor): self.__ancho_petalo = valor
    def set_tipo(self, valor): self.__tipo = valor

    # Método mágico para mostrar el contenido de la flor de forma legible
    def __str__(self):
        return f"Flor('{self.__tipo}'): sépalo=({self.__largo_sepalo}, {self.__ancho_sepalo}), pétalo=({self.__largo_petalo}, {self.__ancho_petalo})"

    # Calcula la distancia euclidiana entre dos flores
    def distancia_euclidiana(self, otra):
        return math.sqrt(
            (self.__largo_sepalo - otra.get_largo_sepalo())**2 +
            (self.__ancho_sepalo - otra.get_ancho_sepalo())**2 +
            (self.__largo_petalo - otra.get_largo_petalo())**2 +
            (self.__ancho_petalo - otra.get_ancho_petalo())**2
        )

    # Calcula la distancia de Manhattan (suma de diferencias absolutas)
    def distancia_manhattan(self, otra):
        return (
            abs(self.__largo_sepalo - otra.get_largo_sepalo()) +
            abs(self.__ancho_sepalo - otra.get_ancho_sepalo()) +
            abs(self.__largo_petalo - otra.get_largo_petalo()) +
            abs(self.__ancho_petalo - otra.get_ancho_petalo())
        )

    # Calcula la distancia de Minkowski entre dos flores, con parámetro p (por defecto p=3)
    def distancia_minkowski(self, otra, p=3):
        return (
            (abs(self.__largo_sepalo - otra.get_largo_sepalo())**p +
             abs(self.__ancho_sepalo - otra.get_ancho_sepalo())**p +
             abs(self.__largo_petalo - otra.get_largo_petalo())**p +
             abs(self.__ancho_petalo - otra.get_ancho_petalo())**p) ** (1 / p)
        )

    # Método mágico para sumar dos flores y obtener una flor promedio
    def __add__(self, otra):
        return Flor(
            (self.__largo_sepalo + otra.get_largo_sepalo()) / 2,
            (self.__ancho_sepalo + otra.get_ancho_sepalo()) / 2,
            (self.__largo_petalo + otra.get_largo_petalo()) / 2,
            (self.__ancho_petalo + otra.get_ancho_petalo()) / 2,
            "Promedio"
        )

    # Método mágico para multiplicar una flor por un número (escalar)
    def __mul__(self, factor):
        return Flor(
            self.__largo_sepalo * factor,
            self.__ancho_sepalo * factor,
            self.__largo_petalo * factor,
            self.__ancho_petalo * factor,
            self.__tipo
        )

# Clase abstracta que define la estructura de un clasificador
class Clasificador(ABC):
    @abstractmethod
    def clasificar(self, flor):
        pass

# Clase que implementa un clasificador simple basado en el largo del pétalo
class ClasificadorIris(Clasificador):
    def clasificar(self, flor):
        largo_petalo = flor.get_largo_petalo()
        if largo_petalo < 2.5:
            return "setosa"
        elif largo_petalo < 5.0:
            return "versicolor"
        else:
            return "virginica"

# Bloque principal de pruebas
if __name__ == "__main__":
    # Crear tres flores con datos reales
    f1 = Flor(5.1, 3.5, 1.4, 0.2, "setosa")
    f2 = Flor(6.4, 3.2, 4.5, 1.5, "versicolor")
    f3 = Flor(7.1, 3.0, 6.1, 2.3, "virginica")

    print("Flores:")
    print(f1)
    print(f2)
    print(f3)

    # Modificamos el ancho del sépalo de la primera flor
    f1.set_ancho_sepalo(3.9)
    print("\nDespués de modificar el ancho del sépalo de f1:")
    print(f1)

    # Clasificar la tercera flor usando el clasificador
    clasificador = ClasificadorIris()
    resultado = clasificador.clasificar(f3)
    print(f"\nClasificación de f3: {resultado}")

    # Mostrar las distancias entre la primera y segunda flor
    print("\nDistancias entre f1 y f2:")
    print(f"Euclidiana: {f1.distancia_euclidiana(f2):.2f}")
    print(f"Manhattan: {f1.distancia_manhattan(f2):.2f}")
    print(f"Minkowski (p=3): {f1.distancia_minkowski(f2):.2f}")

    # Sumar dos flores y ver la flor promedio
    flor_combinada = f1 + f2
    print("\nFlor combinada (promedio de f1 y f2):")
    print(flor_combinada)

    # Multiplicamos la flor por 1.2 para aumentar su tamaño en 20%
    flor_mas_grande = f1 * 1.2
    print("\nFlor f1 con tamaño aumentado en 20%:")
    print(flor_mas_grande)
