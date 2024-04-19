FINAL YEAR PROJECT

!!!! important !!!

mySQL db:
    username = "root"
    password = "ananyo2001"
    database = "face_recognizer"
    **refer "student_table_schema.png" for creating the student table.**

CREATE TABLE `face_recognizer`.`student` (
  `Dep` VARCHAR(45) NULL,
  `course` VARCHAR(45) NULL,
  `Year` VARCHAR(45) NULL,
  `Semester` VARCHAR(45) NULL,
  `Student_id` INT NOT NULL,
  `Name` VARCHAR(45) NULL,
  `Division` VARCHAR(45) NULL,
  `Roll` VARCHAR(45) NULL,
  `Gender` VARCHAR(45) NULL,
  `Dob` VARCHAR(45) NULL,
  `Email` VARCHAR(45) NULL,
  `Phone` VARCHAR(45) NULL,
  `Address` VARCHAR(45) NULL,
  `Teacher` VARCHAR(45) NULL,
  `PhotoSample` VARCHAR(45) NULL,
  PRIMARY KEY (`Student_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

===================================== Pyrhon Dependencies =============================

Python Version - 3.9.13

OpenCv / CV2:-
pip install opencv-contrib-python

mySql Connector for Python :-
pip install mysql-connector-python

Pillow:-
pip install pillow
