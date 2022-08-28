GO
CREATE DATABASE WorldOfPython;

GO
USE WorldOfPython;

GO
--First we create classes and races tables 
CREATE TABLE HERO_CLASSES(
HERO_CLASS nvarchar(60) PRIMARY KEY
)

CREATE TABLE HERO_RACES(
HERO_RACE nvarchar(60) PRIMARY KEY,
HERO_RACE_START_HP smallint,
HERO_RACE_START_MANA smallint,
HERO_RACE_MAX_HP  smallint,
HERO_RACE_MAX_MANA smallint,
)

GO
CREATE TABLE HEROS(
	HERO_ID int IDENTITY PRIMARY KEY,
	HERO_NAME nvarchar(60),
	HERO_CLASS nvarchar(60),
	HERO_RACE nvarchar(60),
	HERO_HP smallint,
	HERO_MANA smallint,
	HERO_LEVEL tinyint,
	CONSTRAINT FK_HERO_CLASS FOREIGN KEY(HERO_CLASS) REFERENCES HERO_CLASSES(HERO_CLASS),
	CONSTRAINT FK_HERO_RACES FOREIGN KEY (HERO_RACE) REFERENCES HERO_RACES(HERO_RACE)
)

GO
CREATE TABLE ABILITIES(
ABILITY_ID int IDENTITY PRIMARY KEY,
ABILITY_NAME nvarchar(60),
ABILITY_DAMAGE smallint,
ABILITY_MANA_COST smallint,
)


GO
CREATE TABLE HERO_ABILITIES(
HERO_ID int,
ABILITY_ID int,
CONSTRAINT PK_HEROES_ABILITY PRIMARY KEY (HERO_ID, ABILITY_ID),
CONSTRAINT FK_HERO_HEROES FOREIGN KEY (HERO_ID) REFERENCES Heros (HERO_ID),
CONSTRAINT FK_ABILITY_ABILITIES FOREIGN KEY (ABILITY_ID) REFERENCES ABILITIES (ABILITY_ID)
)

GO
CREATE TABLE INVENTORY_TYPES(
INVENTORY_TYPE_ID int IDENTITY PRIMARY KEY,
INVENTORY_TYPE_NAME nvarchar(60),
INVENTORY_TYPE_CAPACITY smallint
)

GO
CREATE TABLE INVENTORIES(
INVENTORY_ID int IDENTITY PRIMARY KEY,
INVENTROY_CAPACITY tinyint,
INVENTROY_MONEY_CAPACITY decimal(19,4),
INVENTORY_TYPE int,
CONSTRAINT fk_inventory_type FOREIGN KEY(INVENTORY_TYPE) REFERENCES INVENTORY_TYPES(INVENTORY_TYPE_ID)
)

GO
CREATE TABLE HEROS_INVENTORY(
HERO_ID int NOT NULL,
INVENTORY_ID int NOT NULL,
CONSTRAINT fk_inventory_hero FOREIGN KEY (HERO_ID) REFERENCES Heros (HERO_ID),
CONSTRAINT fk_inventory_inventories FOREIGN KEY (INVENTORY_ID) REFERENCES INVENTORIES (INVENTORY_ID)
)


--we create a table for current levels to be beated
GO
CREATE TABLE LEVELS(
LEVEL_ID int IDENTITY PRIMARY KEY,
LEVEL_NAME nvarchar(60),
LEVEL_REWARD decimal(19,4)
)

GO
CREATE TABLE MONSTERS(
MONSTER_ID int IDENTITY PRIMARY KEY,
MONSTER_NAME nvarchar(60),
MONSTER_HP smallint,
MONSTER_DAMAGE smallint,
MONSTER_REWARD decimal(19,4)
)

GO
--INSERT MONSTERS
INSERT INTO MONSTERS(MONSTER_NAME, MONSTER_HP, MONSTER_DAMAGE, MONSTER_REWARD)
	VALUES
		('Fire_dragon',1000,70,3000),
		('Undead_Ghoul_Warrior',75,40,2000),
		('Undead_Ghoul_Wizzard',17,50,1500),
		('Spider',500,20,1000),
		('Beduin_Skull',300,1,5000),
		('Frost_Yeti',300,40,4000),
		('Ghoul',19,73,400),
		('Jiang-Shi',1,250,5000),
		('Lich',16,50,4000),
		('Mummy',250,25,3500),
		('Revenant',167,1,3000),
		('Skeleton',17,40,4500),
		('Vampire',50,17,3000),
		('Wight',6721,21,2000),
		('Zombie',180,40,2400),
		('12headedhydra',11,50,2500),
		('16headedhydra',4120,5,2200),
		('5headedhydra',500,1,2700),
		('8headedhydra',6,50,1500),
		('Acidicblob',58,1,2000),
		('Airelemental',150,25,1800),
		('Algaebeast',2,150,1500),
		('Archdevil',30,16,1200),
		('Archdruid',30,18,1500),
		('Archmage',9,22,950),
		('Assassin',100,2,1100),
		('Banshee',7,30,1600),
		('Barbarian',2,100,1000),
		('Barbarianchief',2,100,1200),
		('Barracuda',1806,7,850),
		('Basilisk',1670,9,900),
		('Battlerat',90,16,1100),
		('Blackdragon',2,80,850),
		('Blackknight',11,20,1050),
		('Bluedragon',25,13,800),
		('Caryatidguard',10,15,750),
		('Cavegiant',2,70,750),
		('Cavetroll',20,13,1100),
		('Celestialstag',3,70,525),
		('Centaur',16,16,600),
		('Chaoticknight',2,70,800),
		('Chimera',18,14,1100),
		('Cleric',10,9,425),
		('Cockatrice',5,12,400),
		('Crocodile',10,3,600),
		('Cyclops',60,11,700),
		('Deadlyspores',60,10,750),
		('Demondog',14,12,350),
		('Demonlord',3,50,500),
		('Diamondgolem',50,12,575),
		('Dinobeetle',5,10,500),
		('Dinolizard',3,45,500),
		('Druid',3,45,700),
		('Dungbeetle',550,3,550),
		('Dustdemon',40,13,600),
		('Earthelemental',40,7,270),
		('Electriceel',8,10,500),
		('Enchantress',40,11,600),
		('Evileye',416,4,300),
		('Executioner',12,4,400),
		('Fireant',8,10,400),
		('Firebeetle',10,11,500),
		('Fireelemental',200,3,500),
		('Firelizard',4,35,300),
		('Flesheater',4,35,400),
		('Frostgiant',5,5,400),
		('Gargantuanant',250,4,250),
		('Gargoyle',5,10,325),
		('Ghost',6,8,350),
		('Ghoul',4,12,400),
		('Giantcentipede',400,3,400),
		('Giantcrab',750,7,450),
		('Giantleech',518,8,250),
		('Giantscorpion',9,10,275),
		('Giantsloth',3,5,150),
		('Giantspider',4,30,450),
		('Giantsquid',4,30,360),
		('Gnoll',848,6,550),
		('Gnome',30,6,330),
		('Goblin',7,10,300),
		('Dragon',	30,3,375),
		('Gorgon',300,7,300),
		('Graydragon',200,7,200),
		('Greaterdemon',2,30,750),
		('Greaterdevil',351,6,200),
		('Greendragon',25,3,240),
		('Gremlin',350,4,550),
		('Griffin',7,7,600),
		('Guardianspirit',5,25,270),
		('Guardsman',517,5,500),
		('Hag',25,2,600),
		('Harpy',8,9,300),
		('Highcleric',7,22,400),
		('Hilltroll',7,22,400),
		('Hippocampus',120,8,500),
		('Hippogriff',20,2,500),
		('Invisiblething',8,20,300),
		('Killerbees',5,4,400),
		('Kirin',20,2,400),
		('Kobold',20,2,250),
		('Lamprey',252,5,325),
		('Lavabeast',7,18,350),
		('Lesserdemon',3,6,400),
		('Lesserdevil',2,7,400),
		('Lich',7,15,450),
		('Locustplague',7,15,250),
		('Mage',3,5,275),
		('Magician',22,7,150),
		('Maneatingmare',50,6,450),
		('Manticore',30,8,360),
		('Mantiswarrior',70,8,550),
		('Masterarcher',15,9,330),
		('Masterthief',14,9,300)

SELECT
	MONSTER_NAME,
	MONSTER_HP,
	MONSTER_DAMAGE,
	MONSTER_REWARD
FROM
Monsters
	ORDER BY(SELECT NULL)
OFFSET 0 ROWS FETCH NEXT 5 ROWS ONLY


SELECT MONSTER_NAME,MONSTER_HP,MONSTER_DAMAGE,MONSTER_REWARD FROM Monsters ORDER BY(SELECT NULL) OFFSET 0 ROWS FETCH NEXT 5 ROWS ONLY

GO
CREATE TABLE MONSTER_LEVELS(
LEVEL_ID int,
MONSTER_ID int
)


--we create the trigger before the test data is inserted
GO
CREATE OR ALTER TRIGGER trgHeroInserted
ON Heros
INSTEAD OF INSERT
AS
BEGIN
	--Declaring variables to hold current inserted race
	DECLARE @CurrentRaceInserted VARCHAR(60);
	SET @CurrentRaceInserted = (SELECT INSERTED.HERO_RACE FROM INSERTED);

	--get max hp and
	DECLARE @StartRaceHP smallint;
	DECLARE @StartRaceMana smallint;

	SET @StartRaceHP = (SELECT HERO_RACE_START_HP FROM HERO_RACES WHERE HERO_RACE = @CurrentRaceInserted);
	SET @StartRaceMana = (SELECT HERO_RACE_START_MANA FROM HERO_RACES WHERE HERO_RACE = @CurrentRaceInserted);

	--Execute the insert statement
	INSERT INTO Heros(HERO_NAME,HERO_CLASS,HERO_RACE,HERO_HP,HERO_MANA,HERO_LEVEL)
		(SELECT INSERTED.HERO_NAME, INSERTED.HERO_CLASS, INSERTED.HERO_RACE, @StartRaceHP, @StartRaceMana,1 FROM INSERTED);

	PRINT 'TRIGGER trgHeroInserted was fired';
END;

GO
--we create a stored proceudre to level up a hero accordingly



