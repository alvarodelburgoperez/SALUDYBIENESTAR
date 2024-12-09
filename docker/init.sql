CREATE TABLE clientes (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(100) NOT NULL,
    phone VARCHAR(20)  -- Permite más caracteres para el teléfono
);

CREATE TABLE proveedores (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    phone VARCHAR(15)
);

CREATE TABLE productos (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    stock INT NOT NULL
);

CREATE TABLE ofertas (
    id SERIAL PRIMARY KEY,
    product_id INT REFERENCES productos(id),
    discount DECIMAL(5, 2),
    start_date DATE,
    end_date DATE
);

CREATE TABLE mensajes (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    message VARCHAR(500) NOT NULL
);