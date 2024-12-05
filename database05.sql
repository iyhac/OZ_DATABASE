CREATE TABLE user(
	id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(45) NOT NULL,
    password VARCHAR(45) NOT NULL,
    create_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO users(username, password)
VALUES
('user1', 'password1'),
('user2', 'password2'),
('user3', 'password3'),
('user4', 'password4'),
('user5', 'password5'),
('user6', 'password6'),
('user7', 'password7'),
('user8', 'password8'),
('user9', 'password9'),
('user10', 'password10'),

CREATE TABLE inventory_changes(
	id INT AUTO_INCREMENT PRIMARY KEY,
	product_id INT NOT NULL,
	change_type VARCHAR(45) NOT NULL,
	quantity INT NOT NULL,
);

INSERT INTO inventory_changes(product_id, chanhe_type, quantity)
(1, '입고', 50),
(2, '출고', 20),
(3, '입고', 150),
(4, '입고', 50),
(5, '입고', 30),
(6, '입고', 40),
(7, '출고', 70),
(8, '출고', 10),
(9, '입고', 80),
(10, '출고', 60),

