import web
# importa la libreria de webpy

import application.models.model_productos as model_productos
# importa el modelo_productos

render = web.template.render('application/views/productos',base='../master')
# configura la ubicacion de las vistas
