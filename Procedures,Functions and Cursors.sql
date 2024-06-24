USE amazon;

DELIMITER //

CREATE PROCEDURE add_product(IN pname VARCHAR(50), IN price DECIMAL(10, 2), IN stock INT)
BEGIN
  INSERT INTO products (pname, price, stock) VALUES (pname, price, stock);
END//

DELIMITER ;

DELIMITER //

CREATE PROCEDURE get_product(IN pid INT)
BEGIN
  SELECT * FROM products WHERE pid = pid;
END//

DELIMITER ;

DELIMITER //

CREATE FUNCTION get_total_price(pid INT) RETURNS DECIMAL(10, 2)
BEGIN
  DECLARE total_price DECIMAL(10, 2);
  SELECT price INTO total_price FROM products WHERE pid = pid;
  RETURN total_price;
END//

DELIMITER ;

DELIMITER //

CREATE FUNCTION get_customer_name(cid INT) RETURNS VARCHAR(50)
BEGIN
  DECLARE customer_name VARCHAR(50);
  SELECT cname INTO customer_name FROM customers WHERE cid = cid;
  RETURN customer_name;
END//

DELIMITER ;

DELIMITER //

CREATE PROCEDURE get_orders()
BEGIN
  DECLARE done BOOLEAN DEFAULT FALSE;
  DECLARE oid INT;
  DECLARE pid INT;
  DECLARE cid INT;
  DECLARE order_date DATE;
  DECLARE cur CURSOR FOR SELECT * FROM orders;
  DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

  OPEN cur;

  read_loop: LOOP
    FETCH cur INTO oid, pid, cid, order_date;
    IF done THEN
      LEAVE read_loop;
    END IF;
    -- process the row here
    SELECT oid, pid, cid, order_date;
  END LOOP;

  CLOSE cur;
END//

DELIMITER ;

-- Add a new product
CALL add_product('New Product', 19.99, 10);

-- Get the product with pid = 1
CALL get_product(1);

-- Get the total price of the product with pid = 1
SELECT get_total_price(1);

-- Get the customer name with cid = 1
SELECT get_customer_name(1);

-- Get all orders
CALL get_orders();