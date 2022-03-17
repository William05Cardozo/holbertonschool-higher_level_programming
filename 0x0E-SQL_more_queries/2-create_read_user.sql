-- This script create a new database call hbtn_0d_2
-- and new user call user_0d_2 with password
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2 . * TO 'user_0d_2'@'localhost';
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
