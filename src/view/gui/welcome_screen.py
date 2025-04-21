from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class WelcomeScreen(Screen):
    def __init__(self, **kwargs):
        super(WelcomeScreen, self).__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        # Título
        layout.add_widget(Label(
            text='ADMINISTRADOR DE TAREAS',
            font_size=32,
            bold=True,
            halign='center',
            valign='middle'
        ))

        # Botón "Empieza Ahora"
        btn_empezar = Button(
            text='EMPIEZA AHORA',
            font_size=24,
            size_hint=(0.5, 0.2),
            pos_hint={'center_x': 0.5}
        )
        btn_empezar.bind(on_press=self.ir_a_login)
        layout.add_widget(btn_empezar)

        self.add_widget(layout)

    def ir_a_login(self, instance):
        """
        Cambia a la pantalla de inicio de sesión.
        """
        self.manager.current = 'login'