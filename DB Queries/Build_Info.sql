# ************************************************************
# Sequel Pro SQL dump
# Version 4541
#
# http://www.sequelpro.com/
# https://github.com/sequelpro/sequelpro
#
# Host: 127.0.0.1 (MySQL 5.7.22)
# Database: jenkins_jobs
# Generation Time: 2018-07-09 07:45:02 +0000
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Dump of table Build_Info
# ------------------------------------------------------------

DROP TABLE IF EXISTS `Build_Info`;

CREATE TABLE `Build_Info` (
  `Env_ID` varchar(10) NOT NULL,
  `Build_ID` int(11) NOT NULL,
  `Build_Date` date DEFAULT NULL,
  `User_ID` varchar(30) DEFAULT NULL,
  `User_Name` varchar(50) DEFAULT NULL,
  `Build_URL` varchar(500) DEFAULT NULL,
  `Status` varchar(30) DEFAULT NULL,
  UNIQUE KEY `Build_Info_Build_ID_uindex` (`Build_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `Build_Info` WRITE;
/*!40000 ALTER TABLE `Build_Info` DISABLE KEYS */;

INSERT INTO `Build_Info` (`Env_ID`, `Build_ID`, `Build_Date`, `User_ID`, `User_Name`, `Build_URL`, `Status`)
VALUES
	('mpre-slp',6371,'2018-07-03','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6371',NULL),
	('bcre-36',6372,'2018-07-03','bh04962',' Shabnam Bhanu','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6372',NULL),
	('mdsv-03',6373,'2018-07-03','bh05030',' Rajesh Vasamsetty','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6373',NULL),
	('mcop-03',6374,'2018-07-03','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6374',NULL),
	('mcom-153',6375,'2018-07-03','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6375',NULL),
	('bcre-32',6376,'2018-07-03','bh04962',' Shabnam Bhanu','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6376',NULL),
	('bcre-37',6377,'2018-07-03','bh04962',' Shabnam Bhanu','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6377',NULL),
	('mcom-130',6378,'2018-07-03','bh06123',' Vishnu Vardhan Nayakam','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6378',NULL),
	('bcom-121',6379,'2018-07-03','bh06123',' Vishnu Vardhan Nayakam','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6379',NULL),
	('mcom-153',6380,'2018-07-03','bh04970',' Lakshma Vippala','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6380',NULL),
	('mcre-27',6381,'2018-07-03','bh04970',' Lakshma Vippala','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6381',NULL),
	('bcre-32',6382,'2018-07-03','bh04962',' Shabnam Bhanu','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6382',NULL),
	('mcre-27',6383,'2018-07-03','bh04970',' Lakshma Vippala','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6383',NULL),
	('bcre-37',6384,'2018-07-03','bh04962',' Shabnam Bhanu','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6384',NULL),
	('mcop-03',6385,'2018-07-03','bh04962',' Shabnam Bhanu','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6385',NULL),
	('MCOM-130',6386,'2018-07-03','bh06022',' Naga Nikhil Sambu','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6386',NULL),
	('bcom-131',6387,'2018-07-03','bh06126',' Rajesh Kumar Sahoo','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6387',NULL),
	('MCOM-120',6388,'2018-07-03','bh06022',' Naga Nikhil Sambu','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6388',NULL),
	('mcom-120',6389,'2018-07-03','bh06022',' Naga Nikhil Sambu','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6389',NULL),
	('bcom-131',6390,'2018-07-03','bh06126',' Rajesh Kumar Sahoo','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6390',NULL),
	('bcre-33',6391,'2018-07-03','yh05478',' Narasimha Samineni','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6391',NULL),
	('mcom-120',6392,'2018-07-03','bh06123',' Vishnu Vardhan Nayakam','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6392',NULL),
	('bdsv-02',6393,'2018-07-04','bh05030',' Rajesh Vasamsetty','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6393',NULL),
	('bcop-04',6394,'2018-07-04','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6394',NULL),
	('bcre-30',6395,'2018-07-04','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6395',NULL),
	('bcre-31',6396,'2018-07-04','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6396',NULL),
	('bcre-32',6397,'2018-07-04','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6397',NULL),
	('bcre-33',6398,'2018-07-04','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6398',NULL),
	('bcre-34',6399,'2018-07-04','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6399',NULL),
	('bcre-35',6400,'2018-07-04','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6400',NULL),
	('bcre-36',6401,'2018-07-04','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6401',NULL),
	('bcre-37',6402,'2018-07-04','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6402',NULL),
	('bcre-38',6403,'2018-07-04','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6403',NULL),
	('bpre-02',6404,'2018-07-04','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6404',NULL),
	('BCOM-121',6405,'2018-07-04','BH06419',' Rishi Kaushal','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6405',NULL),
	('bcom-121',6406,'2018-07-04','BH06419',' Rishi Kaushal','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6406',NULL),
	('mpre-slp',6407,'2018-07-04','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6407',NULL),
	('mcre-23',6408,'2018-07-04','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6408',NULL),
	('mcre-21',6409,'2018-07-04','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6409',NULL),
	('mcre-20',6410,'2018-07-04','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6410',NULL),
	('mcre-25',6411,'2018-07-04','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6411',NULL),
	('mcre-26',6412,'2018-07-04','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6412',NULL),
	('mcre-27',6413,'2018-07-04','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6413',NULL),
	('mcre-28',6414,'2018-07-04','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6414',NULL),
	('mcre-29',6415,'2018-07-04','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6415',NULL),
	('mcre-24',6416,'2018-07-04','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6416',NULL),
	('mcre-22',6417,'2018-07-04','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6417',NULL),
	('mpre-bb2',6418,'2018-07-04','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6418',NULL),
	('mpre-05',6419,'2018-07-04','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6419',NULL),
	('mpre-07',6420,'2018-07-04','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6420',NULL),
	('mcop-03',6421,'2018-07-04','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6421',NULL),
	('mcom-153',6422,'2018-07-04','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6422',NULL),
	('mdsv-03',6423,'2018-07-04','bh05030',' Rajesh Vasamsetty','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6423',NULL),
	('mcom-130',6424,'2018-07-04','BH06419',' Rishi Kaushal','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6424',NULL),
	('bcom-121',6425,'2018-07-04','BH06427',' Mohan Sai Teki','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6425',NULL),
	('bcre-37',6426,'2018-07-04','bh05030',' Rajesh Vasamsetty','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6426',NULL),
	('bcre-37',6427,'2018-07-04','bh05030',' Rajesh Vasamsetty','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6427',NULL),
	('mcom-120',6428,'2018-07-04','bh06126',' Rajesh Kumar Sahoo','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6428',NULL),
	('bcom-131',6429,'2018-07-04','bh06024',' Sundeep Bagari','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6429',NULL),
	('mpre-slp2',6430,'2018-07-04','bh04969',' Adinarayana Addanki','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6430',NULL),
	('mcom-120',6431,'2018-07-04','bh06123',' Vishnu Vardhan Nayakam','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6431',NULL),
	('bcre-38',6432,'2018-07-05','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6432',NULL),
	('bcre-30',6433,'2018-07-05','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6433',NULL),
	('bcre-32',6434,'2018-07-05','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6434',NULL),
	('bcre-36',6435,'2018-07-05','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6435',NULL),
	('bcre-34',6436,'2018-07-05','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6436',NULL),
	('bcre-35',6437,'2018-07-05','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6437',NULL),
	('bcre-31',6438,'2018-07-05','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6438',NULL),
	('bcre-37',6439,'2018-07-05','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6439',NULL),
	('bpre-02',6440,'2018-07-05','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6440',NULL),
	('bdsv-02',6441,'2018-07-05','bh05030',' Rajesh Vasamsetty','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6441',NULL),
	('bcop-04',6442,'2018-07-05','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6442',NULL),
	('bcom-121',6443,'2018-07-05','bh06419',' Rishi Kaushal','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6443',NULL),
	('bcre-34',6444,'2018-07-05','bh04962',' Shabnam Bhanu','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6444',NULL),
	('mcre-23',6445,'2018-07-05','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6445',NULL),
	('mcre-21',6446,'2018-07-05','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6446',NULL),
	('mcre-20',6447,'2018-07-05','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6447',NULL),
	('mcre-25',6448,'2018-07-05','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6448',NULL),
	('mcre-26',6449,'2018-07-05','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6449',NULL),
	('mcre-27',6450,'2018-07-05','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6450',NULL),
	('mcre-28',6451,'2018-07-05','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6451',NULL),
	('mcre-29',6452,'2018-07-05','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6452',NULL),
	('mcre-24',6453,'2018-07-05','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6453',NULL),
	('mcre-22',6454,'2018-07-05','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6454',NULL),
	('mpre-bb2',6455,'2018-07-05','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6455',NULL),
	('mpre-05',6456,'2018-07-05','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6456',NULL),
	('mpre-07',6457,'2018-07-05','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6457',NULL),
	('mpre-slp',6458,'2018-07-05','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6458',NULL),
	('mdsv-03',6459,'2018-07-05','bh05030',' Rajesh Vasamsetty','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6459',NULL),
	('mcop-03',6460,'2018-07-05','bh04972',' Madhu Kancharla','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6460',NULL),
	('mcom-130',6461,'2018-07-05','bh06419',' Rishi Kaushal','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6461',NULL),
	('mcop-03',6462,'2018-07-05','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6462',NULL),
	('mcom-153',6463,'2018-07-05','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6463',NULL),
	('mcom-153',6464,'2018-07-05','bh04970',' Lakshma Vippala','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6464',NULL),
	('bcom-121',6465,'2018-07-05','bh06419',' Rishi Kaushal','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6465',NULL),
	('mcre-23',6466,'2018-07-05','bh04970',' Lakshma Vippala','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6466',NULL),
	('bcre-36',6467,'2018-07-05','bh04972',' Madhu Kancharla','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6467',NULL),
	('mcom-120',6468,'2018-07-05','bh06126',' Rajesh Kumar Sahoo','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6468',NULL),
	('bcom-131',6469,'2018-07-05','bh06126',' Rajesh Kumar Sahoo','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6469',NULL),
	('bcom-131',6470,'2018-07-05','bh06126',' Rajesh Kumar Sahoo','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6470',NULL),
	('mcom-120',6471,'2018-07-05','bh06126',' Rajesh Kumar Sahoo','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6471',NULL),
	('mcom-120',6472,'2018-07-05','bh06126',' Rajesh Kumar Sahoo','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6472',NULL),
	('bcre-38',6473,'2018-07-06','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6473',NULL),
	('bcre-30',6474,'2018-07-06','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6474',NULL),
	('bcre-32',6475,'2018-07-06','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6475',NULL),
	('bcre-36',6476,'2018-07-06','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6476',NULL),
	('bcre-34',6477,'2018-07-06','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6477',NULL),
	('bcre-35',6478,'2018-07-06','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6478',NULL),
	('bcre-31',6479,'2018-07-06','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6479',NULL),
	('bcre-37',6480,'2018-07-06','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6480',NULL),
	('bpre-02',6481,'2018-07-06','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6481',NULL),
	('bdsv-02',6482,'2018-07-06','bh05030',' Rajesh Vasamsetty','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6482',NULL),
	('bcop-04',6483,'2018-07-06','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6483',NULL),
	('mcop-03',6484,'2018-07-06','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6484',NULL),
	('mcom-153',6485,'2018-07-06','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6485',NULL),
	('mdsv-03',6486,'2018-07-06','bh05030',' Rajesh Vasamsetty','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6486',NULL),
	('mcre-23',6487,'2018-07-06','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6487',NULL),
	('mcre-21',6488,'2018-07-06','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6488',NULL),
	('mcre-20',6489,'2018-07-06','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6489',NULL),
	('mcre-25',6490,'2018-07-06','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6490',NULL),
	('mcre-26',6491,'2018-07-06','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6491',NULL),
	('mcre-27',6492,'2018-07-06','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6492',NULL),
	('mcre-28',6493,'2018-07-06','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6493',NULL),
	('mcre-29',6494,'2018-07-06','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6494',NULL),
	('mcre-24',6495,'2018-07-06','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6495',NULL),
	('mcre-22',6496,'2018-07-06','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6496',NULL),
	('mpre-bb2',6497,'2018-07-06','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6497',NULL),
	('mpre-05',6498,'2018-07-06','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6498',NULL),
	('mpre-07',6499,'2018-07-06','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6499',NULL),
	('mpre-slp',6500,'2018-07-06','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6500',NULL),
	('mcom-153',6501,'2018-07-06','bh04970',' Lakshma Vippala','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6501',NULL),
	('mcom-130',6502,'2018-07-06','bh06021',' Madhu Reddy','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6502',NULL),
	('mcom-143',6503,'2018-07-06','bh04970',' Lakshma Vippala','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6503',NULL),
	('bcom-121',6504,'2018-07-06','bh06021',' Madhu Reddy','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6504',NULL),
	('bcre-34',6505,'2018-07-06','bh04972',' Madhu Kancharla','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6505',NULL),
	('bcre-32',6506,'2018-07-06','bh04972',' Madhu Kancharla','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6506',NULL),
	('mdsv-03',6507,'2018-07-06','bh05030',' Rajesh Vasamsetty','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6507',NULL),
	('mdsv-03',6508,'2018-07-06','bh05030',' Rajesh Vasamsetty','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6508',NULL),
	('bcre-36',6509,'2018-07-06','bh04972',' Madhu Kancharla','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6509',NULL),
	('bcre-37',6510,'2018-07-06','bh04972',' Madhu Kancharla','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6510',NULL),
	('bpre-02',6511,'2018-07-06','bh04962',' Shabnam Bhanu','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6511',NULL),
	('mcop-03',6512,'2018-07-06','bh04970',' Lakshma Vippala','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6512',NULL),
	('mcom-120',6513,'2018-07-06','bh06126',' Rajesh Kumar Sahoo','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6513',NULL),
	('bcom-131',6514,'2018-07-06','bh06126',' Rajesh Kumar Sahoo','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6514',NULL),
	('mcom-120',6515,'2018-07-06','bh06123',' Vishnu Vardhan Nayakam','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6515',NULL),
	('bdsv-02',6516,'2018-07-07','bh04971',' Thirupathi Nampelli','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6516',NULL),
	('bcre-38',6517,'2018-07-07','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6517',NULL),
	('bcre-30',6518,'2018-07-07','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6518',NULL),
	('bcre-32',6519,'2018-07-07','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6519',NULL),
	('bcre-36',6520,'2018-07-07','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6520',NULL),
	('bcre-34',6521,'2018-07-07','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6521',NULL),
	('bcre-35',6522,'2018-07-07','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6522',NULL),
	('bcre-31',6523,'2018-07-07','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6523',NULL),
	('bcre-37',6524,'2018-07-07','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6524',NULL),
	('bpre-02',6525,'2018-07-07','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6525',NULL),
	('mcre-23',6526,'2018-07-07','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6526',NULL),
	('mcre-21',6527,'2018-07-07','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6527',NULL),
	('mcre-20',6528,'2018-07-07','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6528',NULL),
	('mcre-25',6529,'2018-07-07','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6529',NULL),
	('mcre-26',6530,'2018-07-07','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6530',NULL),
	('mcre-27',6531,'2018-07-07','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6531',NULL),
	('mcre-28',6532,'2018-07-07','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6532',NULL),
	('mcre-29',6533,'2018-07-07','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6533',NULL),
	('mcre-24',6534,'2018-07-07','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6534',NULL),
	('mcre-22',6535,'2018-07-07','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6535',NULL),
	('mpre-bb2',6536,'2018-07-07','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6536',NULL),
	('mpre-05',6537,'2018-07-07','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6537',NULL),
	('mpre-07',6538,'2018-07-07','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6538',NULL),
	('mpre-slp',6539,'2018-07-07','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6539',NULL),
	('bpre-02',6540,'2018-07-07','bh04972',' Madhu Kancharla','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6540',NULL),
	('bdsv-02',6541,'2018-07-07','bh04972',' Madhu Kancharla','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6541',NULL),
	('bcom-121',6542,'2018-07-07','bh06021',' Madhu Reddy','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6542',NULL),
	('bpre-02',6543,'2018-07-07','bh04972',' Madhu Kancharla','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6543',NULL),
	('bcre-32',6544,'2018-07-07','bh04972',' Madhu Kancharla','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6544',NULL),
	('bpre-02',6545,'2018-07-07','bh04972',' Madhu Kancharla','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6545',NULL),
	('bcre-32',6546,'2018-07-07','bh04972',' Madhu Kancharla','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6546',NULL),
	('bcre-32',6547,'2018-07-07','bh04972',' Madhu Kancharla','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6547',NULL),
	('bcom-131',6548,'2018-07-07','bh06126',' Rajesh Kumar Sahoo','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6548',NULL),
	('bcom-131',6549,'2018-07-07','bh06126',' Rajesh Kumar Sahoo','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6549',NULL),
	('mcom-140',6550,'2018-07-07','bh06126',' Rajesh Kumar Sahoo','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6550',NULL),
	('mcom-140',6551,'2018-07-07','bh06126',' Rajesh Kumar Sahoo','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6551',NULL),
	('mcom-140',6552,'2018-07-07','bh06126',' Rajesh Kumar Sahoo','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6552',NULL),
	('mcom-140',6553,'2018-07-07','bh06126',' Rajesh Kumar Sahoo','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6553',NULL),
	('mcom-140',6554,'2018-07-07','bh06126',' Rajesh Kumar Sahoo','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6554',NULL),
	('mcom-140',6555,'2018-07-07','bh06126',' Rajesh Kumar Sahoo','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6555',NULL),
	('bdsv-02',6556,'2018-07-08','bh04972',' Madhu Kancharla','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6556',NULL),
	('bcop-04',6557,'2018-07-08','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6557',NULL),
	('bcre-38',6558,'2018-07-08','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6558',NULL),
	('bcre-30',6559,'2018-07-08','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6559',NULL),
	('bcre-32',6560,'2018-07-08','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6560',NULL),
	('bcre-36',6561,'2018-07-08','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6561',NULL),
	('bcre-34',6562,'2018-07-08','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6562',NULL),
	('bcre-35',6563,'2018-07-08','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6563',NULL),
	('bcre-31',6564,'2018-07-08','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6564',NULL),
	('bcre-37',6565,'2018-07-08','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6565',NULL),
	('bpre-02',6566,'2018-07-08','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6566',NULL),
	('bcom-121',6567,'2018-07-08','bh06021',' Madhu Reddy','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6567',NULL),
	('bcom-121',6568,'2018-07-08','bh06021',' Madhu Reddy','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6568',NULL),
	('bcom-131',6569,'2018-07-08','bh06123',' Vishnu Vardhan Nayakam','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6569',NULL),
	('bcre-38',6570,'2018-07-09','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6570','ABORTED'),
	('bcre-30',6571,'2018-07-09','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6571',' FAILURE'),
	('bcre-32',6572,'2018-07-09','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6572',' FAILURE'),
	('bcre-36',6573,'2018-07-09','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6573',' ABORTED'),
	('bcre-34',6574,'2018-07-09','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6574',' FAILURE'),
	('bcre-35',6575,'2018-07-09','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6575',' SUCCESS'),
	('bcre-31',6576,'2018-07-09','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6576',' FAILURE'),
	('bcre-37',6577,'2018-07-09','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6577',' FAILURE'),
	('bpre-02',6578,'2018-07-09','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6578',' SUCCESS'),
	('bdsv-02',6579,'2018-07-09','bh05030',' Rajesh Vasamsetty','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6579',' SUCCESS'),
	('bcop-04',6580,'2018-07-09','da-mcom-wdsdevops',' daMCOMwdsdevops','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6580',' SUCCESS'),
	('bcom-121',6581,'2018-07-09','bh06021',' Madhu Reddy','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6581',' SUCCESS'),
	('bcre-36',6582,'2018-07-09','bh04962',' Shabnam Bhanu','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6582',' FAILURE'),
	('bcre-36',6583,'2018-07-09','bh04962',' Shabnam Bhanu','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6583',' null'),
	('bcre-37',6584,'2018-07-09','bh04962',' Shabnam Bhanu','https://fbd-ci.devops.fds.com/jenkins/view/zeus_recycle/job/zeus_creative_recycles/6584',' FAILURE');

/*!40000 ALTER TABLE `Build_Info` ENABLE KEYS */;
UNLOCK TABLES;



/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
