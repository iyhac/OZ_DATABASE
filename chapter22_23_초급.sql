-- (1) `customers` 테이블에 새 고객을 추가하세요.
  INSERT INTO customers (name, address, ...) VALUES ('John Doe', '123 Main St', ...);

-- (2) products 테이블에 새 제품을 추가하세요.
  INSERT INTO products (name, price, ...) VALUES ('Toy Car', 19.99, ...);

-- (3) employees 테이블에 새 직원을 추가하세요.
  INSERT INTO employees (firstName, lastName, ...) VALUES ('Alice', 'Johnson', ...);

-- (4) offices 테이블에 새 사무실을 추가하세요.
  INSERT INTO offices (city, phone, ...) VALUES ('San Francisco', '123-456-7890', ...);

-- (5) orders 테이블에 새 주문을 추가하세요.
  INSERT INTO orders (orderDate, customerID, ...) VALUES ('2023-01-01', 1, ...);

-- (6) orderdetails 테이블에 주문 상세 정보를 추가하세요.
  INSERT INTO orderdetails (orderID, productID, quantityOrdered, priceEach) VALUES (1, 1, 2, 20.00);

-- (7) payments 테이블에 지불 정보를 추가하세요.
  INSERT INTO payments (customerID, amount, paymentDate) VALUES (1, 200.00, '2023-01-01');

-- (8) productlines 테이블에 제품 라인을 추가하세요.
  INSERT INTO productlines (productLine, textDescription) VALUES ('Classic Cars', 'Various classic cars models');

-- (9) customers 테이블에 다른 지역의 고객을 추가하세요.
  INSERT INTO customers (name, address, city, ...) VALUES ('Jane Smith', '456 Elm St', 'New York', ...);

-- (10) products 테이블에 다른 카테고리의 제품을 추가하세요.
  INSERT INTO products (name, price, productLine, ...) VALUES ('Vintage Train', 34.99, 'Trains', ...);
