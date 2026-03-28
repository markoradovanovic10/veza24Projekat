-- MySQL dump 10.13  Distrib 8.4.8, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: oop_2
-- ------------------------------------------------------
-- Server version	8.4.8

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `brand_for_rent`
--

DROP TABLE IF EXISTS `brand_for_rent`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `brand_for_rent` (
  `id` int NOT NULL AUTO_INCREMENT,
  `brand` varchar(24) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `brand_for_rent`
--

LOCK TABLES `brand_for_rent` WRITE;
/*!40000 ALTER TABLE `brand_for_rent` DISABLE KEYS */;
INSERT INTO `brand_for_rent` VALUES (1,'Audi'),(2,'BMW'),(3,'Mercedes'),(4,'Lancia');
/*!40000 ALTER TABLE `brand_for_rent` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `models_for_rent`
--

DROP TABLE IF EXISTS `models_for_rent`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `models_for_rent` (
  `id` int NOT NULL AUTO_INCREMENT,
  `brand` int NOT NULL,
  `model` varchar(24) NOT NULL,
  `year` int DEFAULT NULL,
  `rented` tinyint NOT NULL DEFAULT '0',
  `rented_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `models_for_rent_brand_for_rent_id_fk` (`brand`),
  CONSTRAINT `models_for_rent_brand_for_rent_id_fk` FOREIGN KEY (`brand`) REFERENCES `brand_for_rent` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `models_for_rent`
--

LOCK TABLES `models_for_rent` WRITE;
/*!40000 ALTER TABLE `models_for_rent` DISABLE KEYS */;
INSERT INTO `models_for_rent` VALUES (1,1,'a4',2010,1,'2026-03-29 11:00:00'),(2,1,'a5',2012,0,NULL),(3,2,'m3',2010,1,'2026-05-15 00:00:00'),(4,4,'Delta',2009,0,NULL);
/*!40000 ALTER TABLE `models_for_rent` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `rented_car` int DEFAULT NULL,
  `name` varchar(24) DEFAULT NULL,
  `last_name` varchar(24) DEFAULT NULL,
  `age` year DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_models_for_rent_id_fk` (`rented_car`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (3,1,'Marko','Radovanovic',1987),(5,NULL,'Bojana','Radovanovic',1991),(6,3,'Petar','Petrovic',2001),(7,NULL,'Nikola','Ciganovic',1994);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-03-29  0:26:47
