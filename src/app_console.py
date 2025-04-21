from view.console.menu import Menu
from controller.app_controlador import AppControlador

if __name__ == "__main__":
    app_controlador = AppControlador()
    Menu(app_controlador).iniciar()
    