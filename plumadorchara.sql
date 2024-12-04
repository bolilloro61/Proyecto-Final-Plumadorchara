-- MySQL dump 10.13  Distrib 8.0.40, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: plumadorchara
-- ------------------------------------------------------
-- Server version	8.0.40

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
-- Table structure for table `cargo`
--

DROP TABLE IF EXISTS `cargo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cargo` (
  `idCargo` int NOT NULL,
  `Descripcion` varchar(500) NOT NULL,
  `Nombre` varchar(100) NOT NULL,
  `Sueldo_Base` decimal(10,2) NOT NULL,
  `Horario_Entrada` time NOT NULL,
  `Horario_Salida` time NOT NULL,
  PRIMARY KEY (`idCargo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cargo`
--

LOCK TABLES `cargo` WRITE;
/*!40000 ALTER TABLE `cargo` DISABLE KEYS */;
INSERT INTO `cargo` VALUES (1,'Responsable de supervisión','Supervisor',30000.00,'08:00:00','17:00:00'),(2,'Encargado de desarrollo','Desarrollador',45000.00,'09:00:00','18:00:00');
/*!40000 ALTER TABLE `cargo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `compra`
--

DROP TABLE IF EXISTS `compra`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `compra` (
  `idCompra` int NOT NULL,
  `Proveedor` int NOT NULL,
  `Cantidad` decimal(10,2) NOT NULL,
  `Costo` decimal(10,2) NOT NULL,
  `Producto` int NOT NULL,
  PRIMARY KEY (`idCompra`),
  KEY `Proveedor` (`Proveedor`),
  KEY `Producto` (`Producto`),
  CONSTRAINT `compra_ibfk_1` FOREIGN KEY (`Proveedor`) REFERENCES `proveedor` (`idProveedor`),
  CONSTRAINT `compra_ibfk_2` FOREIGN KEY (`Producto`) REFERENCES `materiales` (`idMateriales`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `compra`
--

LOCK TABLES `compra` WRITE;
/*!40000 ALTER TABLE `compra` DISABLE KEYS */;
INSERT INTO `compra` VALUES (1,1,50.00,15000.00,1),(2,3,30.00,9000.00,2);
/*!40000 ALTER TABLE `compra` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `departamento`
--

DROP TABLE IF EXISTS `departamento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `departamento` (
  `idDepartamento` int NOT NULL,
  `Gerente` int DEFAULT NULL,
  `Descripcion` varchar(500) NOT NULL,
  `Nombre` varchar(100) NOT NULL,
  PRIMARY KEY (`idDepartamento`),
  KEY `Gerente_idx` (`Gerente`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `departamento`
--

LOCK TABLES `departamento` WRITE;
/*!40000 ALTER TABLE `departamento` DISABLE KEYS */;
INSERT INTO `departamento` VALUES (1,NULL,'Desarrollo de softwar','TI'),(2,2,'Recursos Humanos','RH');
/*!40000 ALTER TABLE `departamento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `distribuidores`
--

DROP TABLE IF EXISTS `distribuidores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `distribuidores` (
  `idDistribuidores` int NOT NULL,
  `Venta` int NOT NULL,
  `Fecha_desde_cliente` date NOT NULL,
  `Nombre` varchar(100) NOT NULL,
  `Num_Telefono` varchar(10) NOT NULL,
  PRIMARY KEY (`idDistribuidores`),
  KEY `Venta` (`Venta`),
  CONSTRAINT `distribuidores_ibfk_1` FOREIGN KEY (`Venta`) REFERENCES `venta` (`idVenta`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `distribuidores`
--

LOCK TABLES `distribuidores` WRITE;
/*!40000 ALTER TABLE `distribuidores` DISABLE KEYS */;
INSERT INTO `distribuidores` VALUES (1,1,'2024-11-10','Distribuidor A','5551112222'),(2,2,'2024-11-12','Distribuidor B','4641774565');
/*!40000 ALTER TABLE `distribuidores` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `empleado`
--

DROP TABLE IF EXISTS `empleado`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `empleado` (
  `idEmpleado` int NOT NULL,
  `Nombre` varchar(50) NOT NULL,
  `Apellidos` varchar(50) NOT NULL,
  `Num_telefono` varchar(12) NOT NULL,
  `Puesto` int NOT NULL,
  `Departamento` int NOT NULL,
  `Tiempo_Activo` decimal(5,2) NOT NULL,
  `Sueldo` decimal(10,2) NOT NULL,
  `Activo` tinyint(1) NOT NULL,
  PRIMARY KEY (`idEmpleado`),
  KEY `Puesto` (`Puesto`),
  KEY `Departamento` (`Departamento`),
  CONSTRAINT `empleado_ibfk_1` FOREIGN KEY (`Puesto`) REFERENCES `cargo` (`idCargo`),
  CONSTRAINT `empleado_ibfk_2` FOREIGN KEY (`Departamento`) REFERENCES `departamento` (`idDepartamento`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `empleado`
--

LOCK TABLES `empleado` WRITE;
/*!40000 ALTER TABLE `empleado` DISABLE KEYS */;
INSERT INTO `empleado` VALUES (1,'Juan','Pérez','5551234567',1,1,2.50,32000.00,1),(2,'Ana','López','5559876543',2,2,1.00,47000.00,1);
/*!40000 ALTER TABLE `empleado` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lote`
--

DROP TABLE IF EXISTS `lote`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `lote` (
  `IdLote` int NOT NULL,
  `Cantidad_Piezas` int NOT NULL,
  `Fecha_lote` date NOT NULL,
  PRIMARY KEY (`IdLote`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lote`
--

LOCK TABLES `lote` WRITE;
/*!40000 ALTER TABLE `lote` DISABLE KEYS */;
INSERT INTO `lote` VALUES (1,5000,'2024-11-01'),(2,300,'2024-11-10');
/*!40000 ALTER TABLE `lote` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `materiales`
--

DROP TABLE IF EXISTS `materiales`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `materiales` (
  `idMateriales` int NOT NULL,
  `Proveedor` int NOT NULL,
  `Existencia_almacen` int NOT NULL,
  `Necesario_lote` decimal(10,2) NOT NULL,
  `Registro_Compra` int DEFAULT NULL,
  `Nombre` varchar(50) NOT NULL,
  PRIMARY KEY (`idMateriales`),
  KEY `Proveedor` (`Proveedor`),
  KEY `Compra_idx` (`Registro_Compra`),
  CONSTRAINT `Compra` FOREIGN KEY (`Registro_Compra`) REFERENCES `compra` (`idCompra`),
  CONSTRAINT `materiales_ibfk_1` FOREIGN KEY (`Proveedor`) REFERENCES `proveedor` (`idProveedor`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `materiales`
--

LOCK TABLES `materiales` WRITE;
/*!40000 ALTER TABLE `materiales` DISABLE KEYS */;
INSERT INTO `materiales` VALUES (1,3,100,50.00,1,''),(2,1,200,30.00,2,'Plastico'),(3,4,250,15.00,1,'Resortes');
/*!40000 ALTER TABLE `materiales` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proveedor`
--

DROP TABLE IF EXISTS `proveedor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `proveedor` (
  `idProveedor` int NOT NULL,
  `Nombre` varchar(100) NOT NULL,
  `Material` int NOT NULL,
  `Telefono` varchar(10) NOT NULL,
  `Email` varchar(50) NOT NULL,
  PRIMARY KEY (`idProveedor`),
  KEY `Material_idx` (`Material`),
  CONSTRAINT `Material` FOREIGN KEY (`Material`) REFERENCES `materiales` (`idMateriales`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proveedor`
--

LOCK TABLES `proveedor` WRITE;
/*!40000 ALTER TABLE `proveedor` DISABLE KEYS */;
INSERT INTO `proveedor` VALUES (1,'Proveedor A',1,'','sfgsgs@gmail.com'),(3,'Proveedor C',1,'3456','erfghj'),(4,'Proveedor D',2,'4645664525','akjghkjnag@kak.com'),(5,'Proveedor E',3,'4561228899','asociados@proveedore.com');
/*!40000 ALTER TABLE `proveedor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `venta`
--

DROP TABLE IF EXISTS `venta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `venta` (
  `idVenta` int NOT NULL,
  `Cliente` int NOT NULL,
  `Cantidad` int NOT NULL,
  `Costo` decimal(10,2) NOT NULL,
  `Fecha_venta` date NOT NULL,
  `Lotes_vendidos` int NOT NULL,
  PRIMARY KEY (`idVenta`),
  KEY `Lotes_vendidos` (`Lotes_vendidos`),
  KEY `Cliente_idx` (`Cliente`),
  CONSTRAINT `Cliente` FOREIGN KEY (`Cliente`) REFERENCES `distribuidores` (`idDistribuidores`),
  CONSTRAINT `venta_ibfk_1` FOREIGN KEY (`Lotes_vendidos`) REFERENCES `lote` (`IdLote`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `venta`
--

LOCK TABLES `venta` WRITE;
/*!40000 ALTER TABLE `venta` DISABLE KEYS */;
INSERT INTO `venta` VALUES (1,1,100,50000.00,'2024-11-15',1),(2,2,150,75000.00,'2024-11-20',2);
/*!40000 ALTER TABLE `venta` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-12-03 21:01:31
