CREATE TABLE  gifts_code( 
    email varchar(100),
	code varchar(50),
	create_time DATETIME,
	update_time DATETIME,
	status int,
	host varchar(20),
	dummy1 varchar(20),
 	dummy2 varchar(20),
 	primary key (email)
);
