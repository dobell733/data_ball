-- Group Number: 75
-- Group Members: Dominic Bell and Muhammad Ali Rawjee

SET FOREIGN_KEY_CHECKS = 0;
SET AUTOCOMMIT = 0;

-- Creates an entity table named Seasons
CREATE or REPLACE TABLE Seasons (
    season_id int NOT NULL AUTO_INCREMENT,
    year year(4) NOT NULL,
    PRIMARY KEY (season_id)
);

-- Insert Data into Seasons
INSERT INTO Seasons (year)
VALUES ('2010'),
    ('2011'),
    ('2012'),
    ('2014');

-- Creates an entity table named Teams

CREATE or REPLACE TABLE Teams (
    team_id int NOT NULL AUTO_INCREMENT,
    team_name varchar(50),
    PRIMARY KEY (team_id)
);

-- Insert Data into Teams
INSERT INTO Teams (team_name)
VALUES ('Miami Heat'),
    ('Brooklyn Nets'),
    ('Golden State Warriors'),
    ('OKC');


-- Creates an entity table named Games
CREATE or REPLACE TABLE Games (
    game_id int NOT NULL AUTO_INCREMENT,
    home_team_id int NOT NULL,
    away_team_id int NOT NULL,
    game_date date NOT NULL,
    FOREIGN KEY (home_team_id) REFERENCES Teams(team_id) ON DELETE CASCADE,
    FOREIGN KEY (away_team_id) REFERENCES Teams(team_id) ON DELETE CASCADE,
    PRIMARY KEY (game_id)
);

-- Insert Data into Games

INSERT INTO Games (home_team_id, away_team_id, game_date)
VALUES (1, 2, '2021-02-01'),
    (2, 1, '2021-03-03'),
    (3, 4, '2021-03-04'),
    (4, 3, '2022-04-04');

-- Creates an entity table named Players
CREATE or REPLACE TABLE Players (
    player_id int NOT NULL AUTO_INCREMENT,
    team_id int NULL,
    f_name varchar(100) NOT NULL,
    l_name varchar(100) NOT NULL,
    position varchar(50) NOT NULL,
    age int not NULL,
    salary int not NULL,
    PRIMARY KEY (player_id),
    FOREIGN KEY (team_id) REFERENCES Teams(team_id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Insert Data into Players

INSERT INTO Players (team_id, f_name, l_name, position, age, salary)
VALUES (1, 'Luka', 'Doncic', 'Shooting Guard', 23, 12000000),
    (2, 'Lebron', 'James', 'Power Forward', 28, 50000000),
    (3, 'Kevin', 'Durant', 'Point Guard', 23, 40000000),
    (4, 'Giannis', 'Antetokounmpo', 'Center', 23, 100000000);

-- Creates an intersection table named Player_Stats_Per_Games
CREATE or REPLACE TABLE Player_Stats_Per_Game (
    player_stats_per_game_id int NOT NULL AUTO_INCREMENT,
    player_id int NOT NULL,
    game_id int NOT NULL,
    minutes_per_game DECIMAL(19,2) NOT NULL,
    field_goal_percentage DECIMAL(19,2) NOT NULL,
    three_point_percentage DECIMAL(19,2) NOT NULL,
    two_point_percentage DECIMAL(19,2) NOT NULL,
    free_throw_percentage DECIMAL(19,2) NOT NULL,
    rebound_count int NOT NULL,
    assist_count int NOT NULL,
    steal_count int NOT NULL,
    block_count int NOT NULL,
    win boolean NOT NULL,
    FOREIGN KEY (player_id) REFERENCES Players(player_id) ON DELETE CASCADE,
    FOREIGN KEY (game_id) REFERENCES Games(game_id) ON DELETE CASCADE,
    PRIMARY KEY (player_stats_per_game_id)
);

-- Insert Data into Player_Stats_Per_Game
INSERT INTO Player_Stats_Per_Game (player_id, game_id, minutes_per_game, field_goal_percentage, 
            three_point_percentage, two_point_percentage, free_throw_percentage, rebound_count, assist_count, 
            steal_count, block_count, win)
VALUES (1, 1, 40, 0.45, 0.54, 0.74, 0.64, 0.65, 17, 6, 0, 1),
        (2, 2, 50, 0.44, 0.44, 0.34, 0.56, 0.32, 10, 5, 6, 1),
        (3, 3, 60, 0.43, 0.94, 0.24, 0.62, 0.2, 12, 3, 9, 0),
        (4, 4, 70, 0.42, 0.4, 0.84, 0.97, 0.9, 23, 2, 0, 0);

-- Creates an intersection table named Player_Stats_Per_Games
CREATE or REPLACE TABLE Player_Stats_Per_Season (
    player_stats_per_season_id int NOT NULL AUTO_INCREMENT,
    player_id int NOT NULL,
    season_id int NOT NULL,
    average_minutes_per_game DECIMAL(19,2) NOT NULL,
    field_goal_percentage DECIMAL(19,2) NOT NULL,
    three_point_percentage DECIMAL(19,2) NOT NULL,
    two_point_percentage DECIMAL(19,2) NOT NULL,
    free_throw_percentage DECIMAL(19,2) NOT NULL,
    rebound_count int NOT NULL,
    assist_count int NOT NULL,
    steal_count int NOT NULL,
    block_count int NOT NULL,
    FOREIGN KEY (player_id) REFERENCES Players(player_id) ON DELETE CASCADE,
    FOREIGN KEY (season_id) REFERENCES Seasons(season_id) ON DELETE CASCADE,
    PRIMARY KEY (player_stats_per_season_id)
);

-- Insert Data into Player_Stats_Per_Season
INSERT INTO Player_Stats_Per_Season (player_id, season_id, average_minutes_per_game, 
                                    field_goal_percentage, three_point_percentage, two_point_percentage, 
                                    free_throw_percentage, rebound_count, assist_count, steal_count, block_count)
VALUES (1, 1, 500, 0.55, 0.54, 0.64, 0.9, 0.7, 170, 60, 56), 
        (2, 1, 550, 0.5, 0.14, 0.84, 0.7, 0.75, 170, 70, 57),
        (3, 1, 570, 0.45, 0.94, 0.24, 0.4, 0.75, 170, 80, 75),
        (4, 1, 600, 0.65, 0.74, 0.89, 0.84, 0.75, 170, 600, 86);

-- Creates an intersection table named Team_Stats_Per_Season
CREATE or REPLACE TABLE Team_Stats_Per_Season (
    team_stats_per_season_id int NOT NULL AUTO_INCREMENT,
    team_id int NOT NULL,
    season_id int NOT NULL,
    rank int NOT NULL,
    win_count int NOT NULL,
    loss_count int NOT NULL,
    FOREIGN KEY (team_id) REFERENCES Teams(team_id) ON DELETE CASCADE,
    FOREIGN KEY (season_id) REFERENCES Seasons(season_id) ON DELETE CASCADE,
    PRIMARY KEY (team_stats_per_season_id)
);

-- Insert Data intp Team_Stats_Per_Season
INSERT INTO Team_Stats_Per_Season (team_id, season_id, rank, win_count, loss_count)
VALUES (1, 1, 1, 45, 2),
        (2, 1, 2, 40, 7),
        (3, 1, 3, 35, 12),
        (4, 1, 4, 30, 17);

-- Display all tables
SELECT * from Seasons;
SELECT * from Teams;
SELECT * from Games;
SELECT * from Players;
SELECT * from Player_Stats_Per_Game;
SELECT * from Player_Stats_Per_Season;
SELECT * from Team_Stats_Per_Season;

SET FOREIGN_KEY_CHECKS = 1;
COMMIT;