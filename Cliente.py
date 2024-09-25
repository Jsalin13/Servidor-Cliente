import socket # librería para conexión

# Conectar al servidor
cliente = socket.socket()
cliente.connect(('127.0.0.1', 12345))

while True:
    # Enviar mensaje al servidor
    mensaje = input("Escriba un mensaje al servidor: ")
    cliente.send(mensaje.encode())
    if mensaje == 'salir':
        print("finalizando conexión con el servidor")
        break

    # Recibir mensaje del servidor
    mensaje_servidor = cliente.recv(1024).decode()
    print(f"El servidor respondió: {mensaje_servidor}")
    if mensaje_servidor == 'salir':
        print("El servidor finalizó la conexión")
        break

# Finalizar conexión
cliente.close()
print("Conexión finalizada")