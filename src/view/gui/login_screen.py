from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.app import App

class LoginScreen(Screen):
    def __init__(self, controlador, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.controlador = controlador  # Guardar la referencia al controlador

        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        layout.add_widget(Label(text='Iniciar Sesión', font_size=24))

        self.usuario_input = TextInput(hint_text='Usuario', multiline=False)
        layout.add_widget(self.usuario_input)

        self.contrasena_input = TextInput(hint_text='Contraseña', password=True, multiline=False)
        layout.add_widget(self.contrasena_input)

        btn_login = Button(text='Ingresar')
        btn_login.bind(on_press=self.validar_login)
        layout.add_widget(btn_login)

        btn_registrar = Button(text='Crear Cuenta')
        btn_registrar.bind(on_press=self.ir_a_registro)
        layout.add_widget(btn_registrar)

        # Botón "Salir"
        btn_salir = Button(
            text='Salir',
            background_color=(1, 0, 0, 1),  # Rojo
            size_hint=(1, 0.5)
        )
        btn_salir.bind(on_press=self.salir_aplicacion)
        layout.add_widget(btn_salir)

        self.add_widget(layout)

    def validar_login(self, instance):
        """
        Método para validar las credenciales de inicio de sesión.
        """
        usuario = self.usuario_input.text
        contrasena = self.contrasena_input.text

        try:
            self.controlador.iniciar_sesion({"id_usuario": usuario, "contraseña": contrasena})
            self.mostrar_popup("Inicio de sesión exitoso", f"Bienvenido, {usuario}!")
            self.limpiar_campos()  # Limpiar campos después de un inicio exitoso

            # Pasar el usuario autenticado a la pantalla principal
            self.manager.get_screen('main').usuario_autenticado = usuario
            self.manager.current = 'main'
        except ValueError as e:
            self.mostrar_popup("Error", str(e))
            self.limpiar_campos()  # Limpiar campos después de un intento fallido

    def ir_a_registro(self, instance):
        """
        Cambia a la pantalla de registro.
        """
        self.limpiar_campos()  # Limpiar campos al cambiar de pantalla
        self.manager.current = 'register'

    def salir_aplicacion(self, instance):
        """
        Cierra la aplicación.
        """
        App.get_running_app().stop()

    def limpiar_campos(self):
        """
        Limpia los campos de texto.
        """
        self.usuario_input.text = ""
        self.contrasena_input.text = ""

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