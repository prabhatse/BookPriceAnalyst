
#Create database
CREATE DATABASE IF NOT EXISTS DBBook;

#Create table book store
CREATE table Book( 
	book_id int not null AUTO_INCREMENT,
    book_isbn int not null,
    book_title varchar(200),
    unique(book_isbn),
    primary key(book_id)
    );
CREATE table Store( 
	store_id int not null AUTO_INCREMENT,
    store_name char(100) not null,
    unique(store_name),
    primary key(store_id)
    );
Create table Book_Detail(
	detail_id int not null AUTO_INCREMENT,
    book_id int not null,
    store_id int not null,
    price float not null,
    date_price datetime,
    primary key(detail_id)
    );

#Install mysql-connector-python before using python to interact
#with the database