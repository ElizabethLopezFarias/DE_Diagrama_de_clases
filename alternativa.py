class Alternativa:
    def __init__(self, contenido: str, ayuda:str):
        self.contenido = contenido
        self.ayuda = ayuda

    def mostrar_alternativa(self):
        print("Contenido:", self.contenido)
        if self.ayuda:
            print("Ayuda:", self.ayuda)


# #prueba
# if __name__ == "__main__":
#     # Crear una alternativa
#     alternativa1 = Alternativa("Opción A", "Esta es la opción A")
    
#     # Mostrar la alternativa
#     alternativa1.mostrar_alternativa()
