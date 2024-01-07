-- Create the database for Aura_Merchandise
CREATE DATABASE Aura_Merchandise;
USE Aura_Merchandise;

-- Create the t_shirts table
CREATE TABLE t_shirts (
    t_shirt_id INT AUTO_INCREMENT PRIMARY KEY,
    brand ENUM('Van Huesen', 'Levi', 'Nike', 'Adidas') NOT NULL,
    color ENUM('Red', 'Blue', 'Black', 'White') NOT NULL,
    size ENUM('XS', 'S', 'M', 'L', 'XL') NOT NULL,
    price INT CHECK (price BETWEEN 10 AND 50),
    stock_quantity INT NOT NULL,
    UNIQUE KEY brand_color_size (brand, color, size)
);

-- Create the hats table
CREATE TABLE hats (
    hat_id INT AUTO_INCREMENT PRIMARY KEY,
    brand ENUM('New Era', 'Nike', 'Adidas', 'Puma') NOT NULL,
    color ENUM('Red', 'Blue', 'Black', 'White') NOT NULL,
    size ENUM('Small', 'Medium', 'Large') NOT NULL,
    price INT CHECK (price BETWEEN 5 AND 30),
    stock_quantity INT NOT NULL,
    UNIQUE KEY brand_color_size (brand, color, size)
);

-- Create the shoes table
CREATE TABLE shoes (
    shoe_id INT AUTO_INCREMENT PRIMARY KEY,
    brand ENUM('Nike', 'Adidas', 'Puma', 'Reebok') NOT NULL,
    color ENUM('Red', 'Blue', 'Black', 'White') NOT NULL,
    size INT CHECK (size BETWEEN 5 AND 12),
    price INT CHECK (price BETWEEN 20 AND 100),
    stock_quantity INT NOT NULL,
    UNIQUE KEY brand_color_size (brand, color, size)
);

-- Create the accessories table
CREATE TABLE accessories (
    accessory_id INT AUTO_INCREMENT PRIMARY KEY,
    type ENUM('Belt', 'Watch', 'Sunglasses', 'Wallet') NOT NULL,
    brand ENUM('Fossil', 'Casio', 'Ray-Ban', 'Levi') NOT NULL,
    color ENUM('Red', 'Blue', 'Black', 'White', 'Brown') NOT NULL,
    price INT CHECK (price BETWEEN 5 AND 150),
    stock_quantity INT NOT NULL
);

-- Add a discounts table applicable to all merchandise
CREATE TABLE discounts (
    discount_id INT AUTO_INCREMENT PRIMARY KEY,
    merchandise_id INT NOT NULL,
    merchandise_type ENUM('T-Shirt', 'Hat', 'Shoe', 'Accessory') NOT NULL,
    pct_discount DECIMAL(5,2) CHECK (pct_discount BETWEEN 0 AND 100)
    -- Note: Add foreign key constraints as necessary
);

-- Insert sample records into the discounts table
-- Note: You'll need to adjust these inserts based on actual IDs and types from your tables
INSERT INTO discounts (merchandise_id, merchandise_type, pct_discount)
VALUES
(1, 'T-Shirt', 10.00),
(2, 'Hat', 15.00),
(3, 'Shoe', 20.00),
(4, 'Accessory', 5.00);

-- Continue using the Aura_Merchandise database
USE Aura_Merchandise;

-- Stored procedure to populate the t_shirts table
DELIMITER $$
CREATE PROCEDURE PopulateTShirts()
BEGIN
    DECLARE counter INT DEFAULT 0;
    DECLARE max_records INT DEFAULT 100;
    DECLARE brand ENUM('Van Huesen', 'Levi', 'Nike', 'Adidas');
    DECLARE color ENUM('Red', 'Blue', 'Black', 'White');
    DECLARE size ENUM('XS', 'S', 'M', 'L', 'XL');
    DECLARE price INT;
    DECLARE stock INT;

    SET SESSION rand_seed1 = UNIX_TIMESTAMP();

    WHILE counter < max_records DO
        SET brand = ELT(FLOOR(1 + RAND() * 4), 'Van Huesen', 'Levi', 'Nike', 'Adidas');
        SET color = ELT(FLOOR(1 + RAND() * 4), 'Red', 'Blue', 'Black', 'White');
        SET size = ELT(FLOOR(1 + RAND() * 5), 'XS', 'S', 'M', 'L', 'XL');
        SET price = FLOOR(10 + RAND() * 41);
        SET stock = FLOOR(10 + RAND() * 91);

        BEGIN
            DECLARE CONTINUE HANDLER FOR 1062 BEGIN END;
            INSERT INTO t_shirts (brand, color, size, price, stock_quantity)
            VALUES (brand, color, size, price, stock);
            SET counter = counter + 1;
        END;
    END WHILE;
END$$
DELIMITER ;

-- Stored procedure to populate the hats table
DELIMITER $$
CREATE PROCEDURE PopulateHats()
BEGIN
    DECLARE counter INT DEFAULT 0;
    DECLARE max_records INT DEFAULT 50;
    DECLARE brand ENUM('New Era', 'Nike', 'Adidas', 'Puma');
    DECLARE color ENUM('Red', 'Blue', 'Black', 'White');
    DECLARE size ENUM('Small', 'Medium', 'Large');
    DECLARE price INT;
    DECLARE stock INT;

    SET SESSION rand_seed1 = UNIX_TIMESTAMP();

    WHILE counter < max_records DO
        SET brand = ELT(FLOOR(1 + RAND() * 4), 'New Era', 'Nike', 'Adidas', 'Puma');
        SET color = ELT(FLOOR(1 + RAND() * 4), 'Red', 'Blue', 'Black', 'White');
        SET size = ELT(FLOOR(1 + RAND() * 3), 'Small', 'Medium', 'Large');
        SET price = FLOOR(5 + RAND() * 26);
        SET stock = FLOOR(5 + RAND() * 46);

        BEGIN
            DECLARE CONTINUE HANDLER FOR 1062 BEGIN END;
            INSERT INTO hats (brand, color, size, price, stock_quantity)
            VALUES (brand, color, size, price, stock);
            SET counter = counter + 1;
        END;
    END WHILE;
END$$
DELIMITER ;

-- Stored procedure to populate the shoes table
DELIMITER $$
CREATE PROCEDURE PopulateShoes()
BEGIN
    DECLARE counter INT DEFAULT 0;
    DECLARE max_records INT DEFAULT 50;
    DECLARE brand ENUM('Nike', 'Adidas', 'Puma', 'Reebok');
    DECLARE color ENUM('Red', 'Blue', 'Black', 'White');
    DECLARE size INT;
    DECLARE price INT;
    DECLARE stock INT;

    SET SESSION rand_seed1 = UNIX_TIMESTAMP();

    WHILE counter < max_records DO
        SET brand = ELT(FLOOR(1 + RAND() * 4), 'Nike', 'Adidas', 'Puma', 'Reebok');
        SET color = ELT(FLOOR(1 + RAND() * 4), 'Red', 'Blue', 'Black', 'White');
        SET size = FLOOR(5 + RAND() * 8);
        SET price = FLOOR(20 + RAND() * 81);
        SET stock = FLOOR(5 + RAND() * 46);

        BEGIN
            DECLARE CONTINUE HANDLER FOR 1062 BEGIN END;
            INSERT INTO shoes (brand, color, size, price, stock_quantity)
            VALUES (brand, color, size, price, stock);
            SET counter = counter + 1;
        END;
    END WHILE;
END$$
DELIMITER ;

-- Stored procedure to populate the accessories table
DELIMITER $$
CREATE PROCEDURE PopulateAccessories()
BEGIN
    DECLARE counter INT DEFAULT 0;
    DECLARE max_records INT DEFAULT 50;
    DECLARE type ENUM('Belt', 'Watch', 'Sunglasses', 'Wallet');
    DECLARE brand ENUM('Fossil', 'Casio', 'Ray-Ban', 'Levi');
    DECLARE color ENUM('Red', 'Blue', 'Black', 'White', 'Brown');
    DECLARE price INT;
    DECLARE stock INT;

    SET SESSION rand_seed1 = UNIX_TIMESTAMP();

    WHILE counter < max_records DO
        SET type = ELT(FLOOR(1 + RAND() * 4), 'Belt', 'Watch', 'Sunglasses', 'Wallet');
        SET brand = ELT(FLOOR(1 + RAND() * 4), 'Fossil', 'Casio', 'Ray-Ban', 'Levi');
        SET color = ELT(FLOOR(1 + RAND() * 5), 'Red', 'Blue', 'Black', 'White', 'Brown');
        SET price = FLOOR(5 + RAND() * 146);
        SET stock = FLOOR(5 + RAND() * 46);

        BEGIN
            DECLARE CONTINUE HANDLER FOR 1062 BEGIN END;
            INSERT INTO accessories (type, brand, color, price, stock_quantity)
            VALUES (type, brand, color, price, stock);
            SET counter = counter + 1;
        END;
    END WHILE;
END$$
DELIMITER ;

-- Call the stored procedures to populate each table
CALL PopulateTShirts();
CALL PopulateHats();
CALL PopulateShoes();
CALL PopulateAccessories();
