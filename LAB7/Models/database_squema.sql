CREATE DATABASE IF NOT EXISTS lab7
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

USE lab7;

CREATE TABLE IF NOT EXISTS users (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    username VARCHAR(100) NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    PRIMARY KEY (id),
    UNIQUE KEY uq_users_username (username)
);
