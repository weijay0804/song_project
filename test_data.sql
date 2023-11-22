# ************************************************************
# Sequel Ace SQL dump
# 版本號： 20046
#
# https://sequel-ace.com/
# https://github.com/Sequel-Ace/Sequel-Ace
#
# 主機: localhost (MySQL 8.2.0)
# 數據庫: topic
# 生成時間: 2023-11-22 04:34:04 +0000
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
SET NAMES utf8mb4;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE='NO_AUTO_VALUE_ON_ZERO', SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# 轉儲表 ai_use
# ------------------------------------------------------------



# 轉儲表 creation_song
# ------------------------------------------------------------

LOCK TABLES `creation_song` WRITE;
/*!40000 ALTER TABLE `creation_song` DISABLE KEYS */;

INSERT INTO `creation_song` (`song_name`, `member_acc`, `data_name`, `time`)
VALUES
	('test','admin02','20231122121617.mp3','2023-11-22 12:16:17'),
	('test2','admin02','20231122121742.mp3','2023-11-22 12:17:43'),
	('test4','admin02','20231122121853.mp3','2023-11-22 12:18:53');

/*!40000 ALTER TABLE `creation_song` ENABLE KEYS */;
UNLOCK TABLES;


# 轉儲表 love_singer
# ------------------------------------------------------------

LOCK TABLES `love_singer` WRITE;
/*!40000 ALTER TABLE `love_singer` DISABLE KEYS */;

INSERT INTO `love_singer` (`singer`, `member_acc`)
VALUES
	('謝婷芝','admin02'),
	('鄧如芳','admin02'),
	('陳念婷','admin02'),
	('蔡怡珊','admin02'),
	('黃昱瑋','admin02');

/*!40000 ALTER TABLE `love_singer` ENABLE KEYS */;
UNLOCK TABLES;


# 轉儲表 member
# ------------------------------------------------------------

LOCK TABLES `member` WRITE;
/*!40000 ALTER TABLE `member` DISABLE KEYS */;

INSERT INTO `member` (`member_acc`, `password`, `mail`, `phone`, `isvip`)
VALUES
	('admin02','test','test@test.com','123456789','0');

/*!40000 ALTER TABLE `member` ENABLE KEYS */;
UNLOCK TABLES;

# 轉儲表 sound
# ------------------------------------------------------------

LOCK TABLES `sound` WRITE;
/*!40000 ALTER TABLE `sound` DISABLE KEYS */;

INSERT INTO `sound` (`name`, `member_acc`, `sound_name`, `data_name`, `time`)
VALUES
	('黃昱瑋','admin02','test1','20231122121617.mp3','2023-11-22 00:00:00'),
	('蔡怡珊','admin02','test1','20231122121742.mp3','2023-11-22 00:00:00'),
	('蔡怡珊','admin02','test2','20231122121853.mp3','2023-11-22 00:00:00');

/*!40000 ALTER TABLE `sound` ENABLE KEYS */;
UNLOCK TABLES;



/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
