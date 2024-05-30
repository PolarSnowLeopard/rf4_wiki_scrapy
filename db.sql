DROP DATABASE IF EXISTS rf4_wiki;
CREATE DATABASE rf4_wiki;
USE rf4_wiki;

CREATE TABLE food (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    description TEXT,
    img VARCHAR(255),
    type VARCHAR(255),
    class VARCHAR(255),
    producer VARCHAR(255),
    price VARCHAR(255)
);

CREATE TABLE fish (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    description TEXT,
    img VARCHAR(255),
    class VARCHAR(255),
    rare_weight VARCHAR(255),
    super_rare_weight VARCHAR(255)
);
