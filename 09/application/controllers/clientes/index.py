import web
import config as config

class Index:
    def __init__(self):
        pass
    
    def GET(self):
        personas = config.model_clientes.select_persona().list()
        # selecciona todos los registros de personas
        return config.render.index(personas)
        # envia los registros y renderiza index.html
