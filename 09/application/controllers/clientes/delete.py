import web
import config as config

class Delete:
    def __init__(self):
        pass
    
    def GET(self, username_cl):
        personas = config.model_clientes.select_username(username_cl)
        # selecciona el registro que coincida con nombre
        return config.render.delete(personas)
        # envia el registro y renderiza delete.html

    def POST(self, username_cl):
        formulario = web.input()
        # atrapa los datos en el formulario
        username_cl = formulario['username_cl']
        # guarda el nombre desde el formulario
        config.model_clientes.delete_persona(username_cl)
        # le pasa los parametros al metodo delete en el modelo
        raise web.seeother('/clientes')
        # redirecciona al index
