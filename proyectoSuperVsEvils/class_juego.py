import random

class Personaje:
    def __init__(self, nombre, poderes, nivel_poder, vida):
        self.nombre = nombre
        self.poderes = poderes
        self.nivel_poder = nivel_poder
        self.vida = vida

    def __str__(self):
        return f'Nombre: {self.nombre}, Poderes: {self.poderes}, Nivel: {self.nivel_poder}, Vida: {self.vida}'

    def pelea_de_personajes(self, otro_personaje):
        if self.nivel_poder > otro_personaje.nivel_poder:
            ganador = self
            perdedor = otro_personaje
        elif self.nivel_poder < otro_personaje.nivel_poder:
            ganador = otro_personaje
            perdedor = self
        else:
            return "Empate"

        ganador.nivel_poder += 25
        ganador.vida -= ganador.vida * 0.1
        perdedor.vida = 0

        return ganador, perdedor

def adversarios():
    return [
        Personaje("Superman", ["SuperFuerza", "Vuelo", "Visión de calor"], 750, 700),
        Personaje("Batman", ["Artes Marciales", "Inteligencia", "Tecnología avanzada"], 450, 650),
        Personaje("Wonder Woman", ["SuperFuerza", "Vuelo", "Agilidad"], 680, 620),
        Personaje("Joker", ["Inteligencia", "Trucos", "Manipulación"], 450, 600),
        Personaje("Flash", ["Velocidad sobrehumana", "Curación acelerada", "Viaje en el tiempo"], 600, 550),
        Personaje("Aquaman", ["Control del agua", "Fuerza sobrehumana", "Telepatía marina"], 680, 700),
        Personaje("Spider-Man", ["Fuerza mejorada", "Agilidad sobrehumana", "Sentido arácnido"], 700, 750),
        Personaje("Wolverine", ["Regeneración celular", "Garras retráctiles", "Sentidos agudizados"], 640, 900),
        Personaje("Iron Man", ["Genio nivel intelectual", "Armadura Iron Man", "Ingeniería"], 600, 700),
        Personaje("Captain America", ["Fuerza sobrehumana", "Agilidad", "Escudo indestructible"], 720, 650),
        Personaje("Black Widow", ["Maestría en combate", "Espionaje", "Artes marciales"], 550, 600),
        Personaje("Thor", ["SuperFuerza", "Vuelo", "Control del clima"], 800, 800)
    ]

def personajes_seleccionables():
    return [
        Personaje("Superman", ["SuperFuerza", "Vuelo", "Visión de calor"], 750, 700),
        Personaje("Batman", ["Artes Marciales", "Inteligencia", "Tecnología avanzada"], 450, 650),
        Personaje("Wonder Woman", ["SuperFuerza", "Vuelo", "Agilidad"], 680, 620),
        Personaje("Joker", ["Inteligencia", "Trucos", "Manipulación"], 450, 600),
        Personaje("Flash", ["Velocidad sobrehumana", "Curación acelerada", "Viaje en el tiempo"], 600, 550),
        Personaje("Aquaman", ["Control del agua", "Fuerza sobrehumana", "Telepatía marina"], 680, 700),
        Personaje("Spider-Man", ["Fuerza mejorada", "Agilidad sobrehumana", "Sentido arácnido"], 700, 750),
        Personaje("Wolverine", ["Regeneración celular", "Garras retráctiles", "Sentidos agudizados"], 640, 900),
        Personaje("Iron Man", ["Genio nivel intelectual", "Armadura Iron Man", "Ingeniería"], 600, 700),
        Personaje("Captain America", ["Fuerza sobrehumana", "Agilidad", "Escudo indestructible"], 720, 650),
        Personaje("Black Widow", ["Maestría en combate", "Espionaje", "Artes marciales"], 550, 600),
        Personaje("Thor", ["SuperFuerza", "Vuelo", "Control del clima"], 800, 800)
    ]

def torneo_de_peleas(personaje_inicial, lista_adversarios):
    personaje_actual = personaje_inicial
    while lista_adversarios and personaje_actual.vida > 0:
        adversario = random.choice(lista_adversarios)
        resultado = personaje_actual.pelea_de_personajes(adversario)
        if resultado == "Empate":
            print(f"La batalla entre {personaje_actual.nombre} y {adversario.nombre} ha resultado en empate")
        else:
            ganador, perdedor = resultado
            print(f"El ganador es {ganador.nombre} con un nivel de poder de {ganador.nivel_poder} y una vida restante de {ganador.vida}, {perdedor.nombre} ha sido eliminado por {ganador.nombre}")
            if perdedor == personaje_actual:
                print("¡Tu personaje ha sido eliminado! Fin del juego.")
                return
            else:
                lista_adversarios.remove(perdedor)
                personaje_actual = ganador
    print(f"El torneo ha concluido, el ganador es {personaje_actual.nombre}.")

def torneo_uno_vs_uno(personaje_inicial, lista_adversarios, lista_seleccionables):
    personaje_actual = personaje_inicial
    while lista_adversarios and lista_seleccionables and personaje_actual.vida > 0:
        indices_adversarios = list(range(len(lista_adversarios)))

        print("Lista de adversarios disponibles:")
        for i in indices_adversarios:
            adversario = lista_adversarios[i]
            print(f"{i + 1}. {adversario.nombre}")

        while True:
            opcion = input("Seleccione el número del adversario deseado: ")
            try:
                opcion = int(opcion)
                if 1 <= opcion <= len(indices_adversarios):
                    break
                else:
                    print("Por favor, seleccione un número válido.")
            except ValueError:
                print("Por favor, ingrese un número válido.")

        adversario_elegido = lista_adversarios[indices_adversarios[opcion - 1]]
        resultado = personaje_actual.pelea_de_personajes(adversario_elegido)
        if resultado == "Empate":
            print(f"La batalla entre {personaje_actual.nombre} y {adversario_elegido.nombre} ha resultado en empate")
        else:
            ganador, perdedor = resultado
            print(f"El ganador es {ganador.nombre} con un nivel de poder de {ganador.nivel_poder} y una vida restante de {ganador.vida}, {perdedor.nombre} ha sido eliminado por {ganador.nombre}")
            if perdedor == personaje_actual:
                print("¡Tu personaje ha sido eliminado! Fin del juego.")
                return
            else:
                indices_adversarios = [index for index in indices_adversarios if index != indices_adversarios[opcion - 1]]
                personaje_actual = ganador

def elegir_personaje(personajes_disponibles):
    print("Lista de personajes seleccionables:")
    for i, personaje in enumerate(personajes_disponibles, 1):
        print(f"{i}. {personaje.nombre}")
    while True:
        opcion = input("Seleccione el número del personaje deseado: ")
        try:
            opcion = int(opcion)
            if 1 <= opcion <= len(personajes_disponibles):
                return personajes_disponibles[opcion - 1]
            else:
                print("Por favor, seleccione un número válido.")
        except ValueError:
            print("Por favor, ingrese un número válido.")