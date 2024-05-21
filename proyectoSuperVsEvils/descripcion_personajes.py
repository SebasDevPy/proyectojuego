from class_juego import Personaje

class Describir:
    def __init__(self, nombre, poderes):
        self.nombre = nombre
        self.poderes = poderes

    def __str__(self):
        return f"Nombre: {self.nombre}, Poderes: {self.poderes}"

def describir_personaje(personaje):
    print("Descripción del personaje:")
    print(f"Nombre: {personaje.nombre}")
    print(f"Poderes: {', '.join(personaje.poderes)}")