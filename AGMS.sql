-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               5.7.24 - MySQL Community Server (GPL)
-- Server OS:                    Win64
-- HeidiSQL Version:             9.5.0.5196
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- Dumping database structure for agms
CREATE DATABASE IF NOT EXISTS `agms` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `agms`;

-- Dumping structure for table agms.arts
CREATE TABLE IF NOT EXISTS `arts` (
  `artistname` varchar(20) DEFAULT NULL,
  `art_id` varchar(20) DEFAULT NULL,
  `price` int(10) DEFAULT NULL,
  KEY `artistname` (`artistname`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- Dumping data for table agms.arts: 3 rows
DELETE FROM `arts`;
/*!40000 ALTER TABLE `arts` DISABLE KEYS */;
INSERT INTO `arts` (`artistname`, `art_id`, `price`) VALUES
	('sach2605', '02', 2350),
	('sach2605', '03', 5500),
	('sach2605', '01', 2500);
/*!40000 ALTER TABLE `arts` ENABLE KEYS */;

-- Dumping structure for table agms.users
CREATE TABLE IF NOT EXISTS `users` (
  `name` varchar(20) DEFAULT NULL,
  `username` varchar(20) NOT NULL,
  `password` varchar(30) DEFAULT NULL,
  `email` varchar(40) DEFAULT NULL,
  `usertype` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`username`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- Dumping data for table agms.users: 1 rows
DELETE FROM `users`;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` (`name`, `username`, `password`, `email`, `usertype`) VALUES
	('Sachin Motwani', 'sach2605', 'abc123', 'sachinmmotwani@gmail.com', 'Artist');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;

-- Dumping structure for table agms.wishlist
CREATE TABLE IF NOT EXISTS `wishlist` (
  `username` varchar(20) NOT NULL,
  `art_id` varchar(20) DEFAULT NULL,
  KEY `username` (`username`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- Dumping data for table agms.wishlist: 1 rows
DELETE FROM `wishlist`;
/*!40000 ALTER TABLE `wishlist` DISABLE KEYS */;
INSERT INTO `wishlist` (`username`, `art_id`) VALUES
	('sach2605', '01');
/*!40000 ALTER TABLE `wishlist` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
