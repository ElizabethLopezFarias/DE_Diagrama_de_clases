class Usuario:
    def __init__(self, correo: str, edad: int, region: int):
        self.correo = correo
        self.edad = edad
        self.region = region

    def responder_encuesta(self, encuesta):
        listado_respuestas = ListadoRespuestas(self)
        encuesta.agregar_listado_respuestas(listado_respuestas)


class ListadoRespuestas:
    def __init__(self, usuario):
        self.usuario = usuario
        self.respuestas = []

    def agregar_respuesta(self, respuesta):
        self.respuestas.append(respuesta)

