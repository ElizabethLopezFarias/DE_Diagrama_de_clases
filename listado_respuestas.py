class ListadoRespuestas:
    def __init__(self, usuario):
        self.usuario = usuario
        self.respuestas = []

    def agregar_respuesta(self, respuesta):
        self.respuestas.append(respuesta)
