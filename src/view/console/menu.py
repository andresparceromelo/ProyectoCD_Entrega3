from controller.app_controlador import AppControlador


class Menu:
    """
    Representa el menú principal de la aplicación de gestión de tareas.
    """

    def __init__(self, controlador: AppControlador):
        """
        Inicializa el menú con una instancia del controlador.

        Args:
            controlador (AppControlador): Objeto que contiene la lógica de la aplicación.
        """
        self.controlador = controlador

    def __mostrar_opciones_principales(self):
        """
        Muestra las opciones disponibles en el menú principal.
        """
        print("""
  ╔══════════════════════════════╗
  ║     GESTOR DE TAREAS CLI     ║
  ╚══════════════════════════════╝
  1. Crear cuenta
  2. Iniciar sesión
  0. Salir
""")

    def __mostrar_opciones_usuario(self, usuario):
        """
        Muestra las opciones disponibles para un usuario autenticado.
        """
        print(f"""
  ╔══════════════════════════════╗
  ║    Bienvenido, {usuario}        ║
  ╚══════════════════════════════╝
  1. Crear tarea
  2. Ver mis tareas
  3. Editar tarea
  4. Eliminar tarea
  5. Cambiar contraseña
  0. Cerrar sesión
""")

    def iniciar(self):
        """
        Inicia el menú principal y gestiona las opciones seleccionadas por el usuario.
        """
        while True:
            self.__mostrar_opciones_principales()
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.__crear_cuenta()
            elif opcion == "2":
                self.__iniciar_sesion()
            elif opcion == "0":
                print("👋 Hasta luego!")
                break
            else:
                print("❌ Opción no válida.")

    def __crear_cuenta(self):
        """
        Lógica para crear una cuenta de usuario.
        """
        try:
            user = input("  Ingrese nombre de usuario: ")
            pwd = input("  Ingrese contraseña: ")
            self.controlador.crear_cuenta({"id_usuario": user, "contraseña": pwd})
            print("  ✅ Cuenta creada exitosamente!")
        except Exception as e:
            print(f"  ❌ Error: {e}")

    def __iniciar_sesion(self):
        """
        Lógica para iniciar sesión.
        """
        user = input("  Usuario: ")
        pwd = input("  Contraseña: ")
        try:
            self.controlador.iniciar_sesion({"id_usuario": user, "contraseña": pwd})
            print("  ✅ Inicio de sesión exitoso!")
            self.__menu_usuario(user)
        except Exception as e:
            print(f"  ❌ Error: {e}")

    def __menu_usuario(self, usuario):
        """
        Muestra el menú para un usuario autenticado y gestiona sus opciones.
        """
        while True:
            self.__mostrar_opciones_usuario(usuario)
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.__crear_tarea(usuario)
            elif opcion == "2":
                self.__ver_tareas(usuario)
            elif opcion == "3":
                self.__editar_tarea(usuario)
            elif opcion == "4":
                self.__eliminar_tarea(usuario)
            elif opcion == "5":
                self.__cambiar_contraseña(usuario)
            elif opcion == "0":
                break
            else:
                print("❌ Opción no válida.")

    def __crear_tarea(self, usuario):
        """
        Lógica para crear una tarea.
        """
        try:
            texto = input("  Descripción de la tarea: ")
            categoria = input("  Categoría: ")
            estado = input("  Estado (Por hacer, En progreso, Completada): ")
            self.controlador.crear_tarea({
                "usuario_creador": usuario,
                "txt_tarea": texto,
                "categoria": categoria,
                "estado": estado
            })
            print("  ✅ Tarea creada!")
        except Exception as e:
            print(f"  ❌ Error: {e}")

    def __ver_tareas(self, usuario):
        """
        Lógica para mostrar las tareas de un usuario.
        """
        tareas = self.controlador.obtener_tareas(usuario)
        if not tareas:
            print("\n  No tienes tareas registradas.")
        else:
            print("\n  Tus tareas:")
            for i, tarea in enumerate(tareas, 1):
                print(f"  {i}. [{tarea['estado']}] {tarea['txt_tarea']} - Categoría: {tarea['categoria']}")

    def __editar_tarea(self, usuario):
        """
        Lógica para editar una tarea.
        """
        try:
            tarea_original = input("  Nombre exacto de la tarea a editar: ")
            nuevo_texto = input("  Nuevo texto: ")
            nueva_categoria = input("  Nueva categoría: ")
            nuevo_estado = input("  Nuevo estado (Por hacer, En progreso, Completada): ")
            self.controlador.editar_tarea({
                "usuario": usuario,
                "tarea_original": tarea_original,
                "nuevo_texto": nuevo_texto,
                "nueva_categoria": nueva_categoria,
                "nuevo_estado": nuevo_estado
            })
            print("  ✅ Tarea actualizada!")
        except Exception as e:
            print(f"  ❌ Error: {e}")

    def __eliminar_tarea(self, usuario):
        """
        Lógica para eliminar una tarea.
        """
        try:
            tarea_nombre = input("  Nombre exacto de la tarea a eliminar: ")
            self.controlador.eliminar_tarea({"usuario": usuario, "tarea_nombre": tarea_nombre})
            print("  ✅ Tarea eliminada!")
        except Exception as e:
            print(f"  ❌ Error: {e}")

    def __cambiar_contraseña(self, usuario):
        """
        Lógica para cambiar la contraseña de un usuario.
        """
        try:
            nueva_pwd = input("  Nueva contraseña: ")
            self.controlador.cambiar_contraseña({"id_usuario": usuario, "nueva_contraseña": nueva_pwd})
            print("  ✅ Contraseña actualizada!")
        except Exception as e:
            print(f"  ❌ Error: {e}")