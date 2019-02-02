import config as config 
# importa el archivo config

db = config.db 
# crea un objeto del objeto db creado en config


# Metodo para seleccionar todos los registros de productos
def select_producto():
    try:
        return db.select('productos',vars=locals())
        # selecciona todos los registros de la tabla
    except Exception as e:
        print "Model select_productos Error {}",format(e.args)
        print "Model select_productos Message {}",format(e.message)
        return None

# Metodo para seleccionar un registro que coincida con el username dado  
def select_clave(clave_p):
    try:
        return db.select('productos',where='clave_p=$clave_p',vars=locals())[0] 
        # selecciona el primer registro que coincida con el username
    except Exception as e:
        print "Model select_nombre Error {}",format(e.args)
        print "Model select_nombre Message {}",format(e.message)
        return None

# Metodo para insertar un nuevo registro

def insert_producto(clave_p, nombre_p,precio_p,marca_p,proveedor_p):
    try:
        return db.insert('productos',
        clave_p=clave_p,
        nombre_p=nombre_p,
        precio_p=precio_p,
        marca_p=marca_p,
        proveedor_p=proveedor_p)
        # Inserta un registro en productos
    except Exception as e:
        print "Model insert_productos Error {}",format(e.args)
        print "Model insert_productos Message {}",format(e.message)
        return None

# Metodo para eliminar un registro que coincida con el username recibido

def delete_producto(clave_p):
    try:
        return db.delete('productos',where='clave_p=$clave_p',vars=locals())
        # borra un registro de productos
    except Exception as e:
        print "Model delete_productos Error {}",format(e.args)
        print "Model detele_productos Message {}",format(e.message)
        return None

# Metodo para actualizar el email, del nombre recibido

def update_producto(clave_p, nombre_p,precio_p,marca_p,proveedor_p):
    try:
        return db.update('productos',
        nombre_p=nombre_p,
        precio_p=precio_p,
        marca_p=marca_p,
        proveedor_p=proveedor_p
        , where='clave_p=$clave_p', vars=locals())
        # Actualiza el email de las productos que coincidan con el nombre dado
    except Exception as e:
        print "Model update_productos Error {}",format(e.args)
        print "Model update_productos Message {}",format(e.message)
        return None
