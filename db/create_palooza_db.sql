/*

create database for paloozabot logs

*/

-- DDL (data definition language)


CREATE TABLE Message (
    Message_time TIMESTAMP,
    User_id VARCHAR(32),
    Channel_name VARCHAR(32),
    Channel_id INTEGER,
    Message TEXT,
    Mentions TEXT[],
    Emojis TEXT[],
    PRIMARY KEY (Message_time, User_id)
);


CREATE TABLE Command (
    Message_time TIMESTAMP,
    User_id VARCHAR(32),
    Command VARCHAR(32),
    PRIMARY KEY (Message_time, User_id)
);


CREATE TABLE System (
    Datetime TIMESTAMP,
    Level VARCHAR(8),
    Module TEXT,
    Context TEXT,
    Message TEXT,
    PRIMARY KEY (Datetime)
);