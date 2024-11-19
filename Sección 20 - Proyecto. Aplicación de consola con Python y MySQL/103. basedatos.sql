CREATE DATABASE IF NOT EXISTS master_python;
USE master_python;

-- Crear tabla de usuarios
CREATE TABLE usuarios (
    id INT AUTO_INCREMENT NOT NULL,
    nombre VARCHAR(200),
    apellidos VARCHAR(500),
    email VARCHAR(500) NOT NULL,
    password VARCHAR(500) NOT NULL,
    fecha DATE NOT NULL,
    CONSTRAINT pk_usuarios PRIMARY KEY(id),
    CONSTRAINT uq_email UNIQUE(email)
) ENGINE=InnoDB;

-- Crear tabla de notas
CREATE TABLE notas (
    id INT AUTO_INCREMENT NOT NULL,
    usuario_id INT NOT NULL,
    titulo VARCHAR(300) NOT NULL,
    descripcion MEDIUMTEXT,
    fecha DATE NOT NULL,
    CONSTRAINT pk_notas PRIMARY KEY(id),
    CONSTRAINT fk_nota_usuario FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
) ENGINE=InnoDB;
-- Ejecutarlo dentro de MySQL