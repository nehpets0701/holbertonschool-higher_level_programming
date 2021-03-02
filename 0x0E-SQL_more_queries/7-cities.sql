-- cities
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (id INT UNIQUE PRIMARY KEY NOT NULL AUTO_INCREMENT, FOREIGN KEY (state_id) REFERENCES states(id) INT NOT NULL, name VARCHAR(256) NOT NULL);
