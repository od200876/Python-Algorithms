-- ============================================
-- DATA : DELIVERYgroupNb
-- ============================================

USE DELIVERYgroupNb;

-- ---- prod ----
INSERT INTO prod (PID, PName, Color, Weight) VALUES
(1,  'pr1',  'red',   23),
(2,  'pr2',  'green', 25),
(3,  'pr3',  'black', 20),
(4,  'pr4',  'red',   22),
(5,  'pr5',  'red',   33),
(6,  'pr6',  'black', 21),
(7,  'pr7',  'red',   65),
(8,  'pr8',  'green', 34),
(9,  'pr9',  'black', 32),
(10, 'pr10', 'red',   32),
(11, 'pr11', 'white', 43),
(12, 'pr12', 'red',   23),
(13, 'pr13', 'green', 21),
(14, 'pr14', 'black', 45);

-- ---- fact ----
INSERT INTO fact (FID, FName, City) VALUES
(1, 'Factory1', 'Setif'),
(2, 'Factory2', 'Setif'),
(3, 'Factory3', 'Annaba'),
(4, 'Factory4', 'Annaba'),
(5, 'Factory5', 'Algiers'),
(6, 'Factory6', 'Algiers'),
(7, 'Factory7', 'Constantine'),
(8, 'Factory8', 'Oran');

-- ---- sup ----
INSERT INTO sup (SID, SName, Status, City) VALUES
(1, 'Supplier1', 'Private',     'Annaba'),
(2, 'Supplier2', 'State owned', 'Annaba'),
(3, 'Supplier3', 'Private',     'Algiers'),
(4, 'Supplier4', 'Private',     'Algiers'),
(5, 'Supplier5', 'State owned', 'Constantine'),
(6, 'Supplier6', 'Private',     'Constantine');

-- ---- deliv ----
INSERT INTO deliv (PID, FID, SID, Quantity) VALUES
(1,  1, 3, 15),
(1,  1, 5, 35),
(2,  1, 3, 50),
(2,  3, 1, 123),
(4,  3, 1, 150),
(5,  1, 3, 70),
(5,  3, 2, 220),
(5,  4, 3, 100),
(5,  6, 4, 55),
(10, 2, 1, 200),
(10, 2, 3, 80),
(10, 3, 1, 300),
(10, 4, 3, 40),
(11, 2, 1, 21),
(11, 3, 3, 400),
(13, 2, 2, 20),
(14, 2, 2, 233);
