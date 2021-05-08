CREATE TABLE `ion_image`.`Patients` (
  `patient_id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NULL,
  `last_name` VARCHAR(45) NULL,
  `birthday` DATE NULL,
  PRIMARY KEY (`patient_id`),
  UNIQUE INDEX `patient_id_UNIQUE` (`patient_id` ASC));

CREATE TABLE `ion_image`.`Images` (
  `image_id` INT NOT NULL AUTO_INCREMENT,
  `patient_id` INT NULL,
  `time_taken` DATE NULL,
  `image_url` VARCHAR(2048) NULL,
  PRIMARY KEY (`image_id`),
  UNIQUE INDEX `image_id_UNIQUE` (`image_id` ASC));


INSERT INTO `ion_image`.`Patients` (`patient_id`, `first_name`, `last_name`, `birthday`) VALUES ('1', 'Jim', 'Jones', '1960-10-01');
INSERT INTO `ion_image`.`Patients` (`patient_id`, `first_name`, `last_name`, `birthday`) VALUES ('2', 'Winston', 'Rogers', '1970-04-04');
INSERT INTO `ion_image`.`Patients` (`patient_id`, `first_name`, `last_name`, `birthday`) VALUES ('3', 'Diane', 'Simmons', '1980-08-01');

INSERT INTO `ion_image`.`Images` (`image_id`, `patient_id`, `time_taken`) VALUES ('1', '1', '2021-02-01');
INSERT INTO `ion_image`.`Images` (`image_id`, `patient_id`, `time_taken`) VALUES ('2', '2', '2020-06-15');
INSERT INTO `ion_image`.`Images` (`image_id`, `patient_id`, `time_taken`) VALUES ('3', '3', '2020-03-14');
INSERT INTO `ion_image`.`Images` (`image_id`, `patient_id`, `time_taken`) VALUES ('4', '1', '2021-03-10');

UPDATE `ion_image`.`Images` SET `image_url` = 'https://hekangjia.s3.us-east-2.amazonaws.com/ion_image/3.jpg' WHERE (`image_id` = '3');
UPDATE `ion_image`.`Images` SET `image_url` = 'https://hekangjia.s3.us-east-2.amazonaws.com/ion_image/4.jpg' WHERE (`image_id` = '4');
UPDATE `ion_image`.`Images` SET `image_url` = 'https://hekangjia.s3.us-east-2.amazonaws.com/ion_image/2.jpg' WHERE (`image_id` = '2');
UPDATE `ion_image`.`Images` SET `image_url` = 'https://hekangjia.s3.us-east-2.amazonaws.com/ion_image/1.jpg' WHERE (`image_id` = '1');
