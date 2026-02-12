import threading
import time
import random

# Lock que representa la plancha (solo uno puede usarla a la vez)
plancha_lock = threading.Lock()

# Lista para guardar pedidos completados
pedidos_completados = []


def preparar_pedido(nombre_pedido):
    """
    Simula la preparación de un pedido en un restaurante.
    Cada pedido se ejecuta en su propio hilo.
    Solo un hilo puede usar la plancha a la vez.
    """
    print(f"{nombre_pedido}: esperando para usar la plancha...")

    # Zona crítica: usar la plancha
    with plancha_lock:
        print(f"{nombre_pedido}: empezando a cocinar en la plancha.")

        tiempo_coccion = random.randint(2, 5)
        time.sleep(tiempo_coccion)

        print(f"{nombre_pedido}: terminado en {tiempo_coccion} segundos.")

    # Guardar pedido completado
    pedidos_completados.append(nombre_pedido)


def main():
    pedidos = [
        "Hamburguesa",
        "Hot Dog",
        "Papas Fritas",
        "Pizza",
        "Sandwich"
    ]

    hilos = []

    # Crear e iniciar un hilo por pedido
    for pedido in pedidos:
        hilo = threading.Thread(target=preparar_pedido, args=(pedido,))
        hilos.append(hilo)
        hilo.start()

    # Esperar a que todos los pedidos terminen
    for hilo in hilos:
        hilo.join()

    # Mostrar pedidos completados
    print("\nTodos los pedidos han sido preparados:")
    for pedido in pedidos_completados:
        print(f"✔ {pedido}")


if __name__ == "__main__":
    main()
