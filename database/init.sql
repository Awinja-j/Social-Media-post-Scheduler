CREATE USER posta_admin WITH PASSWORD 'posta_admin123';
CREATE DATABASE posta_user_db;
GRANT ALL PRIVILEGES ON DATABASE posta_user_db TO posta_admin;