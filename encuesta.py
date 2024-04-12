from pregunta import Pregunta
from usuario import Usuario, ListadoRespuestas

class Encuesta:
    def __init__(self, nombre:str, preguntas:list):
        self.nombre = nombre
        self.__preguntas = [
            Pregunta(
                p["enunciado"],
                p["ayuda"],
                p["requerido"],
                p["lista_alternativas"]
            ) for p in preguntas
        ]
        
        self.__listado_respuestas = []

    def mostrar_encuesta(self):
        print("Nombre de la encuesta:", self.nombre)
        
        if self.preguntas:
            print("Preguntas:")
            for p in self.__preguntas:
                p.mostrar_pregunta()

    def agregar_listado_respuestas(self, listado_respuestas):
        self.respuestas.append(listado_respuestas)


class EncuestaLimitadaEdad(Encuesta):
    def __init__(self, nombre: str, edad_minima:int, edad_maxima: int, preguntas: list):
        super().__init__(nombre, preguntas)
        self.__edad_minima = edad_minima
        self.__edad_maxima = edad_maxima

    @property
    def edad_minima(self):
        return self.__edad_minima
    
    @edad_minima.setter
    def edad_minima(self, nueva_edad):
        self.__edad_minima = nueva_edad

    @property
    def edad_maxima(self):
        return self.__edad_maxima
    
    @edad_maxima.setter
    def edad_maxima(self, nueva_edad):
        self.__edad_maxima = nueva_edad

    def validar_edad(self):
        return self.__edad_minima <= self.edad <= self.__edad_maxima

    def agregar_respuesta(self, respuestas: list):
        if self.validar_edad():
            super().agregar_listado_respuestas(respuestas)


class EncuestaLimitadaRegion(Encuesta):
    def __init__(self, nombre:str, lista_regiones:list, preguntas: list):
        super().__init__(nombre, preguntas)
        self.regiones = lista_regiones

    def validar_region(self):
        return self.region 

    def agregar_respuesta(self, respuestas: list):
        if self.validar_region():
            super().agregar_listado_respuestas(respuestas)
