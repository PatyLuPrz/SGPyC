import web
import config as config

class View:
    def __init__(self):
        pass
    
    def GET(self,username_cl):
        persona = config.model_clientes.select_username(username_cl)
        # selecciona el registro que coincida con nombre
        return config.render.view(persona)
        # envia el registro y renderiza view.html
