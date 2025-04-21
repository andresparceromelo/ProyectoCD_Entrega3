from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup

class RegisterScreen(Screen):
    def __init__(self, controlador, **kwargs):
        super(RegisterScreen, self).__init__(**kwargs)
        self.controlador = controlador  # Guardar la referencia al controlador

        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        layout.add_widget(Label(text='Registro de Usuario', font_size=24))

        self.nuevo_usuario_input = TextInput(hint_text='Nuevo usuario', multiline=False)
        layout.add_widget(self.nuevo_usuario_input)

        self.nueva_contrasena_input = TextInput(hint_text='Nueva contraseña', password=True, multiline=False)
        layout.add_widget(self.nueva_contrasena_input)

        btn_registrar = Button(text='Registrar')
        btn_registrar.bind(on_press=self.registrar_usuario)
        layout.add_widget(btn_registrar)

        btn_volver = Button(text='Volver al Login')
        btn_volver.bind(on_press=self.volver_login)
        layout.add_widget(btn_volver)

        self.add_widget(layout)

    def registrar_usuario(self, instance):
        """
        Lógica para registrar un nuevo usuario.
        """
        usuario = self.nuevo_usuario_input.text
        contrasena = self.nueva_contrasena_input.text

        try:
            self.controlador.crear_cuenta({"id_usuario": usuario, "contraseña": contrasena})
            self.mostrar_popup("Éxito", "Cuenta creada con éxito!")
            self.limpiar_campos()  # Limpiar campos después de un registro exitoso
            self.manager.current = 'login'
        except ValueError as e:
            self.mostrar_popup("Error", str(e))
            self.limpiar_campos()  # Limpiar campos después de un intento fallido

    def volver_login(self, instance):
        """
        Cambia a la pantalla de login.
        """
        self.limpiar_campos()  # Limpiar campos al cambiar de pantalla
        self.manager.current = 'login'

    def limpiar_campos(self):
        """
        Limpia los campos de texto.
        """
        self.nuevo_usuario_input.text = ""
        self.nueva_contrasena_input.text = ""

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
