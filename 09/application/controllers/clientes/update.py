import web
import config as config

class Update:
    def __init__(self):
        pass
    
    def GET(self, nombre):
        persona = config.model_clientes.select_username(nombre)
        # selecciona un registro que conincida con nombre
        return config.render.update(persona)
        # Envia el registro y renderiza update.html

    def POST(self, email):
        formulario = web.input()
        # almacena los datos del formulario
        username_cl = formulario['username_cl']
        # almacena los datos del formulario
        nombre_cl = formulario['nombre_cl']
        # almacena los datos del formulario
        apellido_p_cl = formulario['apellido_p_cl']
        # almacena el nombre desde el formulario
        apellido_m_cl = formulario['apellido_m_cl']
        # almacena el nombre desde el formulario
        email_cl = formulario['email_cl']
        # almacena el email desde el formulario
        config.model_clientes.update_persona(username_cl,nombre_cl,apellido_p_cl,apellido_m_cl,email_cl)
        # le pasa los datos a el metodo update en el modelo
        raise web.seeother('/clientes')
        # redirecciona al index
