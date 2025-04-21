from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput

class MainScreen(Screen):
    def __init__(self, controlador, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.controlador = controlador  # Guardar la referencia al controlador
        self.usuario_autenticado = None  # Variable para almacenar el usuario autenticado

        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        layout.add_widget(Label(text='Bienvenido a la pantalla principal', font_size=24))

        btn_crear_tarea = Button(text='Crear Tarea')
        btn_crear_tarea.bind(on_press=self.crear_tarea)
        layout.add_widget(btn_crear_tarea)

        btn_ver_tareas = Button(text='Ver Tareas')
        btn_ver_tareas.bind(on_press=self.ver_tareas)
        layout.add_widget(btn_ver_tareas)

        btn_editar_tarea = Button(text='Editar Tarea')
        btn_editar_tarea.bind(on_press=self.editar_tarea)
        layout.add_widget(btn_editar_tarea)

        btn_eliminar_tarea = Button(text='Eliminar Tarea')
        btn_eliminar_tarea.bind(on_press=self.eliminar_tarea)
        layout.add_widget(btn_eliminar_tarea)

        btn_cambiar_contrasena = Button(text='Cambiar Contraseña')
        btn_cambiar_contrasena.bind(on_press=self.cambiar_contrasena)
        layout.add_widget(btn_cambiar_contrasena)

        btn_logout = Button(text='Cerrar Sesión')
        btn_logout.bind(on_press=self.cerrar_sesion)
        layout.add_widget(btn_logout)

        self.add_widget(layout)

    def crear_tarea(self, instance):
        """
        Lógica para crear una tarea.
        """
        popup_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        txt_tarea = TextInput(hint_text='Descripción de la tarea')
        categoria = TextInput(hint_text='Categoría')
        estado = TextInput(hint_text='Estado (Por hacer, En progreso, Completada)')
        popup_layout.add_widget(txt_tarea)
        popup_layout.add_widget(categoria)
        popup_layout.add_widget(estado)

        btn_crear = Button(text='Crear')
        btn_crear.bind(on_press=lambda x: self._crear_tarea(txt_tarea.text, categoria.text, estado.text))
        popup_layout.add_widget(btn_crear)

        popup = Popup(title='Crear Tarea', content=popup_layout, size_hint=(0.8, 0.6))
        popup.open()

    def _crear_tarea(self, txt_tarea, categoria, estado):
        """
        Método auxiliar para crear una tarea.
        """
        try:
            self.controlador.crear_tarea({
                "usuario_creador": self.usuario_autenticado,  # Usar el usuario autenticado
                "txt_tarea": txt_tarea,
                "categoria": categoria,
                "estado": estado
            })
            self.mostrar_popup("Éxito", "Tarea creada con éxito!")
        except ValueError as e:
            self.mostrar_popup("Error", str(e))

    def ver_tareas(self, instance):
        """
        Lógica para ver las tareas del usuario.
        """
        try:
            tareas = self.controlador.obtener_tareas(self.usuario_autenticado)  # Usar el usuario autenticado
            if not tareas:
                self.mostrar_popup("Tareas", "No tienes tareas registradas.")
            else:
                contenido = "\n".join([f"{i+1}. {t['txt_tarea']} - {t['categoria']} ({t['estado']})" for i, t in enumerate(tareas)])
                self.mostrar_popup("Tus Tareas", contenido)
        except KeyError:
            self.mostrar_popup("Error", "Usuario no encontrado.")

    def editar_tarea(self, instance):
        """
        Lógica para editar una tarea.
        """
        popup_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        tarea_original = TextInput(hint_text='Nombre de la tarea a editar')
        nuevo_texto = TextInput(hint_text='Nuevo texto')
        nueva_categoria = TextInput(hint_text='Nueva categoría')
        nuevo_estado = TextInput(hint_text='Nuevo estado')
        popup_layout.add_widget(tarea_original)
        popup_layout.add_widget(nuevo_texto)
        popup_layout.add_widget(nueva_categoria)
        popup_layout.add_widget(nuevo_estado)

        btn_editar = Button(text='Editar')
        btn_editar.bind(on_press=lambda x: self._editar_tarea(tarea_original.text, nuevo_texto.text, nueva_categoria.text, nuevo_estado.text))
        popup_layout.add_widget(btn_editar)

        popup = Popup(title='Editar Tarea', content=popup_layout, size_hint=(0.8, 0.8))
        popup.open()

    def _editar_tarea(self, tarea_original, nuevo_texto, nueva_categoria, nuevo_estado):
        """
        Método auxiliar para editar una tarea.
        """
        try:
            self.controlador.editar_tarea({
                "usuario": self.usuario_autenticado,  # Usar el usuario autenticado
                "tarea_original": tarea_original,
                "nuevo_texto": nuevo_texto,
                "nueva_categoria": nueva_categoria,
                "nuevo_estado": nuevo_estado
            })
            self.mostrar_popup("Éxito", "Tarea editada con éxito!")
        except ValueError as e:
            self.mostrar_popup("Error", str(e))

    def eliminar_tarea(self, instance):
        """
        Lógica para eliminar una tarea.
        """
        popup_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        tarea_nombre = TextInput(hint_text='Nombre de la tarea a eliminar')
        popup_layout.add_widget(tarea_nombre)

        btn_eliminar = Button(text='Eliminar')
        btn_eliminar.bind(on_press=lambda x: self._eliminar_tarea(tarea_nombre.text))
        popup_layout.add_widget(btn_eliminar)

        popup = Popup(title='Eliminar Tarea', content=popup_layout, size_hint=(0.8, 0.4))
        popup.open()

    def _eliminar_tarea(self, tarea_nombre):
        """
        Método auxiliar para eliminar una tarea.
        """
        try:
            self.controlador.eliminar_tarea({
                "usuario": self.usuario_autenticado,  # Usar el usuario autenticado
                "tarea_nombre": tarea_nombre
            })
            self.mostrar_popup("Éxito", "Tarea eliminada con éxito!")
        except ValueError as e:
            self.mostrar_popup("Error", str(e))

    def cambiar_contrasena(self, instance):
        """
        Lógica para cambiar la contraseña.
        """
        popup_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        nueva_contrasena = TextInput(hint_text='Nueva contraseña', password=True)
        popup_layout.add_widget(nueva_contrasena)

        btn_cambiar = Button(text='Cambiar')
        btn_cambiar.bind(on_press=lambda x: self._cambiar_contrasena(nueva_contrasena.text))
        popup_layout.add_widget(btn_cambiar)

        popup = Popup(title='Cambiar Contraseña', content=popup_layout, size_hint=(0.8, 0.4))
        popup.open()

    def _cambiar_contrasena(self, nueva_contrasena):
        """
        Método auxiliar para cambiar la contraseña.
        """
        try:
            self.controlador.cambiar_contraseña({
                "id_usuario": self.usuario_autenticado,  # Usar el usuario autenticado
                "nueva_contraseña": nueva_contrasena
            })
            self.mostrar_popup("Éxito", "Contraseña cambiada con éxito!")
        except ValueError as e:
            self.mostrar_popup("Error", str(e))

    def cerrar_sesion(self, instance):
        """
        Lógica para cerrar sesión y volver a la pantalla de login.
        """
        self.manager.current = 'login'

    def mostrar_popup(self, titulo, mensaje):
        """
        Muestra un popup con un mensaje.

        Args:
            titulo (str): Título del popup.
            mensaje (str): Mensaje del popup.
        """
        popup_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        popup_layout.add_widget(Label(text=mensaje))
        btn_cerrar = Button(text="Cerrar", size_hint=(1, 0.5))
        popup_layout.add_widget(btn_cerrar)

        popup = Popup(title=titulo, content=popup_layout, size_hint=(0.8, 0.4))
        btn_cerrar.bind(on_press=popup.dismiss)
        popup.open()
