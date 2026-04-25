# Investigue qué usos se le pueden dar a la herencia multiple y cree un ejemplo.
#   Herencia:
#   Combinar comportamientos de distintas fuentes sin repetir código
#   Modelar objetos del mundo real que tienen múltiples roles
#   Crear mixins (clases pequeñas que agregan una funcionalidad específica) 
#   Si dos clases padre tienen un método con el mismo nombre, Python necesita saber cuál usar primero. 
#   Lo resuelve con el MRO (Method Resolution Order), que va de izquierda a derecha.

class Frontend:
    def design_interface(self):
        print("Designing the user interface 🎨")

    def handle_css(self):
        print("Applying styles with CSS 💅")

class Backend:
    def handle_database(self):
        print("Querying the database 🗄️")

    def create_api(self):
        print("Creating API endpoints 🔌")

class FullStackDeveloper(Frontend, Backend):  # inherits from both
    def introduce(self):
        print("I'm Full Stack, I can do it all! 💻")

dev = FullStackDeveloper()
dev.design_interface()    # Designing the user interface 🎨
dev.handle_css()          # Applying styles with CSS 💅
dev.handle_database()     # Querying the database 🗄️
dev.create_api()          # Creating API endpoints 🔌
dev.introduce()           # I'm Full Stack, I can do it all! 💻