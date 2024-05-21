from class_juego import personajes_seleccionables, torneo_de_peleas, adversarios, torneo_uno_vs_uno, elegir_personaje
from descripcion_personajes import describir_personaje

def mostrar_menu():
    print("Bienvenido al juego SuperVsEvils")
    print("1. Ver lista de personajes seleccionables")
    print("2. Elegir personaje y comenzar el torneo")
    print("3. Pelea 1vs1")
    print("4. Salir")

def main():
    personajes_disponibles = personajes_seleccionables()
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            while True:
                print("Lista de personajes seleccionables:")
                for i, personaje in enumerate(personajes_disponibles, 1):
                    print(f"{i}. {personaje.nombre}")
                print("0. Regresar al menú principal")
                seleccion = input("Seleccione el número del personaje para ver la descripción o 0 para regresar: ")
                try:
                    seleccion = int(seleccion)
                    if seleccion == 0:
                        break
                    elif 1 <= seleccion <= len(personajes_disponibles):
                        describir_personaje(personajes_disponibles[seleccion - 1])
                    else:
                        print("Por favor, seleccione un número válido.")
                except ValueError:
                    print("Por favor, ingrese un número válido.")
        elif opcion == "2":
            personaje_elegido = elegir_personaje(personajes_disponibles)
            print(f"¡Has elegido a {personaje_elegido.nombre}!")
            personajes_disponibles.remove(personaje_elegido)
            torneo_de_peleas(personaje_elegido, adversarios())
        elif opcion == "3":
            personaje_elegido = elegir_personaje(personajes_disponibles + adversarios())
            print(f"¡Has elegido a {personaje_elegido.nombre}!")
            torneo_uno_vs_uno(personaje_elegido, adversarios(), personajes_disponibles)
        elif opcion == "4":
            print("¡Gracias por jugar!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()