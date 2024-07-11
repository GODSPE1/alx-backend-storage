-- Script that creates a table called users without failing
-- id INT
-- email: string
-- name: string

CREATE TABLE IF NOT EXISTS `users` (
    `id` INT NULL AUTO_INCREMENT PRIMARY KEY,
    `email` VARCHAR(255) NOT NULL UNIQUE,
    `name` VARCHAR(255)
);