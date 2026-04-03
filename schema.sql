CREATE DATABASE IF NOT EXISTS auth_flask;
USE auth_flask;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);

INSERT IGNORE INTO users (name, email, password)
VALUES ('João', 'joao@email.com', 'senha123');
