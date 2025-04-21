from model.usuario import GestorUsuario
from model.tarea import GestorTarea

class GestorAplicacion:
    """Coordina la lógica del programa, conectando tareas y usuarios."""
    def __init__(self):
        self.gestor_usuarios = GestorUsuario()
        self.gestor_tareas = GestorTarea()

    def crear_usuario(self, datos):
        self.gestor_usuarios.crear_cuenta(datos)

    def login(self, datos):
        return self.gestor_usuarios.iniciar_sesion(datos)

    def cambiar_contraseña(self, datos):
        self.gestor_usuarios.cambiar_contraseña(datos)

    def crear_tarea(self, datos):
        self.gestor_tareas.crear_tarea(datos, self.gestor_usuarios)

    def editar_tarea(self, datos):
        self.gestor_tareas.editar_tarea(datos, self.gestor_usuarios)

    def eliminar_tarea(self, datos):
        self.gestor_tareas.eliminar_tarea(datos, self.gestor_usuarios)
