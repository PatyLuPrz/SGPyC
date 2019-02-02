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
        config.model_clientes.insert_persona(username_cl,nombre_cl,apellido_p_cl,apellido_m_cl,email_cl)
        # llama el metodo de insert_personas y le pasa los parametros guardados
        raise web.seeother('/clientes')
        # redirecciona al index
