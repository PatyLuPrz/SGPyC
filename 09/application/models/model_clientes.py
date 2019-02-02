import config as config 
# importa el archivo config

db = config.db 
# crea un objeto del objeto db creado en config


# Metodo para seleccionar todos los registros de clientes
def select_persona():
    try:
        return db.select('clientes',vars=locals())
        # selecciona todos los registros de la tabla
    except Exception as e:
        print "Model select_clientes Error {}",format(e.args)
        print "Model select_clientes Message {}",format(e.message)
        return None

# Metodo para seleccionar un registro que coincida con el username dado  
def select_username(username_cl):
    try:
        return db.select('clientes',where='username_cl=$username_cl',vars=locals())[0] 
        # selecciona el primer registro que coincida con el username
    except Exception as e:
        print "Model select_nombre Error {}",format(e.args)
        print "Model select_nombre Message {}",format(e.message)
        return None

# Metodo para insertar un nuevo registro

def insert_persona(username_cl, nombre_cl,apellido_p_cl,apellido_m_cl,email_cl):
    try:
        return db.insert('clientes',
        username_cl=username_cl,
        nombre_cl=nombre_cl,
        apellido_p_cl=apellido_p_cl,
        apellido_m_cl=apellido_m_cl,
        email_cl=email_cl)
        # Inserta un registro en clientes
    except Exception as e:
        print "Model insert_clientes Error {}",format(e.args)
        print "Model insert_clientes Message {}",format(e.message)
        return None

# Metodo para eliminar un registro que coincida con el username recibido

def delete_persona(username_cl):
    try:
        return db.delete('clientes',where='username_cl=$username_cl',vars=locals())
        # borra un registro de clientes
    except Exception as e:
        print "Model delete_clientes Error {}",format(e.args)
        print "Model detele_clientes Message {}",format(e.message)
        return None

# Metodo para actualizar el email, del nombre recibido

def update_persona(username_cl, nombre_cl,apellido_p_cl,apellido_m_cl,email_cl):
    try:
        return db.update('clientes',
        nombre_cl=nombre_cl,
        apellido_p_cl=apellido_p_cl,
        apellido_m_cl=apellido_m_cl,
        email_cl=email_cl
        , where='username_cl=$username_cl', vars=locals())
        # Actualiza el email de las clientes que coincidan con el nombre dado
    except Exception as e:
        print "Model update_clientes Error {}",format(e.args)
        print "Model update_clientes Message {}",format(e.message)
        return None
