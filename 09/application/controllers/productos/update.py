import web
import config as config

class Update:
    def __init__(self):
        pass
    
    def GET(self, clave_p):
        producto = config.model_productos.select_clave(clave_p)
        # selecciona un registro que conincida con nombre
        return config.render.update(producto)
        # Envia el registro y renderiza update.html

    def POST(self, clave):
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
        config.model_productos.update_producto(clave_p,nombre_p,precio_p,marca_p,proveedor_p)
        # le pasa los datos a el metodo update en el modelo
        raise web.seeother('/productos')
        # redirecciona al index
