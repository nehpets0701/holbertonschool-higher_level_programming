-- create user with database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- grants
GRANT USAGE ON *.* TO 'user_0d_2'@'localhost'
GRANT SELECT hbtn_0d_2.* TO 'user_0d_2'@'localhost'
