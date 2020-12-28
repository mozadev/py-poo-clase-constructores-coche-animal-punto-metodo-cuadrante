class Coche():

    ruedas=4

    def desplazamiento(self):
        print("El coche se esta desplazando sobre 4 ruedas")

class Moto():

    ruedas=2

    def desplazamiento(self):
        print("La moto se esta desplazando sobre 2 ruedas")

miVehiculo=Coche()

print("Mi coche tiene ", miVehiculo.ruedas, " ruedas")

miVehiculo.desplazamiento()

print("---------------Segundo objeto---------------")

miVehiculo2=Moto()

print("Mi moto tiene ", miVehiculo2.ruedas, " ruedas")

miVehiculo2.desplazamiento()


___________________________________________________________

class Coche():

    ruedas=4

    def desplazamiento(self):
        print("El coche se esta desplazando sobre", self.ruedas, "ruedas")
class Moto():

    ruedas=2

    def desplazamiento(self):
        print("La moto se esta desplazando sobre 2 ruedas")
miVehiculo=Coche()
miVehiculo.ruedas=3

print("Mi coche tiene ", miVehiculo.ruedas, " ruedas")
miVehiculo.desplazamiento()

print("---------------Segundo objeto---------------")

miVehiculo2=Moto()
print("Mi moto tiene ", miVehiculo2.ruedas, " ruedas")

miVehiculo2.desplazamiento()


___________________________________________________________
METODO CONSTRUCTOR
___________________________________________________________
___________________________________________________________

class Cachorro():
    def __init__(self, color, raza):
        self.color = color
        self.raza = raza
perrito = Cachorro("Marrón claro", "Golden retriever")
print("Este es un cachorro de la raza {} y es de color {}".format(perrito.raza, perrito.color))

___________________________________________________________

class Cachorro():
    def __init__(self, color, raza, tamaño, nombre):
        self.color = color
        self.raza = raza
        self.tamaño = tamaño
        self.nombre = nombre
perrito = Cachorro("Marrón claro", "pequinez", "pequeño", "Mel")
print("Este es un cachorro de la raza {}, es de color {}, de tamaño {} y su nombre es {}" .format(perrito.raza, perrito.color, perrito.tamaño, perrito.nombre))


__________________________________________________

class Cachorro():
    def __init__(self, color, raza, tamaño, nombre):
        self.color = color
        self.raza = raza
        self.tamaño = tamaño
        self.nombre = nombre
perrito = Cachorro("Marrón claro", "pequinez", "pequeño", "Mel")
pollito = Cachorro("amarillo", "sanfernando", "pequeño", "pio")
print("Este es un cachorro de la raza {}, es de color {}, de tamaño {} y su nombre es {}" .format(perrito.raza, perrito.color, perrito.tamaño, perrito.nombre))
print("El pollito es de color", pollito.color)
print("El pollito es de raza", pollito.raza)
print("El pollito es de tamaño", pollito.tamaño)
print("El pollito es de nombre", pollito.nombre)

__________________________________________________________


import math

class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    def cuadrante(self):
        if self.x > 0 and self.y > 0:
            print("{} pertenece al primer cuadrante".format(self))
        elif self.x < 0 and self.y > 0:
            print("{} pertenece al segundo cuadrante".format(self))
        elif self.x < 0 and self.y < 0:
            print("{} pertenece al tercer cuadrante".format(self))
        elif self.x > 0 and self.y < 0:
            print("{} pertenece al cuarto cuadrante".format(self))
        elif self.x != 0 and self.y == 0:
            print("{} se sitúa sobre el eje X".format(self))
        elif self.x == 0 and self.y != 0:
            print("{} se sitúa sobre el eje Y".format(self))
        else:
            print("{} se encuentra sobre el origen".format(self))

    def vector(self, p):
        print("El vector entre {} y {} es ({}, {})".format(
            self, p, p.x - self.x, p.y - self.y) )

    def distancia(self, p):
        d = math.sqrt( (p.x - self.x)**2 + (p.y - self.y)**2 )
        print("La distancia entre los puntos {} y {} es {}".format(
            self, p, d))


class Rectangulo:

    def __init__(self, pInicial=Punto(), pFinal=Punto()):
        self.pInicial = pInicial
        self.pFinal = pFinal

        # Hago los cálculos, pero no llamo los atributos igual 
        # que los métodos porque sino podríamos sobreescribirlos
        self.vBase = abs(self.pFinal.x - self.pInicial.x)
        self.vAltura = abs(self.pFinal.y - self.pInicial.y)
        self.vArea = self.vBase * self.vAltura

    def base(self):
        print("La base del rectángulo es {}".format( self.vBase ) )

    def altura(self):
        print("La altura del rectángulo es {}".format( self.vAltura ) )

    def area(self):
        print("El área del rectángulo es {}".format( self.vArea ) )


A = Punto(2,3)
B = Punto(5,5)
C = Punto(-3, -1)
D = Punto(0,0)

A.cuadrante()
C.cuadrante()
D.cuadrante()

A.vector(B)
B.vector(A)

A.distancia(B)
B.distancia(A)

A.distancia(D)
B.distancia(D)
C.distancia(D)

R = Rectangulo(A, B)
R.base()
R.altura()
R.area()

___________________________________________________________

import math

class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    def cuadrante(self):
        if self.x > 0 and self.y > 0:
            print("{} pertenece al primer cuadrante".format(self))
        elif self.x < 0 and self.y > 0:
            print("{} pertenece al segundo cuadrante".format(self))
        elif self.x < 0 and self.y < 0:
            print("{} pertenece al tercer cuadrante".format(self))
        elif self.x > 0 and self.y < 0:
            print("{} pertenece al cuarto cuadrante".format(self))
        elif self.x != 0 and self.y == 0:
            print("{} se sitúa sobre el eje X".format(self))
        elif self.x == 0 and self.y != 0:
            print("{} se sitúa sobre el eje Y".format(self))
        else:
            print("{} se encuentra sobre el origen".format(self))

    def vector(self, p):
        print("El vector entre {} y {} es ({}, {})".format(
            self, p, p.x - self.x, p.y - self.y) )
 

A = Punto(2,3)
B = Punto(5,5)
C = Punto(-3, -1)
D = Punto(0,0)

A.cuadrante()
C.cuadrante()
D.cuadrante()

A.vector(B)
B.vector(A)

___________________________________________________________

import math

class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    def cuadrante(self):
        if self.x > 0 and self.y > 0:
            print("{} pertenece al primer cuadrante".format(self))
        elif self.x < 0 and self.y > 0:
            print("{} pertenece al segundo cuadrante".format(self))
        elif self.x < 0 and self.y < 0:
            print("{} pertenece al tercer cuadrante".format(self))
        elif self.x > 0 and self.y < 0:
            print("{} pertenece al cuarto cuadrante".format(self))
        elif self.x != 0 and self.y == 0:
            print("{} se sitúa sobre el eje X".format(self))
        elif self.x == 0 and self.y != 0:
            print("{} se sitúa sobre el eje Y".format(self))
        else:
            print("{} se encuentra sobre el origen".format(self))

    def vector(self, p):
        print("El vector entre {} y {} es ({}, {})".format(
            self, p, p.x - self.x, p.y - self.y) )
 
A = Punto(2,3)
B = Punto(5,5)
C = Punto(-3, -1)
D = Punto(0,0)
E = Punto(4, -6)

A.cuadrante()
C.cuadrante()
D.cuadrante()
E.cuadrante ()

A.vector(B)
B.vector(A)

___________________________________________________________



https://unipython.com/programacion-orientada-objetos-python/

https://byte-mind.net/curso-python-poo/



