from dataclasses import dataclass
from typing import List

# Clase Elemento
@dataclass
class Elemento:
    nombre: str

    def __eq__(self, other):
        if isinstance(other, Elemento):
            return self.nombre == other.nombre
        return False

# Clase Conjunto
class Conjunto:
    contador = 0

    def __init__(self, nombre: str):
        self.lista_elementos: List[Elemento] = []
        self.nombre: str = nombre
        self.__id: int = Conjunto.contador
        Conjunto.contador += 1

    @property
    def id(self) -> int:
        return self.__id

    def contiene(self, elemento: Elemento) -> bool:
        return any(e == elemento for e in self.lista_elementos)

    def agregar_elemento(self, elemento: Elemento):
        if not self.contiene(elemento):
            self.lista_elementos.append(elemento)

    def unir(self, otro_conjunto: "Conjunto") -> "Conjunto":
        nuevo_conjunto = Conjunto(f"{self.nombre} UNIDO {otro_conjunto.nombre}")
        for elem in self.lista_elementos:
            nuevo_conjunto.agregar_elemento(elem)
        for elem in otro_conjunto.lista_elementos:
            nuevo_conjunto.agregar_elemento(elem)
        return nuevo_conjunto

    def __add__(self, otro_conjunto: "Conjunto") -> "Conjunto":
        return self.unir(otro_conjunto)

    @classmethod
    def intersectar(cls, conjunto1: "Conjunto", conjunto2: "Conjunto") -> "Conjunto":
        elementos_interseccion = [elem for elem in conjunto1.lista_elementos if conjunto2.contiene(elem)]
        nombre_interseccion = f"{conjunto1.nombre} INTERSECTADO {conjunto2.nombre}"
        nuevo_conjunto = Conjunto(nombre_interseccion)
        for elem in elementos_interseccion:
            nuevo_conjunto.agregar_elemento(elem)
        return nuevo_conjunto

    def __str__(self) -> str:
        elementos = ", ".join([elem.nombre for elem in self.lista_elementos])
        return f"Conjunto {self.nombre}: ({elementos})"


    # Crear objetos Elemento
elemento1 = Elemento("Agua")
elemento2 = Elemento("Fuego")
elemento3 = Elemento("Tierra")

# Crear objetos Conjunto
conjunto1 = Conjunto("Conjunto A")
conjunto2 = Conjunto("Conjunto B")

# Agregar elementos a los conjuntos
conjunto1.agregar_elemento(elemento1)
conjunto1.agregar_elemento(elemento2)
conjunto2.agregar_elemento(elemento2)
conjunto2.agregar_elemento(elemento3)

# Verificar si un conjunto contiene un elemento con el mismo nombre
print("conjunto1 contiene elemento1:", conjunto1.contiene(elemento1))  # True
print("conjunto2 contiene elemento1:", conjunto2.contiene(elemento1))  # False

# Unir dos conjuntos y verificar el resultado
conjunto_unido = conjunto1 + conjunto2
print(conjunto_unido)

# Intersectar dos conjuntos y verificar el resultado
conjunto_interseccion = Conjunto.intersectar(conjunto1, conjunto2)
print(conjunto_interseccion)

    



            
            


        


    
    

        
    
        