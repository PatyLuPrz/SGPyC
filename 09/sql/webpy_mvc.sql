CREATE DATABASE ria_mppm;

USE ria_mppm;

CREATE TABLE clientes(
    username_cl      varchar(30)     NOT NULL    PRIMARY KEY,
    nombre_cl        varchar(59)     NOT NULL,
    apellido_p_cl    varchar(50)     NOT NULL,
    apellido_m_cl    varchar(50)     NOT NULL,
    email_cl         varchar(50)     NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE productos(
    clave_p       varchar(15)     NOT NULL    PRIMARY KEY,
    nombre_p      varchar(50)     NOT NULL,
    precio_p      varchar(5)      NOT NULL,
    marca_p       varchar(50)     NOT NULL,
    proveedor_p   varchar(50)     NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


INSERT INTO clientes(username_cl, nombre_cl, apellido_p_cl, apellido_m_cl,email_cl) VALUES
('adogamm','Adolfo','Leon','Barron','adolfo.leba@correo.com'),
('danni_pink','Daniela','Rubiales','Marquez','danni_06@correo.com'),
('arelux','Arely','Leon','Castro','arely_leon@correo.com');

INSERT INTO productos(clave_p,nombre_p,precio_p,marca_p,proveedor_p) VALUES
('PBPC-01','Lapices','6.0','PencilPluss','Pencils Inc'),
('PBPC-02','Gomas','2.0','BorraTodo','NoMoreMistakes Company'),
('PBPC-03','Tijeras','10.0','MaxiFilo','Tijeras y algo más');


SHOW TABLES;

SELECT * FROM clientes;

DESCRIBE clientes;

SELECT * FROM productos;

DESCRIBE productos;

CREATE USER 'ria'@'localhost' IDENTIFIED BY 'ria.2019';
GRANT ALL PRIVILEGES ON ria_mppm.* TO 'ria'@'localhost';
FLUSH PRIVILEGES;
