import web

urls=(
    '/','application.controllers.index.index.Index',
    '/clientes','application.controllers.clientes.index.Index',
    '/clientes/update/(.*)','application.controllers.clientes.update.Update',
    '/clientes/insert','application.controllers.clientes.insert.Insert',
    '/clientes/delete/(.*)','application.controllers.clientes.delete.Delete',
    '/clientes/view/(.*)','application.controllers.clientes.view.View',
    '/productos','application.controllers.productos.index.Index',
    '/productos/update/(.*)','application.controllers.productos.update.Update',
    '/productos/insert','application.controllers.productos.insert.Insert',
    '/productos/delete/(.*)','application.controllers.productos.delete.Delete',
    '/productos/view/(.*)','application.controllers.productos.view.View'
)

if __name__ == '__main__':
    # web.config.debug = False
    app = web.application(urls,globals())
    app.run()

