CREATE TABLE `cc` (
	`exchangedate` DATE NOT NULL,
	`cc` CHAR(3) NOT NULL,
	`rate` FLOAT NOT NULL,
	PRIMARY KEY (`exchangedate`, `cc`)
)
COLLATE='utf8_general_ci'
ENGINE=MyISAM
;
