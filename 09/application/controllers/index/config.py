import web
# importa la libreria de webpy

import application.models.model_index as model_index
# importa el modelo_persona

render = web.template.render('application/views/index',base='../master')
# configura la ubicacion de las vistas
