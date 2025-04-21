from model.tarea import Tarea

class Usuario:
    """Representa un usuario con ID, contraseña y lista de tareas propias."""
    def __init__(self, datos: dict) -> None:
        self.id_usuario: str = datos["id_usuario"]
        self.contraseña: str = datos["contraseña"]
        self.tareas: list[Tarea] = []

    def agregar_tarea(self, tarea: Tarea):
        self.tareas.append(tarea)

    def __repr__(self):
        return f"Usuario('{self.id_usuario}')"

class GestorUsuario:
    """Administra a los usuarios: registro, login y cambios de contraseña."""
    def __init__(self) -> None:
        self.usuarios: dict[str, Usuario] = {}

    def crear_cuenta(self, datos: dict):
        id_usuario = datos.get("id_usuario")
        contraseña = datos.get("contraseña")
        if id_usuario in self.usuarios:
            raise ValueError("El usuario ya existe")
        if len(id_usuario) < 3:
            raise ValueError("El nombre de usuario debe tener al menos 3 caracteres")
        if len(contraseña) < 7 or sum(c.isdigit() for c in contraseña) < 2:
            raise ValueError("La contraseña debe tener al menos 7 caracteres y 2 números")
        self.usuarios[id_usuario] = Usuario(datos)

    def iniciar_sesion(self, datos: dict):
        id_usuario = datos.get("id_usuario")
        contraseña = datos.get("contraseña")
        if not id_usuario or not contraseña:
            raise ValueError("Credenciales inválidas")
        if id_usuario not in self.usuarios:
            raise ValueError("Usuario no encontrado")
        if self.usuarios[id_usuario].contraseña != contraseña:
            raise ValueError("Contraseña incorrecta")
        return "Inicio de sesión exitoso"

    def cambiar_contraseña(self, datos: dict):
        id_usuario = datos.get("id_usuario")
        nueva_contraseña = datos.get("nueva_contraseña")
        if id_usuario not in self.usuarios:
            raise ValueError("Usuario no encontrado")
        if not nueva_contraseña or not isinstance(nueva_contraseña, str):
            raise ValueError("La contraseña debe tener al menos 7 caracteres y 2 números")
        if len(nueva_contraseña) < 7 or sum(c.isdigit() for c in nueva_contraseña) < 2:
            raise ValueError("La contraseña debe tener al menos 7 caracteres y 2 números")
        self.usuarios[id_usuario].contraseña = nueva_contraseña
