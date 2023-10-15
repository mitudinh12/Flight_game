# Flight_game

Welcome to the flight game. Let's manage your CO2 budget while exploring different countries and continents. You must make strategic decisions about where to travel and manage your carbon footprint. Your goal is to take as many flights as possible. Good luck!!

**Database**
The game use country table from database flight_game from the course and create 1 additional table to save the player's record

Create extra table:

   create table player_record (
     id int not null auto_increment,
     player_name varchar(255) not null,
     co2_budget int not null default 10000,
     location varchar(255) not null,
     score int not null default 0,
     primary key (id)
     );
   

