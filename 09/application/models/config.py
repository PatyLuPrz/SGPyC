import web

db = web.database(
    dbn = 'mysql', # motor de la base de datos
    host = 'localhost', # ruta del servidor
    db = 'ria_mppm', # nombre de la bd
    user = 'root' # usuario de la bd
)
