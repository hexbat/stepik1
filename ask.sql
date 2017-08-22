create database ask;
CREATE USER 'ask'@'%' IDENTIFIED BY 'askpassword';
GRANT ALL PRIVILEGES ON ask.* TO 'ask'@'%' WITH GRANT OPTION;
FLUSH PRIVILEGES;