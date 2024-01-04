-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 04, 2024 at 03:31 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `costume_rental`
--

-- --------------------------------------------------------

--
-- Table structure for table `costume`
--

CREATE TABLE `costume` (
  `Costume_Name` text NOT NULL,
  `Costume_Price` varchar(100) NOT NULL,
  `Costume_Quantity` varchar(100) NOT NULL,
  `Total_Cost` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `costume`
--

INSERT INTO `costume` (`Costume_Name`, `Costume_Price`, `Costume_Quantity`, `Total_Cost`) VALUES
('Fairy Costume', 'RM35', '1', ''),
('Disney Princess Costume', 'RM40', '1', ''),
('Mermaid Costume', 'RM50', '1', ''),
('Animal Costume', 'RM70', '1', ''),
('Superhero Costume', 'RM85', '1', ''),
('Sanrio costume', 'RM40', '1', '');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
