CREATE DATABASE IF NOT EXISTS `oscar`;
USE oscar;

CREATE TABLE `shows` (
  `id` int(32) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` int(32) unsigned NOT NULL,
  `name` varchar(100) NOT NULL,
  `description` varchar(255) NOT NULL,
  `channel` int(10) unsigned NOT NULL,
  `show_day` varchar(10) NOT NULL,
  `show_time` time NOT NULL,
  `length` int(10) unsigned NOT NULL,
  `active` tinyint(1) unsigned NOT NULL DEFAULT '1',
  `frequency` varchar(3) NOT NULL DEFAULT '0',
  `file_root` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `channel` (`channel`),
  KEY `frequency` (`frequency`),
  KEY `show_day` (`show_day`),
  KEY `show_time` (`show_time`),
  KEY `file_root` (`file_root`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `users` (
  `id` int(32) unsigned NOT NULL AUTO_INCREMENT,
  `username` varchar(128) NOT NULL,
  `passwd` varchar(4096) NOT NULL,
  `display_name` varchar(256) NOT NULL,
  `email` varchar(256) NOT NULL,
  `resident` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `username` (`username`),
  KEY `resident` (`resident`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

