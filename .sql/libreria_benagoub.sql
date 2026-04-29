-- Esegui queste query coprono diversi aspetti come SELECT, JOIN, GROUP BY, HAVING, ORDER BY, COUNT, SUM, AVG e molto altro.



-- 1. Elenco di tutti i libri
select titolo from libro; 

-- 2. Elenco di tutti gli autori
select nome, cognome from autore  ;

-- 3. Elenco di tutti gli editori
select nome from editore; 

-- 4. Selezionare il titolo e il prezzo dei libri ordinati per prezzo crescente
select titolo, prezzo from libro
order by prezzo ;

-- 5. Selezionare i libri con un prezzo superiore a 15€
select titolo, prezzo from libro 
where prezzo>15 ; 

-- 6. Contare il numero totale di libri nel database
select count(titolo) from libro; 

-- 7. Ottenere la media delle pagine dei libri
select avg(pagine) from libro;

-- 8. Trovare il libro più costoso
select titolo, prezzo from libro
order by prezzo desc limit 1 ; 

-- 9. Trovare il libro meno costoso
select titolo, prezzo from libro
order by prezzo limit 1;

-- 10. Contare il numero di autori per nazione
select count(id), nazionalita from autore 
group by nazionalita ; 

-- 11. Elenco dei libri con più di 500 pagine
select titolo, pagine from libro
where pagine>500 ;

-- 12. Elenco degli autori italiani
select * from autore 
where nazionalita = 'it' ; 

-- 13. Trovare tutti i libri pubblicati da un determinato editore (es. Mondadori)
select titolo, nome from libro, editore
where nome = 'Mondadori';

-- 14. Contare il numero di libri per ogni editore
select count(l.id) as num_lib, e.nome as nome_edit
from editore e 
join libro l on e.id = l.editore_id
group by e.id; 

-- 15. Trovare i libri con più di 400 pagine pubblicati da un determinato editore
select l.titolo as libroo, e.nome as editore , l.pagine
from libro l
join editore e on l.editore_id = e.id
where l.pagine>400 ; 

-- 16. Trovare il numero di autori che hanno scritto almeno un libro
select count(autore_id), l.id from autore_libro, libro
join libro l on autore_libro = l.id
where l.id >1 
;
-- 17. Trovare gli autori che hanno scritto più di un libro
select autore.nome, count(*) as book
from autore_libro
join autore on autore.id = autore_libro.autore_id
group by autore.nome
having book> 1 ;  

-- 18. Trovare gli autori che non hanno scritto alcun libro
select autore.nome, count(*) as book
from autore_libro
join autore on autore.id = autore_libro.autore_id
group by autore.nome
having book <1 ;

-- 19. Selezionare i libri con più di un autore
select libro.titolo, count(*) as aut
from autore_libro
join libro on libro.id = autore_libro.libro_id
group by libro.titolo
having aut > 1 ; 

-- 20. Contare il numero di libri per autore
select autore.nome, count(*)
from autore_libro
join autore on autore.id = autore_libro.autore_id
group by autore.nome; 

-- 21. Ottenere la somma totale del prezzo di tutti i libri
select sum(libro.prezzo) from libro; 

-- 22. Contare il numero di libri con un prezzo compreso tra 10 e 20 euro
select count(libro.titolo) from libro
where prezzo between 10 and 20 ;

-- 23. Trovare il prezzo medio dei libri per editore
select editore.nome, avg(libro.prezzo)
from libro 
join editore on libro.editore_id = editore.id
group by editore.nome ;

-- 24. Trovare gli autori con più libri pubblicati da editori diversi
select autore.nome, count(editore.id) as numero_editori
from autore_libro
join libro on autore_libro.libro_id = libro.id
join autore on autore_libro.autore_id = autore.id
join editore on libro.editore_id = editore.id
group by autore.id 
having count(editore.id) > 1 ; 

-- 25. Trovare i libri con il prezzo più alto per ogni editore
select max(libro.prezzo), editore.nome 
from libro , editore
group by editore.nome; 

-- 26. Ottenere i 5 libri più costosi
select libro.titolo, libro.prezzo from libro 
order by libro.prezzo desc limit 5 ; 

-- 27. Contare il numero di libri pubblicati da ciascun editore con più di 3 libri
select count(l.id) as conto, e.nome from editore as e
join libro as l on l.editore_id=e.id
group by l.editore_id 
having conto> 3
; 

-- 28. Selezionare il nome degli editori che hanno pubblicato almeno un libro con più di 500 pagine
select editore.nome, count(*)
from editore 
join libro on editore_id = libro.editore_id
where libro.pagine > 500 
group by editore.nome with rollup; 

-- 29. Trovare gli autori che hanno scritto libri pubblicati da più di un editore
select autore.nome, count(editore.id) as numero_editori
from autore_libro
join libro on autore_libro.libro_id = libro.id
join autore on autore_libro.autore_id = autore.id
join editore on libro.editore_id = editore.id
group by autore.id
having count(editore.id) > 1 ; 

 
-- 30. Contare il numero di libri per ogni autore con più di 1 libro; 
select autore.nome, count(libro_id) as conta
from autore_libro
join autore on autore.id = autore_libro.autore_id
group by autore.nome
having conta>1;





-- join delle tabelle
select e.nome, l.titolo, a.nome, a.cognome 
from autore_libro al
join libro l on al.libro_id = l.id -- associazione di chiave fk di AutoriLibri con PK libro
join autore a on al.autore_id = a.id -- associazione autore-libro -> autore
join editore e on l.editore_id = e.id -- associazione libro -> editore
join libro l on e.id = l.editore_id
;



-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: localhost    Database: tss_2022
-- ------------------------------------------------------
-- Server version	8.0.28

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
-- Table structure for table `autore`
--
use libreria;
DROP TABLE IF EXISTS `autore`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `autore` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(30) DEFAULT NULL,
  `cognome` varchar(50) DEFAULT NULL,
  `nazionalita` char(2) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `autore`
--

LOCK TABLES `autore` WRITE;
/*!40000 ALTER TABLE `autore` DISABLE KEYS */;
INSERT INTO `autore` VALUES (1,'John Ronald Reuel','Tolkien','za'),(2,'Dan','Brown','us'),(3,'Paulo','Coelho','br'),(4,'J. D.','Salinger','us'),(5,'Agatha','Christie','en'),(6,'J. K.','Rowling','en'),(7,'Tsao','Chan','cn'),(8,'E. L.','James','en'),(9,'Antoine','de Saint-Exup?ry','fr'),(10,'Charles','Dickens','en'),(11,'Miguel','de Cervantes','es'),(12,'Clive Staples','Lewis','en'),(13,'Tse-tung','Mao','cn'),(14,'Michele','Rech, Zerocalcare','it'),(15,'Andrea','Camilleri','it'),(16,'Ken','Follett','en'),(17,'Kazuo','Ishiguro','jp'),(18,'Carlo','Fruttero','it'),(19,'Franco','Lucentini','it'),(20,'Italo','Calvino','it'),(21,'Stephen','King','us'),(22,'Isabel','Allende','cl');
/*!40000 ALTER TABLE `autore` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-02-25 11:45:45

-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: localhost    Database: tss_2022
-- ------------------------------------------------------
-- Server version	8.0.28

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
-- Table structure for table `autore_libro`
--

DROP TABLE IF EXISTS `autore_libro`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `autore_libro` (
  `libro_id` int NOT NULL,
  `autore_id` int NOT NULL,
  PRIMARY KEY (`libro_id`,`autore_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `autore_libro`
--

LOCK TABLES `autore_libro` WRITE;
/*!40000 ALTER TABLE `autore_libro` DISABLE KEYS */;
INSERT INTO `autore_libro` VALUES (1,3),(2,8),(3,5),(4,11),(5,6),(6,2),(7,4),(8,12),(9,13),(10,9),(11,1),(12,7),(13,16),(14,18),(14,19),(15,1),(16,14),(17,2),(18,17),(19,15),(20,10),(21,20),(22,21);
/*!40000 ALTER TABLE `autore_libro` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-02-25 11:45:45
-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: localhost    Database: tss_2022
-- ------------------------------------------------------
-- Server version	8.0.28

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
-- Table structure for table `autore_libro`
--

DROP TABLE IF EXISTS `autore_libro`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `autore_libro` (
  `libro_id` int NOT NULL,
  `autore_id` int NOT NULL,
  PRIMARY KEY (`libro_id`,`autore_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `autore_libro`
--

LOCK TABLES `autore_libro` WRITE;
/*!40000 ALTER TABLE `autore_libro` DISABLE KEYS */;
INSERT INTO `autore_libro` VALUES (1,3),(2,8),(3,5),(4,11),(5,6),(6,2),(7,4),(8,12),(9,13),(10,9),(11,1),(12,7),(13,16),(14,18),(14,19),(15,1),(16,14),(17,2),(18,17),(19,15),(20,10),(21,20),(22,21);
/*!40000 ALTER TABLE `autore_libro` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-02-25 11:45:45
-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: localhost    Database: tss_2022
-- ------------------------------------------------------
-- Server version	8.0.28

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
-- Table structure for table `autore`
--

DROP TABLE IF EXISTS `autore`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `autore` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(30) DEFAULT NULL,
  `cognome` varchar(50) DEFAULT NULL,
  `nazionalita` char(2) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `autore`
--

LOCK TABLES `autore` WRITE;
/*!40000 ALTER TABLE `autore` DISABLE KEYS */;
INSERT INTO `autore` VALUES (1,'John Ronald Reuel','Tolkien','za'),(2,'Dan','Brown','us'),(3,'Paulo','Coelho','br'),(4,'J. D.','Salinger','us'),(5,'Agatha','Christie','en'),(6,'J. K.','Rowling','en'),(7,'Tsao','Chan','cn'),(8,'E. L.','James','en'),(9,'Antoine','de Saint-Exup?ry','fr'),(10,'Charles','Dickens','en'),(11,'Miguel','de Cervantes','es'),(12,'Clive Staples','Lewis','en'),(13,'Tse-tung','Mao','cn'),(14,'Michele','Rech, Zerocalcare','it'),(15,'Andrea','Camilleri','it'),(16,'Ken','Follett','en'),(17,'Kazuo','Ishiguro','jp'),(18,'Carlo','Fruttero','it'),(19,'Franco','Lucentini','it'),(20,'Italo','Calvino','it'),(21,'Stephen','King','us'),(22,'Isabel','Allende','cl');
/*!40000 ALTER TABLE `autore` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-02-25 11:45:45
-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: localhost    Database: tss_2022
-- ------------------------------------------------------
-- Server version	8.0.28

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
-- Table structure for table `editore`
--

DROP TABLE IF EXISTS `editore`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `editore` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(30) DEFAULT NULL,
  `contatto` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `contatto` (`contatto`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `editore`
--

LOCK TABLES `editore` WRITE;
/*!40000 ALTER TABLE `editore` DISABLE KEYS */;
INSERT INTO `editore` VALUES (1,'Mondadori','info-mondadori@gmail.com'),(3,'Einaudi','amm-einaudi@gmail.com'),(4,'Salani','salani-info@gmail.com'),(5,'Edizioni Clandestine','clandestine-info@gmail.com'),(6,'Bao Publishing','bao_editore@gmail.com'),(7,'Sellerio','amm-sellerio@gmail.com'),(8,'BUR','bur_editore@gmail.com'),(9,'Sperling & Kupfer','sperling-info@gmail.com'),(10,'Bompiani','contact-bompiani@gmail.com'),(11,'Adelphi','adelphi-info@gmail.com');
/*!40000 ALTER TABLE `editore` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-02-25 11:45:44
-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: localhost    Database: tss_2022
-- ------------------------------------------------------
-- Server version	8.0.28

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
-- Table structure for table `libro`
--

DROP TABLE IF EXISTS `libro`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `libro` (
  `id` int NOT NULL AUTO_INCREMENT,
  `titolo` varchar(100) DEFAULT NULL,
  `prezzo` decimal(6,2) DEFAULT NULL,
  `pagine` smallint DEFAULT NULL,
  `editore_id` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `libro`
--

LOCK TABLES `libro` WRITE;
/*!40000 ALTER TABLE `libro` DISABLE KEYS */;
INSERT INTO `libro` VALUES (1,'Alchimista (L\')',12.00,10,1),(2,'Cinquanta sfumature di grigio',10.20,560,1),(3,'Dieci piccoli indiani',10.20,208,1),(4,'Don Chisciotte della Mancha',20.40,NULL,3),(5,'Harry Potter e la Pietra Filosofale',8.50,302,4),(6,'Il Codice da Vinci',11.00,512,1),(7,'Il giovane Holden',10.20,251,3),(8,'Il leone, la strega e l\'armadio',7.65,182,1),(9,'Il libretto rosso',7.22,160,5),(10,'Il Piccolo Principe',4.25,95,1),(11,'Il Signore degli Anelli: La compagnia dell\'anello. Le due torri. Il ritorno del re',25.00,1255,10),(12,'Il sogno della camera rossa. Romanzo cinese del XVIII secolo',15.30,721,3),(13,'La colonna di fuoco',27.00,912,1),(14,'La donna della domenica',12.00,434,1),(15,'Lo Hobbit',9.35,417,10),(16,'Macerie prime',14.45,192,6),(17,'Origin',21.25,564,1),(18,'Quel che resta del giorno',12.00,276,3),(19,'Un mese con Montalbano',12.75,512,7),(20,'Una storia tra due citt├á',9.77,600,10),(21,'Marcovaldo',10.00,120,7),(22,'IT',25.00,550,9),(23,'gomorra',12.59,345,1);
/*!40000 ALTER TABLE `libro` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-02-25 11:45:45

-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: localhost    Database: tss_2022
-- ------------------------------------------------------
-- Server version	8.0.28

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
-- Table structure for table `editore`
--

DROP TABLE IF EXISTS `editore`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `editore` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(30) DEFAULT NULL,
  `contatto` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `contatto` (`contatto`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `editore`
--

LOCK TABLES `editore` WRITE;
/*!40000 ALTER TABLE `editore` DISABLE KEYS */;
INSERT INTO `editore` VALUES (1,'Mondadori','info-mondadori@gmail.com'),(3,'Einaudi','amm-einaudi@gmail.com'),(4,'Salani','salani-info@gmail.com'),(5,'Edizioni Clandestine','clandestine-info@gmail.com'),(6,'Bao Publishing','bao_editore@gmail.com'),(7,'Sellerio','amm-sellerio@gmail.com'),(8,'BUR','bur_editore@gmail.com'),(9,'Sperling & Kupfer','sperling-info@gmail.com'),(10,'Bompiani','contact-bompiani@gmail.com'),(11,'Adelphi','adelphi-info@gmail.com');
/*!40000 ALTER TABLE `editore` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-02-25 11:45:44

-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: localhost    Database: tss_2022
-- ------------------------------------------------------
-- Server version	8.0.28

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
-- Table structure for table `libro`
--

DROP TABLE IF EXISTS `libro`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `libro` (
  `id` int NOT NULL AUTO_INCREMENT,
  `titolo` varchar(100) DEFAULT NULL,
  `prezzo` decimal(6,2) DEFAULT NULL,
  `pagine` smallint DEFAULT NULL,
  `editore_id` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `libro`
--

LOCK TABLES `libro` WRITE;
/*!40000 ALTER TABLE `libro` DISABLE KEYS */;
INSERT INTO `libro` VALUES (1,'Alchimista (L\')',12.00,10,1),(2,'Cinquanta sfumature di grigio',10.20,560,1),(3,'Dieci piccoli indiani',10.20,208,1),(4,'Don Chisciotte della Mancha',20.40,NULL,3),(5,'Harry Potter e la Pietra Filosofale',8.50,302,4),(6,'Il Codice da Vinci',11.00,512,1),(7,'Il giovane Holden',10.20,251,3),(8,'Il leone, la strega e l\'armadio',7.65,182,1),(9,'Il libretto rosso',7.22,160,5),(10,'Il Piccolo Principe',4.25,95,1),(11,'Il Signore degli Anelli: La compagnia dell\'anello. Le due torri. Il ritorno del re',25.00,1255,10),(12,'Il sogno della camera rossa. Romanzo cinese del XVIII secolo',15.30,721,3),(13,'La colonna di fuoco',27.00,912,1),(14,'La donna della domenica',12.00,434,1),(15,'Lo Hobbit',9.35,417,10),(16,'Macerie prime',14.45,192,6),(17,'Origin',21.25,564,1),(18,'Quel che resta del giorno',12.00,276,3),(19,'Un mese con Montalbano',12.75,512,7),(20,'Una storia tra due citt├á',9.77,600,10),(21,'Marcovaldo',10.00,120,7),(22,'IT',25.00,550,9),(23,'gomorra',12.59,345,1);
/*!40000 ALTER TABLE `libro` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-02-25 11:45:45
