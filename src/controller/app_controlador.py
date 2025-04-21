from model.usuario import GestorUsuario
from model.tarea import GestorTarea


class AppControlador:
    """
    Controlador principal que gestiona la lógica de la aplicación.
    """

    def __init__(self):
        self.gestor_usuarios = GestorUsuario()
        self.gestor_tareas = GestorTarea()

    def crear_cuenta(self, datos):
        self.gestor_usuarios.crear_cuenta(datos)

    def iniciar_sesion(self, datos):
        self.gestor_usuarios.iniciar_sesion(datos)

    def crear_tarea(self, datos):
        self.gestor_tareas.crear_tarea(datos, self.gestor_usuarios)

    def obtener_tareas(self, usuario):
        return [
            {
                "txt_tarea": tarea.txt_tarea,
                "categoria": tarea.categoria,
                "estado": tarea.estado
            }
            for tarea in self.gestor_usuarios.usuarios[usuario].tareas
        ]

    def editar_tarea(self, datos):
        self.gestor_tareas.editar_tarea(datos, self.gestor_usuarios)

    def eliminar_tarea(self, datos):
        self.gestor_tareas.eliminar_tarea(datos, self.gestor_usuarios)

    def cambiar_contraseña(self, datos):
        self.gestor_usuarios.cambiar_contraseña(datos)