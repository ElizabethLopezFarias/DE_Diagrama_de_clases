from alternativa import Alternativa

class Pregunta:
    def __init__(self, enunciado: str, ayuda:str, requerido: bool, alternativas: list):
        self.enunciado = enunciado
        self.ayuda = ayuda
        self.requerido = requerido
        #Crea un objeto de la clase Alternativa e luego itera en la lista alternativas
        self.__lista_alternativas = [Alternativa(a["contenido"], a["ayuda"]) for a in alternativas]

    def mostrar_pregunta(self):
        # imprime el enunciado
        print("Enunciado:", self.enunciado)
        # si existe contenido en ayuda lo imprimirá
        if self.ayuda:
            print("Ayuda:", self.ayuda)
        #imprime si es requerido
        print("Requerido:", self.requerido)
        # itera sobre self.__lista_alternativas para llamar al método mostrar_alternativa()
        for a in self.__lista_alternativas:
            a.mostrar_alternativa()


 