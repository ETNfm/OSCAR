CREATE DATABASE `oscar` IF NOT EXISTS;

CREATE TABLE `shows` IF NOT EXISTS(
  `id` unsigned bigint NOT NULL AUTO_INCREMENT,
  `user_id` unsigned bigint NOT NULL,
  `name` varchar(100) NOT NULL,
  `description` varchar(255) NOT NULL,
  `channel` unsigned int NOT NULL,
  `show_day` varchar(10) NOT NULL,
  `show_time` time NOT NULL,
  `length` unsigned int NOT NULL,
  `active` tinyint(1) unsigned NOT NULL DEFAULT '1',
  `frequency` varchar(3) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `channel` (`channel`),
  KEY `frequency (`frequency`),
  KEY `show_day (`show_day`),
  KEY `show_time` (`show_time`),
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `users` (
  `id` unsigned NOT NULL AUTO_INCREMENT,
  `username` varchar(255) NOT NULL,
  `passwd` varchar(255) NOT NULL,
  `display_name` varchar(255) NOT NULL,
  `email` char(130) NOT NULL,
  `resident` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `username` (`username`),
  KEY `frequency` (`frequency`),
  KEY `active` (`active`) 
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
