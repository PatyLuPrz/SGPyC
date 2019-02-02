import web
import config as config

class View:
    def __init__(self):
        pass
    
    def GET(self,clave_p):
        persona = config.model_productos.select_clave(clave_p)
        # selecciona el registro que coincida con nombre
        return config.render.view(persona)
        # envia el registro y renderiza view.html