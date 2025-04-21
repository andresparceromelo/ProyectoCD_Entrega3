from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from view.gui.welcome_screen import WelcomeScreen  # Nueva pantalla
from view.gui.login_screen import LoginScreen
from view.gui.register_screen import RegisterScreen
from view.gui.main_screen import MainScreen
from controller.app_controlador import AppControlador

class GestorTareasApp(App):
    def build(self):
        self.title = 'Gestor de Tareas'
        controlador = AppControlador()  # Crear una única instancia del controlador

        sm = ScreenManager()
        sm.add_widget(WelcomeScreen(name='welcome'))  # Agregar pantalla de bienvenida
        sm.add_widget(LoginScreen(controlador, name='login'))  # Pasar el controlador
        sm.add_widget(RegisterScreen(controlador, name='register'))  # Pasar el controlador
        sm.add_widget(MainScreen(controlador, name='main'))  # Pasar el controlador
        return sm

if __name__ == '__main__':
    GestorTareasApp().run()
