from datetime import datetime

class Tarea:
    """Representa una tarea con texto, categoría, estado y fecha de creación."""
    def __init__(self, datos: dict) -> None:
        self.txt_tarea: str = datos["txt_tarea"]
        self.usuario_creador: str = datos["usuario_creador"]
        self.fecha_creacion: datetime = datetime.now()
        self.categoria: str = datos["categoria"]
        self.estado: str = datos["estado"]

    def __repr__(self):
        return f"Tarea('{self.txt_tarea}', '{self.usuario_creador}', '{self.categoria}', '{self.estado}')"

class GestorTarea:
    """Administra las tareas del sistema: crear, editar y eliminar tareas."""
    def __init__(self):
        self.tareas = []

    def crear_tarea(self, datos: dict, gestor_usuarios):
        usuario = datos.get("usuario_creador")
        if usuario not in gestor_usuarios.usuarios:
            raise ValueError("Usuario no encontrado")
        if not datos.get("txt_tarea"):
            raise ValueError("El texto de la tarea no puede estar vacío")
        if not datos.get("categoria"):
            raise ValueError("Debe especificar una categoría")
        tarea = Tarea(datos)
        self.tareas.append(tarea)
        gestor_usuarios.usuarios[usuario].agregar_tarea(tarea)

    def editar_tarea(self, datos: dict, gestor_usuarios):
        usuario = datos.get("usuario")
        tarea_original = datos.get("tarea_original")
        if usuario not in gestor_usuarios.usuarios:
            raise ValueError("Usuario no encontrado")
        usuario_obj = gestor_usuarios.usuarios[usuario]
        tarea_encontrada = next((t for t in usuario_obj.tareas if t.txt_tarea == tarea_original), None)
        if not tarea_encontrada:
            raise ValueError("Tarea no encontrada")
        if not datos.get("nuevo_texto"):
            raise ValueError("El texto de la tarea no puede estar vacío")
        tarea_encontrada.txt_tarea = datos["nuevo_texto"]
        tarea_encontrada.categoria = datos["nueva_categoria"]
        tarea_encontrada.estado = datos["nuevo_estado"]

    def eliminar_tarea(self, datos: dict, gestor_usuarios):
        usuario = datos.get("usuario")
        tarea_nombre = datos.get("tarea_nombre")
        if usuario not in gestor_usuarios.usuarios:
            raise ValueError("Usuario no encontrado")
        tarea_a_eliminar = next((t for t in self.tareas if t.txt_tarea == tarea_nombre), None)
        if not tarea_a_eliminar:
            raise ValueError("Tarea no encontrada")
        if tarea_a_eliminar.usuario_creador != usuario:
            raise ValueError("No puedes eliminar una tarea que no te pertenece")
        usuario_obj = gestor_usuarios.usuarios[usuario]
        usuario_obj.tareas.remove(tarea_a_eliminar)
        self.tareas.remove(tarea_a_eliminar)
