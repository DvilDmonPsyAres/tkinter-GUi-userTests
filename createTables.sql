CREATE TABLE pacientes (
    paciente_id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre VARCHAR(100) NOT NULL,
    apellidos VARCHAR(100) NOT NULL,
    fecha_de_nacimiento DATE,
    genero VARCHAR(1) NOT NULL
);

-- Tabla Resultados
CREATE TABLE resultados_prueba_uno(
    prueba_id INTEGER PRIMARY KEY AUTOINCREMENT,
    paciente_id INTEGER,
    fecha_de_prueba DATE NOT NULL,
    tipo_prueba INTEGER NOT NULL,
    resultado VARCHAR(100),
    FOREIGN KEY(paciente_id) REFERENCES pacientes(paciente_id) 
);