import web
import config as config

class Insert:
    def __init__(self):
        pass
    
    def GET(self):
        return config.render.insert()
        # renderiza la pagina insert.html
    
    def POST(self):
        formulario = web.input()
        # almacena los datos del formulario
        clave_p = formulario['clave_p']
        # almacena los datos del formulario
        nombre_p = formulario['nombre_p']
        # almacena los datos del formulario
        precio_p = formulario['precio_p']
        # almacena el nombre desde el formulario
        marca_p = formulario['marca_p']
        # almacena el nombre desde el formulario
        proveedor_p = formulario['proveedor_p']
        # almacena el email desde el formulario
        config.model_productos.insert_producto(clave_p,nombre_p,precio_p,marca_p,proveedor_p)
        # llama el metodo de insert_personas y le pasa los parametros guardados
        raise web.seeother('/productos')
        # redirecciona al index
