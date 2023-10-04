# Flight_game
Software1 course project

**Database**
The game use country table from database flight_game from the course
1. Create extra table:
   create table player_record (
     id int not null auto_increment,
     player_name varchar(255) not null,
     co2_budget int not null default 10000,
     location varchar(255) not null,
     score int not null default 0,
     primary key (id)
     );

