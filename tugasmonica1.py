-- 1. Membuat database baru
CREATE DATABASE db_toko_online;

-- 2. Menggunakan database yang baru dibuat
USE db_toko_online;

-- 3. Memoryviewembuat tabel pelanggan dengan spesifikasi yang ditentukan
CREATE TABLE pelanggan (
    id_pelanggan INT NOT NULL AUTO_INCREMENT,
    nama_depan VARCHAR(50) NOT NULL,
    nama_belakang VARCHAR(50),
    email VARCHAR(100) NOT NULL,
    tanggal_daftar DATE,
    PRIMARY KEY (id_pelanggan),
    CONSTRAINT uq_email UNIQUE (email)
);