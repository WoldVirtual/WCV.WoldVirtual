from BK_CPSGR.usuarios   import registrar_usuario, verificar_credenciales, manejar_accion
from BK_CPSGR.recursos   import RecursosUsuario, asignar_recursos_a_usuario, MonitoreoRecursos
from BK_CPSGR.blockchain import Blockchain
from BK_CPSGR.database  import conectar_base_datos
from BK_CPSGR.compresion import comprimir_y_guardar_datos, cargar_y_descomprimir_datos
from BK_CPSGR.servidor   import app, socketio

def main():
    # Inicializar recursos
    recursos_usuario = RecursosUsuario(50, 50)  # Ejemplo de inicialización con 50% de CPU y ancho de banda

    # Conectar a la base de datos
    db = conectar_base_datos()

    # Crear un nuevo usuario
    registrar_usuario("nombre", "contraseña")

    # Ejecutar compresión de datos
    datos_usuario = {"nombre": "nombre", "datos": "datos_ejemplo"}
    comprimir_y_guardar_datos(datos_usuario, "datos_comprimidos.gz")

    # Procesar transacción en la blockchain
    blockchain = Blockchain()
    blockchain.agregar_bloque("transaccion_ejemplo")

    # Iniciar servidor
    socketio.run(app, debug=True)

if __name__ == "main":
    main()
