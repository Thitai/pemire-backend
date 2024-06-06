PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE alembic_version (
	version_num VARCHAR(32) NOT NULL, 
	CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);
INSERT INTO alembic_version VALUES('c51408f12b7a');
CREATE TABLE admins (
	id INTEGER NOT NULL, 
	username VARCHAR, 
	password VARCHAR, 
	PRIMARY KEY (id)
);
INSERT INTO admins VALUES(1,'dev','dev123');
INSERT INTO admins VALUES(2,'stewie',X'243262243132247550746f66563146446c746a6e7a7075324e35586c654d304f554e346f2e6269416375777643324657666c7a50654a4b457a496e36');
INSERT INTO admins VALUES(3,'pemire01',X'2432622431322444736c335654315041705750596b714b526a4c6a797579424d504871343747494852326276474e77794d4d30534568436978596971');
CREATE TABLE images (
	id INTEGER NOT NULL, 
	motor_id INTEGER, 
	image_url VARCHAR, 
	PRIMARY KEY (id), 
	FOREIGN KEY(motor_id) REFERENCES motors (id)
);
INSERT INTO images VALUES(2,1,'https://scontent.fnbo1-1.fna.fbcdn.net/v/t39.30808-6/435107185_813763384106441_9029993953694419958_n.jpg?_nc_cat=104&ccb=1-7&_nc_sid=5f2048&_nc_ohc=nPRUNEoq62wAb7vymry&_nc_ht=scontent.fnbo1-1.fna&oh=00_AfAHnB1EXwIj_5cK_SeKySriU1R4tTfsNJBpNO5FzFkCGA&oe=66207AE1');
INSERT INTO images VALUES(3,1,'https://scontent.fnbo1-1.fna.fbcdn.net/v/t39.30808-6/435107185_813763384106441_9029993953694419958_n.jpg?_nc_cat=104&ccb=1-7&_nc_sid=5f2048&_nc_ohc=nPRUNEoq62wAb7vymry&_nc_ht=scontent.fnbo1-1.fna&oh=00_AfAHnB1EXwIj_5cK_SeKySriU1R4tTfsNJBpNO5FzFkCGA&oe=66207AE1');
CREATE TABLE IF NOT EXISTS "motors" (
	id INTEGER NOT NULL, 
	name VARCHAR, 
	image VARCHAR, 
	type VARCHAR, 
	description VARCHAR, 
	price INTEGER, 
	model VARCHAR NOT NULL, 
	engine_number VARCHAR, 
	mileage INTEGER NOT NULL, 
	engine_size VARCHAR, 
	fuel_type VARCHAR, 
	created_at DATETIME DEFAULT (CURRENT_TIMESTAMP), 
	PRIMARY KEY (id)
);
INSERT INTO motors VALUES(1,'Motor 1','https://i.ibb.co/282z92m/Screenshot-2024-03-08-100519.png','Subaru','Luxurious interior, powerful engine. Perfect for long trips.','900,000','Model D','1',5000,'2.5L','Electric','2024-04-12 20:42:21');
INSERT INTO motors VALUES(2,'Motor 2','https://i.ibb.co/282z92m/Screenshot-2024-03-08-100519.png','Subaru','Luxurious interior, powerful engine. Perfect for long trips.','1,500,000','Model E','2',30000,'1.8L','Hybrid','2024-04-12 20:42:21');
INSERT INTO motors VALUES(3,'Motor 3','https://i.ibb.co/282z92m/Screenshot-2024-03-08-100519.png','Subaru','Reliable and efficient. Great fuel economy. Perfect for city driving.','1,300,000','Model A','3',10000,'1.8L','Plug-in Hybrid','2024-04-12 20:42:21');
INSERT INTO motors VALUES(4,'Motor 4','https://i.ibb.co/282z92m/Screenshot-2024-03-08-100519.png','Subaru','Luxurious interior, powerful engine. Perfect for long trips.','1,300,000','Model D','4',40000,'3.0L','Petrol','2024-04-12 20:42:21');
INSERT INTO motors VALUES(5,'Motor 5','https://i.ibb.co/282z92m/Screenshot-2024-03-08-100519.png','Subaru','Reliable and efficient. Great fuel economy. Perfect for city driving.','1,500,000','Model D','5',40000,'1.8L','Plug-in Hybrid','2024-04-12 20:42:21');
COMMIT;
