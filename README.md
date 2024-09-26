La arquitectura Cliente – Servidor que se tiene en el ejercicio práctico anterior, se usa para facilitar la interacción entre dos programas independientes que se comunican a través de una red, aun cuando se encuentren instalados en la misma maquina física. Algunas de las ventajas y uso de esta arquitectura son:

1.	Separación de responsabilidades: El servidor se encarga de las solicitudes y el cliente de enviarlas, esto facilitando la implementación y mantenimiento ya que se pueden hacer de manera independiente
2.	Escalabilidad: Un servidor puede atender varios clientes, por lo que el sistema será escalable.
 
3.	Reutilización de servicios: Un servidor presta servicio a varios cliente, por lo que se puede reutilizar el mismo código
4.	Facilidad de mantenimiento: Al realizarse un cambio en el cliente o en el servidor, puede hacerse de manera individual sin influir al otro.
Funcionalidad

1.	El servidor comienza esperando una conexión (127.0.0.1) y puerto (12345).

2.	El cliente se conecta a esa dirección y puerto.
3.	El cliente envía un mensaje al servidor.
4.	El servidor recibe el mensaje y puede enviar otro de vuelta.
5.	El cliente recibe el mensaje del servidor.
6.	El proceso continúa hasta que uno de los 2 envía la palabra “Salir”, lo que provoca que se finalice la conexión.
Montaje

Este ejercicio se realizó usando el aplicativo Visual Studio Code, integrando la extensión del lenguaje Python con el cual se usó la librería Socket para lograr crear las conexiones TCP para la comunicación y el intercambio de información entre Servidor y Cliente.
