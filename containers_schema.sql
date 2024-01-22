DROP TABLE IF EXISTS `containerslist`;
CREATE TABLE `containerslist` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `container_name` varchar(255) NOT NULL,
  `update_status` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=159 DEFAULT CHARSET=latin1;
