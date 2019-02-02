import web
# importa la libreria de webpy

import application.models.model_clientes as model_clientes
# importa el modelo_persona

render = web.template.render('application/views/clientes',base='../master')
# configura la ubicacion de las vistas
