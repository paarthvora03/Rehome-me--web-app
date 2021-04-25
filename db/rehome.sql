-- phpMyAdmin SQL Dump
-- version 4.9.3
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Apr 25, 2021 at 11:39 AM
-- Server version: 5.7.26
-- PHP Version: 7.4.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `rehome`
--

-- --------------------------------------------------------

--
-- Table structure for table `contactUs`
--

CREATE TABLE `contactUs` (
  `contactUsID` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `emailID` varchar(100) NOT NULL,
  `mobileNumber` varchar(15) NOT NULL,
  `message` text NOT NULL,
  `contactUsAddedOn` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `donate`
--

CREATE TABLE `donate` (
  `donateID` int(11) NOT NULL,
  `userID` int(11) NOT NULL,
  `donatedBy` varchar(100) NOT NULL,
  `mobileNumber` varchar(15) NOT NULL,
  `amount` double NOT NULL,
  `donatedOn` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `rehome`
--

CREATE TABLE `rehome` (
  `rehomeID` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `age` varchar(15) NOT NULL,
  `rehomeAddedOn` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `takeCare`
--

CREATE TABLE `takeCare` (
  `takeCareID` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `emailID` varchar(100) NOT NULL,
  `mobileNumber` varchar(15) NOT NULL,
  `numberOfDays` int(11) NOT NULL,
  `reason` text NOT NULL,
  `takeCareAddedOn` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `userID` int(11) NOT NULL,
  `fullName` varchar(100) NOT NULL,
  `emailID` varchar(100) NOT NULL,
  `mobileNumber` varchar(15) NOT NULL,
  `password` varchar(200) NOT NULL,
  `userAddedOn` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `contactUs`
--
ALTER TABLE `contactUs`
  ADD PRIMARY KEY (`contactUsID`);

--
-- Indexes for table `donate`
--
ALTER TABLE `donate`
  ADD PRIMARY KEY (`donateID`);

--
-- Indexes for table `rehome`
--
ALTER TABLE `rehome`
  ADD PRIMARY KEY (`rehomeID`);

--
-- Indexes for table `takeCare`
--
ALTER TABLE `takeCare`
  ADD PRIMARY KEY (`takeCareID`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`userID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `contactUs`
--
ALTER TABLE `contactUs`
  MODIFY `contactUsID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `donate`
--
ALTER TABLE `donate`
  MODIFY `donateID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `rehome`
--
ALTER TABLE `rehome`
  MODIFY `rehomeID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `takeCare`
--
ALTER TABLE `takeCare`
  MODIFY `takeCareID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `userID` int(11) NOT NULL AUTO_INCREMENT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
