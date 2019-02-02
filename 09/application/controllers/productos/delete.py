import web
import config as config

class Delete:
    def __init__(self):
        pass
    
    def GET(self, clave):
        personas = config.model_productos.select_clave(clave)
        # selecciona el registro que coincida con nombre
        return config.render.delete(personas)
        # envia el registro y renderiza delete.html

    def POST(self, clave_p):
        formulario = web.input()
        # atrapa los datos en el formulario
        clave_p = formulario['clave_p']
        # guarda el nombre desde el formulario
        config.model_productos.delete_producto(clave_p)
        # le pasa los parametros al metodo delete en el modelo
        raise web.seeother('/productos')
        # redirecciona al index
