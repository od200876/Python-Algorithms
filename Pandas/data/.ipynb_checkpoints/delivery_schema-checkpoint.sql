-- ============================================
-- SCHEMA : DELIVERYgroupNb
-- ============================================

CREATE DATABASE IF NOT EXISTS DELIVERYgroupNb
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

USE DELIVERYgroupNb;

-- Table: prod
CREATE TABLE prod (
  PID     INT(6)       NOT NULL AUTO_INCREMENT,
  PName   VARCHAR(50)  NOT NULL,
  Color   VARCHAR(20),
  Weight  INT(3),
  PRIMARY KEY (PID)
);

-- Table: fact
CREATE TABLE fact (
  FID     INT(6)       NOT NULL AUTO_INCREMENT,
  FName   VARCHAR(50)  NOT NULL,
  City    VARCHAR(20),
  PRIMARY KEY (FID)
);

-- Table: sup
CREATE TABLE sup (
  SID     INT(6)       NOT NULL AUTO_INCREMENT,
  SName   VARCHAR(50)  NOT NULL,
  Status  VARCHAR(20),
  City    VARCHAR(30),
  PRIMARY KEY (SID)
);

-- Table: deliv  (PK composite)
CREATE TABLE deliv (
  PID      INT(6)  NOT NULL,
  FID      INT(6)  NOT NULL,
  SID      INT(6)  NOT NULL,
  Quantity INT(5),
  PRIMARY KEY (PID, FID, SID),
  CONSTRAINT fk_deliv_prod FOREIGN KEY (PID) REFERENCES prod(PID),
  CONSTRAINT fk_deliv_fact FOREIGN KEY (FID) REFERENCES fact(FID),
  CONSTRAINT fk_deliv_sup  FOREIGN KEY (SID) REFERENCES sup(SID)
);
