-- Crear tabla Ciudad
CREATE TABLE Ciudad (
    id INT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    provincia VARCHAR(255) NOT NULL,
    codigo_postal VARCHAR(10) 
);

-- Crear tabla Persona
CREATE TABLE Persona (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    apellido VARCHAR(255) NOT NULL,
    dni VARCHAR(10) NOT NULL,
    email VARCHAR(255) NOT NULL,
    fecha_nacimiento DATE,
    telefono VARCHAR(15),
    ciudad_id INT, -- Clave foránea para relacionar con Ciudad
    CONSTRAINT unique_dni UNIQUE (dni), -- Asegurar que el DNI sea único
    CONSTRAINT unique_email UNIQUE (email), -- Asegurar que el email sea único
    CONSTRAINT unique_telefono UNIQUE (telefono), -- Asegurar que el teléfono sea único
    CONSTRAINT fk_ciudad FOREIGN KEY (ciudad_id) REFERENCES Ciudad(id)
);


-- Insertar ciudades
INSERT INTO Ciudad (id,nombre, provincia, codigo_postal) VALUES
    (1, 'Cordoba Capital', 'Cordoba', '5000'),
    (2, 'Villa Maria', 'Cordoba', '5900'),
    (3, 'Rio Cuarto', 'Cordoba', '5800'),
    (4, 'San Francisco', 'Cordoba', '2400'),
    (5, 'Villa Nueva', 'Cordoba', '5901'),
    (6, 'Las Higueras', 'Cordoba', '5805'),
    (7, 'Junin', 'Buenos Aires', '6000'),
    (8, 'Vedia', 'Buenos Aires', '6030'),
    (9, 'La Plata', 'Buenos Aires', '1900'),
    (10, 'Mar del Plata', 'Buenos Aires', '7600'),
    (11, 'Rosario', 'Santa Fe', '2000'),
    (12, 'Santa Fe', 'Santa Fe', '3000'),
    (13, 'Parana', 'Entre Rios', '3100'),
    (14, 'Mendoza', 'Mendoza', '5500'),
    (15, 'San Juan', 'San Juan', '5400'),
    (16, 'Salta', 'Salta', '4400'),
    (17, 'Tucuman', 'Tucuman', '4000');
    

-- Insertar personas
INSERT INTO Persona (nombre, apellido, dni, email, fecha_nacimiento, telefono, ciudad_id) VALUES
    ('Juan', 'Perez', '12345678A', 'juan@example.com', '1990-05-15', '555-123-456', 1),
    ('Maria', 'Lopez', '98765432B', 'maria@example.com', '1985-09-20', '555-789-123', 1);
