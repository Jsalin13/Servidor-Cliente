import socket # librería para conexión

# Crear el socket
servidor = socket.socket()

# IP y puerto del servidor
servidor.bind(('127.0.0.1', 12345))
servidor.listen(1)
print("Esperando conexión con el cliente")

# Aceptar conexión
conexion, direccion = servidor.accept()
print(f"Conexión desde {direccion}")

while True:
    # Recibir mensaje del cliente
    mensaje = conexion.recv(1024).decode()
    if mensaje == 'salir':
        print("El cliente finalizó la conexión")
        break
    print(f"El cliente respondió: {mensaje}")

    # Enviar mensaje al cliente
    mensaje_servidor = input("Escriba un mensaje al cliente: ")
    conexion.send(mensaje_servidor.encode())
    if mensaje_servidor == 'salir':
        print("El servidor finalizó la conexión")
        break

# Finalizar conexión
conexion.close()
servidor.close()
print("Conexión finalizada")