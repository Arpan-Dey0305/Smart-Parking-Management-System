-- Create the database
CREATE DATABASE IF NOT EXISTS DATABASE_NAME;

-- Use the database
USE DATABASE_NAME;

-- Create the table
CREATE TABLE IF NOT EXISTS TABLE_NAME (
    id INT AUTO_INCREMENT PRIMARY KEY,
    car_no VARCHAR(10) NOT NULL,
    car_type VARCHAR(10) NOT NULL,
    unique_code VARCHAR(20) NOT NULL UNIQUE,
    entry_time DATETIME NOT NULL,
    exit_time DATETIME,
    charge DECIMAL(10, 2)
);
