/*
SQLyog Community v13.1.5  (64 bit)
MySQL - 5.6.12-log : Database - evengara
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`evengara` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `evengara`;

/*Table structure for table `category` */

DROP TABLE IF EXISTS `category`;

CREATE TABLE `category` (
  `cat_id` int(11) NOT NULL AUTO_INCREMENT,
  `category` varchar(250) NOT NULL,
  PRIMARY KEY (`cat_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

/*Data for the table `category` */

insert  into `category`(`cat_id`,`category`) values 
(1,'Biriyani');

/*Table structure for table `chat` */

DROP TABLE IF EXISTS `chat`;

CREATE TABLE `chat` (
  `chatid` int(11) NOT NULL AUTO_INCREMENT,
  `senderid` int(11) NOT NULL,
  `reciverid` int(11) NOT NULL,
  `message` varchar(2500) NOT NULL,
  `date` date NOT NULL,
  `time` time NOT NULL,
  `type` varchar(20) NOT NULL,
  PRIMARY KEY (`chatid`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4;

/*Data for the table `chat` */

insert  into `chat`(`chatid`,`senderid`,`reciverid`,`message`,`date`,`time`,`type`) values 
(1,2,1,'hhhi','2021-09-11','00:00:00','shop'),
(2,2,1,'hai','2021-09-11','00:00:00','shop'),
(3,2,1,'aa','2021-09-11','12:30:29','shop'),
(4,2,1,'aa','2021-09-11','12:35:24','shop'),
(5,2,1,'gg','2021-09-11','12:36:36','shop'),
(6,2,1,'hi','2021-09-11','12:39:01','shop');

/*Table structure for table `customer` */

DROP TABLE IF EXISTS `customer`;

CREATE TABLE `customer` (
  `customerid` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `place` varchar(250) NOT NULL,
  `post` varchar(250) NOT NULL,
  `pin` int(11) NOT NULL,
  `contact` bigint(20) NOT NULL,
  `email` varchar(250) NOT NULL,
  `loginid` int(11) NOT NULL,
  PRIMARY KEY (`customerid`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

/*Data for the table `customer` */

insert  into `customer`(`customerid`,`name`,`place`,`post`,`pin`,`contact`,`email`,`loginid`) values 
(1,'Ashiq','Pottikkall','Othukkungal',12345,1234,'ashiq@gmail.com',3);

/*Table structure for table `deliveryboy` */

DROP TABLE IF EXISTS `deliveryboy`;

CREATE TABLE `deliveryboy` (
  `boyid` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(250) NOT NULL,
  `image` varchar(250) NOT NULL,
  `age` int(11) NOT NULL,
  `place` varchar(250) NOT NULL,
  `post` varchar(250) NOT NULL,
  `pin` int(11) NOT NULL,
  `contact` bigint(20) NOT NULL,
  `email` varchar(250) NOT NULL,
  `loginid` int(11) NOT NULL,
  PRIMARY KEY (`boyid`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

/*Data for the table `deliveryboy` */

insert  into `deliveryboy`(`boyid`,`name`,`image`,`age`,`place`,`post`,`pin`,`contact`,`email`,`loginid`) values 
(1,'Jafar','/static/imgs/deliveryboy/download (1).jfif',20,'Iringallur ','Iringallur',676304,9605882981,'jafariringallur@gmail.com',5);

/*Table structure for table `location` */

DROP TABLE IF EXISTS `location`;

CREATE TABLE `location` (
  `locid` int(11) NOT NULL AUTO_INCREMENT,
  `latitude` float NOT NULL,
  `longitude` float NOT NULL,
  `location` varchar(250) NOT NULL,
  `date` date NOT NULL,
  `time` time NOT NULL,
  `orderid` int(11) NOT NULL,
  PRIMARY KEY (`locid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

/*Data for the table `location` */

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `loginid` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(250) NOT NULL,
  `password` int(11) NOT NULL,
  `usertype` varchar(10) NOT NULL,
  PRIMARY KEY (`loginid`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4;

/*Data for the table `login` */

insert  into `login`(`loginid`,`username`,`password`,`usertype`) values 
(1,'admin',1234,'admin'),
(2,'rolex@gmail.com',1233,'shop'),
(3,'ashiq@gmail.com',1234,'customer'),
(4,'liyana@gmail.com',1111,'shop'),
(5,'jafariringallur@gmail.com',2147483647,'pending');

/*Table structure for table `notification` */

DROP TABLE IF EXISTS `notification`;

CREATE TABLE `notification` (
  `notificationid` int(11) NOT NULL AUTO_INCREMENT,
  `notification` varchar(2500) NOT NULL,
  `date` date NOT NULL,
  PRIMARY KEY (`notificationid`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

/*Data for the table `notification` */

insert  into `notification`(`notificationid`,`notification`,`date`) values 
(1,'hi','2021-09-12'),
(2,'aaa','2021-09-12');

/*Table structure for table `offer` */

DROP TABLE IF EXISTS `offer`;

CREATE TABLE `offer` (
  `offerid` int(11) NOT NULL AUTO_INCREMENT,
  `productid` int(11) NOT NULL,
  `offername` varchar(250) NOT NULL,
  `description` varchar(2500) NOT NULL,
  `startdate` date NOT NULL,
  `enddate` date NOT NULL,
  `shopid` int(11) DEFAULT NULL,
  PRIMARY KEY (`offerid`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

/*Data for the table `offer` */

insert  into `offer`(`offerid`,`productid`,`offername`,`description`,`startdate`,`enddate`,`shopid`) values 
(2,3,'Onam','aa','2021-09-01','2021-09-25',2);

/*Table structure for table `ordermain` */

DROP TABLE IF EXISTS `ordermain`;

CREATE TABLE `ordermain` (
  `ordermainid` int(11) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `status` varchar(25) NOT NULL,
  `total` int(11) NOT NULL,
  `userid` int(11) NOT NULL,
  PRIMARY KEY (`ordermainid`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

/*Data for the table `ordermain` */

insert  into `ordermain`(`ordermainid`,`date`,`status`,`total`,`userid`) values 
(1,'2021-09-11','pending',170,3);

/*Table structure for table `ordersub` */

DROP TABLE IF EXISTS `ordersub`;

CREATE TABLE `ordersub` (
  `ordersubid` int(11) NOT NULL AUTO_INCREMENT,
  `ordermainid` int(11) NOT NULL,
  `productid` int(11) NOT NULL,
  `quantity` int(11) NOT NULL,
  `shopid` int(11) DEFAULT NULL,
  PRIMARY KEY (`ordersubid`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;

/*Data for the table `ordersub` */

insert  into `ordersub`(`ordersubid`,`ordermainid`,`productid`,`quantity`,`shopid`) values 
(1,1,2,1,2),
(2,1,3,1,2),
(3,1,3,1,4);

/*Table structure for table `products` */

DROP TABLE IF EXISTS `products`;

CREATE TABLE `products` (
  `prdid` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `image` varchar(255) NOT NULL,
  `description` varchar(2500) NOT NULL,
  `madedate` date NOT NULL,
  `expdate` date NOT NULL,
  `price` int(11) NOT NULL,
  `shopid` int(11) NOT NULL,
  `categoryid` int(11) NOT NULL,
  PRIMARY KEY (`prdid`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;

/*Data for the table `products` */

insert  into `products`(`prdid`,`name`,`image`,`description`,`madedate`,`expdate`,`price`,`shopid`,`categoryid`) values 
(2,'Biriyani','/static/imgs/products/download.jfif','Full','2021-09-11','2021-09-11',160,2,1),
(3,'Beef Biriyani','/static/imgs/products/download.jfif','Half','2021-09-11','2021-09-11',140,2,1);

/*Table structure for table `review` */

DROP TABLE IF EXISTS `review`;

CREATE TABLE `review` (
  `reviewid` int(11) NOT NULL AUTO_INCREMENT,
  `review` varchar(2500) NOT NULL,
  `rating` int(11) NOT NULL,
  `userid` int(11) NOT NULL,
  `date` date NOT NULL,
  `type` varchar(20) DEFAULT NULL,
  `id` int(11) DEFAULT NULL,
  PRIMARY KEY (`reviewid`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

/*Data for the table `review` */

insert  into `review`(`reviewid`,`review`,`rating`,`userid`,`date`,`type`,`id`) values 
(1,'Good Services',4,3,'2021-09-11','shop',1),
(2,'good',5,3,'2021-09-12','shop',2);

/*Table structure for table `shop` */

DROP TABLE IF EXISTS `shop`;

CREATE TABLE `shop` (
  `shopid` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `address` varchar(255) NOT NULL,
  `contact` bigint(20) NOT NULL,
  `email` varchar(250) NOT NULL,
  `loginid` int(11) NOT NULL,
  PRIMARY KEY (`shopid`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;

/*Data for the table `shop` */

insert  into `shop`(`shopid`,`name`,`address`,`contact`,`email`,`loginid`) values 
(1,'Rolex','Bustand Vengara',1234567890,'rolex@gmail.com',2),
(3,'Liyana Textails','Al Nakheel Mall',1111,'liyana@gmail.com',4);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
