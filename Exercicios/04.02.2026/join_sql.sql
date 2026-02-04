-- MySQL dump 10.13  Distrib 8.0.45, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: loja_online
-- ------------------------------------------------------
-- Server version	5.5.5-10.4.32-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `clientes`
--

DROP TABLE IF EXISTS `clientes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `clientes` (
  `Cliente_ID` int(11) NOT NULL AUTO_INCREMENT,
  `Nome` varchar(100) DEFAULT NULL,
  `Email` varchar(100) DEFAULT NULL,
  `Cidade` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`Cliente_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clientes`
--

LOCK TABLES `clientes` WRITE;
/*!40000 ALTER TABLE `clientes` DISABLE KEYS */;
INSERT INTO `clientes` VALUES (1,'Maria Silva','maria@email.com','São Paulo'),(2,'João Santos','joao@email.com','Santo André'),(3,'Ana Costa','ana@email.com','Campinas'),(4,'Pedro Oliveira','pedro@email.com','Rio de Janeiro'),(5,'Carla Mendes','carla@email.com','Belo Horizonte'),(6,'Lucas Pereira','lucas@email.com','Curitiba'),(7,'Fernanda Rocha','fernanda@email.com','Porto Alegre'),(8,'Ricardo Lima','ricardo@email.com','Salvador'),(9,'Juliana Alves','juliana@email.com','Fortaleza'),(10,'Bruno Martins','bruno@email.com','Brasília');
/*!40000 ALTER TABLE `clientes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `itens_pedido`
--

DROP TABLE IF EXISTS `itens_pedido`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `itens_pedido` (
  `Item_ID` int(11) NOT NULL AUTO_INCREMENT,
  `Pedido_ID` int(11) DEFAULT NULL,
  `Produto_ID` int(11) DEFAULT NULL,
  `Quantidade` int(11) DEFAULT NULL,
  PRIMARY KEY (`Item_ID`),
  KEY `Pedido_ID` (`Pedido_ID`),
  KEY `Produto_ID` (`Produto_ID`),
  CONSTRAINT `itens_pedido_ibfk_1` FOREIGN KEY (`Pedido_ID`) REFERENCES `pedidos` (`Pedido_ID`),
  CONSTRAINT `itens_pedido_ibfk_2` FOREIGN KEY (`Produto_ID`) REFERENCES `produtos` (`Produto_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `itens_pedido`
--

LOCK TABLES `itens_pedido` WRITE;
/*!40000 ALTER TABLE `itens_pedido` DISABLE KEYS */;
INSERT INTO `itens_pedido` VALUES (1,1,1,1),(2,1,3,2),(3,2,2,1),(4,3,5,1),(5,4,7,2),(6,5,9,1),(7,6,4,1),(8,7,6,3),(9,8,8,2),(10,9,10,1);
/*!40000 ALTER TABLE `itens_pedido` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pedidos`
--

DROP TABLE IF EXISTS `pedidos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pedidos` (
  `Pedido_ID` int(11) NOT NULL AUTO_INCREMENT,
  `Cliente_ID` int(11) DEFAULT NULL,
  `Data_Pedido` date DEFAULT NULL,
  PRIMARY KEY (`Pedido_ID`),
  KEY `fk_pedidos_clientes` (`Cliente_ID`),
  CONSTRAINT `fk_pedidos_clientes` FOREIGN KEY (`Cliente_ID`) REFERENCES `clientes` (`Cliente_ID`),
  CONSTRAINT `pedidos_ibfk_1` FOREIGN KEY (`Cliente_ID`) REFERENCES `clientes` (`Cliente_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pedidos`
--

LOCK TABLES `pedidos` WRITE;
/*!40000 ALTER TABLE `pedidos` DISABLE KEYS */;
INSERT INTO `pedidos` VALUES (1,1,'2026-02-01'),(2,2,'2026-02-02'),(3,3,'2026-02-03'),(4,4,'2026-02-04'),(5,5,'2026-02-05'),(6,6,'2026-02-06'),(7,7,'2026-02-07'),(8,8,'2026-02-08'),(9,9,'2026-02-09'),(10,10,'2026-02-10');
/*!40000 ALTER TABLE `pedidos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `produtos`
--

DROP TABLE IF EXISTS `produtos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `produtos` (
  `Produto_ID` int(11) NOT NULL AUTO_INCREMENT,
  `Nome_Produto` varchar(100) DEFAULT NULL,
  `Preco` decimal(10,2) DEFAULT NULL,
  `Categoria` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`Produto_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `produtos`
--

LOCK TABLES `produtos` WRITE;
/*!40000 ALTER TABLE `produtos` DISABLE KEYS */;
INSERT INTO `produtos` VALUES (1,'Notebook',3500.00,'Eletrônicos'),(2,'Smartphone',2000.00,'Eletrônicos'),(3,'Cafeteira',300.00,'Eletrodomésticos'),(4,'Geladeira',2500.00,'Eletrodomésticos'),(5,'Televisão 50\"',2800.00,'Eletrônicos'),(6,'Fone de Ouvido Bluetooth',250.00,'Acessórios'),(7,'Mouse Gamer',150.00,'Acessórios'),(8,'Livro - SQL para Iniciantes',80.00,'Livros'),(9,'Tênis Esportivo',350.00,'Moda'),(10,'Relógio de Pulso',500.00,'Moda');
/*!40000 ALTER TABLE `produtos` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-02-04 11:15:28
