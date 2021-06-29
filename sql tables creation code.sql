create database CrimeRecordMS;
use CrimeRecordMS;
CREATE TABLE Complainant
(
AadharCard bigint(12) unsigned,
First_Name varchar(50) not null,
Middle_Name varchar(50),
Last_Name varchar(50) not null,
Email varchar(150),
H_NO int(5) not null,
Society varchar(100) not null,
Locality varchar(100) not null,
PinCode int(6) unsigned not null,
MobileNo bigint(10) unsigned not null ,
PRIMARY KEY (AadharCard) 
);
select * from Complainant;
CREATE TABLE PoliceStation
(
       PS_ID INT(5) unsigned not null, 
       PRIMARY KEY (PS_ID),
	   Locality VARCHAR(50) not null        
);
select * from policestation;

CREATE TABLE PoliceOfficer
(
ServiceID bigint(10) unsigned,
First_Name varchar(50) not null,
Middle_Name varchar(50),
Last_Name varchar(50) not null,
Gender ENUM('F', 'M') not null,  
DOB date not null,
Email varchar(150),
H_NO int(5) not null,
Society varchar(100) not null,
Locality varchar(100) not null,
PinCode int(6) unsigned not null,
MobileNo bigint(10) unsigned not null,
PoliceStationID int unsigned ,
Foreign key (PoliceStationID) REFERENCES PoliceStation(PS_ID) 
ON DELETE set Null
ON UPDATE cascade ,
PRIMARY KEY (ServiceID)
);

CREATE TABLE CRM_Employee
(
EmployeeID bigint(10) unsigned,
First_Name varchar(50) not null,
Middle_Name varchar(50),
Last_Name varchar(50) not null,
Gender ENUM('F', 'M') not null,  
DOB date not null,
Email varchar(150),
H_NO int(5) not null,
Society varchar(100) not null,
Locality varchar(100) not null,
PinCode int(6) unsigned not null,
MobileNo bigint(10) unsigned not null,
PRIMARY KEY (EmployeeID)
);

select * from policeofficer;
-- drop table policeofficer;
-- drop table fir;
-- drop table recorded_as;

CREATE TABLE FIR
(
   	FIR_Reg_No VARCHAR(50), 
   	Date Date not null,
   	Time Time not null,
   	Place VARCHAR(50) not null,
	PoliceOfficer_ID bigint(10) unsigned,
    PoliceStation INT(5) unsigned not null,
   	IncidentDetails TEXT(1000) ,
    Primary key (FIR_Reg_No),
    FOREIGN KEY (PoliceStation) REFERENCES policestation (ps_id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (PoliceOfficer_ID) REFERENCES PoliceOfficer (ServiceID) ON DELETE set null ON UPDATE CASCADE    
);

CREATE TABLE Crime
(
	SectionNO smallint(4) unsigned,
    CrimeType varchar(200) not null,
    Primary key (SectionNO)
);
select * from crime;

CREATE TABLE NGO
(
	NGO_ID int(5) unsigned,
    NGO_Name varchar(200) not null,
    NGO_Type varchar(200),
    Address varchar(500) not null,
    PRIMARY KEY (NGO_ID)
);
select* from ngo;

CREATE TABLE Prison
(
	Prison_ID int(6) unsigned,
    Location varchar(200) not null,
    Pincode int(6) not null,
    JailerServiceID bigint(8) unsigned not null,
    JailerName varchar(200) not null,
    Primary key (Prison_ID)
);

CREATE TABLE Criminal
(
CriminalID bigint(10) unsigned,
First_Name varchar(50) not null,
Middle_Name varchar(50),
Last_Name varchar(50) not null,
Gender ENUM('F', 'M') not null,
DOB date not null,  
H_NO int(5) not null,
Society varchar(100) not null,
Locality varchar(100) not null,
PinCode int(6) unsigned not null,
MobileNo bigint(10) unsigned not null,
Nationality varchar(50) not null,
NGO_ID int(5) unsigned,
Prison_ID int(6) unsigned,
PRIMARY KEY (CriminalID),
FOREIGN KEY (NGO_ID) 
REFERENCES NGO(NGO_ID) 
ON DELETE set Null
ON UPDATE cascade,
FOREIGN KEY (Prison_ID) 
REFERENCES Prison(Prison_ID) 
ON DELETE set Null
ON UPDATE cascade
);
select* from criminal;


Create table Cases (
Case_ID BIGINT(10) unsigned NOT NULL,
ReportDate Date NOT NULL,
-- Case_Type enum("Low profile","High Profile") default "Low Profile",
Crime_Type smallint(4) unsigned,
Case_Status varchar(1000) default "Case Reported",
-- enum("Accused under judicial custody","Announcement of punishment 
-- and criminal sentenced","Appeal to higher court
-- ","Bail from judicial custody issued to accused","Bail issued to accused
-- ","Case closed","Case reported","Extent of punishment declaration","FIR 
-- Registered","Investigation held","Investigation Officer appointed
-- ","Investigation Officer not appointed","Investigation transferred to 
-- CBI","Investigation transferred to subsidiary state","Jurisdiction 
-- Dispute","Out of the court settlement 
-- ","Second trial scheduled","Sentence issued and accused sent to jail","Stay 
-- from the court issued","Third trial scheduled","Trial completed 
-- ","Trial due in 10 days","Trial due in 10 months","Trial due in 12 
-- months","Trial due in 24 months","Trial due in 40 days","Trial due in 7 days
-- ","Undergoing forensic investigation","Undergoing investigation") DEFAULT 
-- "Case reported",
Description text(200),
PRIMARY KEY (Case_ID),
FOREIGN KEY (Crime_Type) REFERENCES Crime(SectionNo) ON DELETE  SET NULL ON UPDATE CASCADE
);

-- ALTER TABLE cases MODIFY COLUMN Case_Status varchar(1000) default "Case Reported";
-- drop table case_leads;-- 
Create table Case_Leads (
Case_ID BIGINT(10) unsigned NOT NULL, 
First_Name varchar(50) NOT NULL, 
Middle_Name varchar(50),
Last_Name varchar(50) NOT NULL,
Lead_Type varchar(20) NOT NULL,
DOB Date NOT NULL,
Description text(1000) NOT NULL,
Mobile_no bigint(10) unsigned NOT NULL,
FOREIGN KEY (Case_ID) REFERENCES Cases(Case_ID) ON DELETE CASCADE ON UPDATE CASCADE,
primary key(Case_ID, First_Name , Lead_Type, Mobile_no)
);

alter table case_leads add primary key(Case_ID, First_Name (50), Lead_Type(50), Mobile_no(10));

-- drop table legal_info;
create table Legal_Info (
Case_ID  BIGINT(10) unsigned NOT NULL,
Court_ID int unsigned,
Judge_Assigned varchar(50),
Police_Officer varchar(50) NOT NULL,
Lawyer varchar(50),
FOREIGN KEY (Case_ID) REFERENCES Cases(Case_ID) ON DELETE CASCADE ON UPDATE CASCADE,
Primary key(Case_ID,Police_Officer)
);

CREATE TABLE recorded_as (
  FIR_Reg_No varchar(50),
  Case_ID bigint unsigned,
  primary key (FIR_Reg_No,Case_ID),
  FOREIGN KEY (FIR_Reg_No) REFERENCES FIR (FIR_Reg_No) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (Case_ID) REFERENCES cases (Case_ID) ON DELETE CASCADE ON UPDATE CASCADE
) ;

CREATE TABLE ministry_of_home_affairs (
  Officer_ID int,
  Officer_Name varchar(100) NOT NULL,
  PRIMARY KEY (Officer_ID)
) ;

CREATE TABLE users (
  User_ID bigint unsigned,
  Email varchar(100) NOT NULL,
  Username varchar(50) NOT NULL,
  Pass varchar(50) NOT NULL,
  Type_ enum('CRME','Police','Complainant','Admin','Investigating Body') NOT NULL,
  PRIMARY KEY (User_ID,Type_)
) ;

CREATE TABLE files (
  AadharCard bigint unsigned NOT NULL,
  FIR_Reg_No varchar(50) NOT NULL,
  PRIMARY KEY (AadharCard,FIR_Reg_No),
  FOREIGN KEY (FIR_Reg_No) REFERENCES fir (FIR_Reg_No) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (AadharCard) REFERENCES complainant (AadharCard) ON DELETE CASCADE ON UPDATE CASCADE
) ;

CREATE TABLE InvestigatingBureau(
 Team_Id int NOT NULL,
 Investigating_Officer varchar(100) NOT NULL,
 Member_1 varchar(100) NOT NULL,
 Member_2 varchar(100) NOT NULL,
 Investigates bigint(10) unsigned,
 Description varchar(100),
 PRIMARY KEY (Team_Id) ,
 FOREIGN KEY (Investigates) REFERENCES HighProfile(Case_ID)
 ON DELETE set Null
 ON UPDATE cascade
);

CREATE TABLE Investigate(
 Service_Id bigint(10) unsigned NOT NULL,
 Case_ID bigint(10) unsigned ,
 PRIMARY KEY (Service_Id,Case_ID) ,
 FOREIGN KEY (Case_ID) REFERENCES lowprofile(Case_ID) ON DELETE cascade ON UPDATE cascade,
 FOREIGN KEY (Service_ID) REFERENCES PoliceOfficer(ServiceID) ON DELETE cascade ON UPDATE cascade
);

CREATE TABLE associated(
 Case_ID bigint(10) unsigned not null,
 CriminalID bigint(10) unsigned not null,
 PRIMARY KEY (Case_ID,CriminalID) ,
 FOREIGN KEY (Case_ID) REFERENCES Cases(Case_ID) ON DELETE cascade ON UPDATE cascade,
 FOREIGN KEY (CriminalID) REFERENCES Criminal(CriminalID) ON DELETE cascade ON UPDATE cascade
);

CREATE TABLE LowProfile(
 Case_ID bigint(10) unsigned,
 No_of_victims tinyint(10) unsigned,
 PRIMARY KEY (Case_ID) ,
 FOREIGN KEY (Case_ID) REFERENCES Cases(Case_ID) ON DELETE cascade ON UPDATE cascade
);

CREATE TABLE highProfile(
 Case_ID bigint(10) unsigned,
 No_of_victims tinyint(10) unsigned,
 PRIMARY KEY (Case_ID) ,
 FOREIGN KEY (Case_ID) REFERENCES Cases(Case_ID) ON DELETE cascade ON UPDATE cascade
);
-- drop table associated;
-- select* from associated;
select* from ngo;


