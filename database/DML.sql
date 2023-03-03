-- Group Number: 75
-- Group Members: Dominic Bell and Muhammad Ali Rawjee


------------------------------------------------------------------------------
-- Seasons queries --
------------------------------------------------------------------------------
-- select all seasons --
SELECT  Seasons.season_id,
        Seasons.year
FROM Seasons

-- add new season --
INSERT INTO Seasons(year)
VALUES (:year_yearInput)

------------------------------------------------------------------------------
-- Games queries --
------------------------------------------------------------------------------
-- select all games --
SELECT  Games.game_id,
        Games.home_team_id,
        Games.away_team_id,
        Games.game_date
FROM Games

-- add new game --
INSERT INTO Games(home_team_id, away_team_id, game_date)
VALUES (:home_team_id_idInput, :away_team_id_idInput, :game_date_dateInput)

------------------------------------------------------------------------------
-- Teams queries --
------------------------------------------------------------------------------
-- select all Teams --
SELECT  Teams.team_id,
        Teams.team_name
FROM Teams

-- add new team --
INSERT INTO Teams(team_name)
VALUES (:team_name_nameInput)


------------------------------------------------------------------------------
-- Players queries --
------------------------------------------------------------------------------
-- select all players --
SELECT  Players.player_id,
        Players.team_id,
        Players.f_name,
        Players.l_name,
        Players.position,
        Players.age,
        Players.salary
FROM Players

-- add new player --
INSERT INTO Players(team_id, f_name, l_name, position, age, salary)
VALUES (:team_id_idInput, 
        :f_name_nameInput, 
        :l_name_nameInput, 
        :position_textInput, 
        :age_numInput, 
        :salary_numInput)


------------------------------------------------------------------------------
-- Player_Stats_Per_Game queries --
------------------------------------------------------------------------------
-- select all Player_Stats_Per_Game --
SELECT  Player_Stats_Per_Game.player_stats_per_game_id,
        Players.player_id,
        Games.game_id,
        Player_Stats_Per_Game.minutes_per_game,
        Player_Stats_Per_Game.field_goal_percentage,
        Player_Stats_Per_Game.three_point_percentage,
        Player_Stats_Per_Game.two_point_percentage,
        Player_Stats_Per_Game.free_throw_percentage,
        Player_Stats_Per_Game.rebound_count,
        Player_Stats_Per_Game.assist_count,
        Player_Stats_Per_Game.steal_count,
        Player_Stats_Per_Game.block_count,
        Player_Stats_Per_Game.win
FROM Player_Stats_Per_Game
INNER JOIN Players ON Player_Stats_Per_Game.player_id = Players.player_id
INNER JOIN Games ON Player_Stats_Per_Game.game_id = Games.game_id

-- add new Player_Stat_Per_Game  --
INSERT INTO Player_Stats_Per_Game(player_id, game_id, minutes_per_game, field_goal_percentage, three_point_percentage, 
            two_point_percentage, free_throw_percentage, rebound_count, assist_count, steal_count,
            block_count, win)
VALUES ((SELECT player_id FROM Players WHERE (f_name = :player_fname_Input, l_name = :player_lnameInput)), 
        (SELECT game_id FROM Games WHERE (home_team_id = :home_team_idInput, away_team_id = :away_team_idInput)), 
        :minutes_per_game_numInput, 
        :field_goal_percentage_floatInput, 
        :three_point_percentage_floatInput, 
        :two_point_percentage_floatInput,
        :free_throw_percentage_floatInput,
        :rebound_count_numInput
        :assist_count_numInput,
        :steal_count_numInput,
        :block_count_numInput,
        :win_numInput)


-- update Player_Stats_Per_Game data --


UPDATE Player_Stats_Per_Game
SET player_id = (SELECT Players.player_id FROM Players WHERE (Players.f_name=:player_f_nameInput, Players.l_name=:player_l_nameInput), 
    game_id = (SELECT Games.game_id FROM Games WHERE (Games.home_team_id = :home_team_idInput, Games.away_team_id = :away_team_idInput),
    minutes_per_game = :minutes_per_game_numInput,
    field_goal_percentage = :field_goal_percentage_floatInput,
    three_point_percentage = :three_point_percentage_floatInput,
    two_point_percentage = :two_point_percentage_floatInput,
    free_throw_percentage = :free_throw_percentage_floatInput, 
    rebound_count = :rebound_count_numInput, 
    assist_count = :assist_count_numInput, 
    steal_count = :steal_count_numInput,
    block_count = :block_count_numInput, 
    win = :win_numInput

WHERE Player_Stats_Per_Game.player_stats_per_game_id = :player_stats_per_game_id_numInput;


-- Delete Player_Stats_Per_Game --


DELETE FROM Player_Stats_Per_Game 
WHERE player_id=(SELECT Players.player_id FROM Players WHERE f_name=:f_nameInput, l_name= :l_nameInput)
AND game_id = (SELECT Games.game_id FROM Games WHERE home_team_id = :home_team_idInput, away_team_id =: away_team_idInput);



------------------------------------------------------------------------------
-- Player_Stats_Per_Season queries --
------------------------------------------------------------------------------
-- select all Player_Stats_Per_Season --
SELECT  Player_Stats_Per_Season.player_stats_per_season_id,
        Players.player_id,
        Seasons.season_id,
        Player_Stats_Per_Season.average_minutes_per_game,
        Player_Stats_Per_Season.field_goal_percentage,
        Player_Stats_Per_Season.three_point_percentage,
        Player_Stats_Per_Season.two_point_percentage,
        Player_Stats_Per_Season.free_throw_percentage,
        Player_Stats_Per_Season.rebound_count,
        Player_Stats_Per_Season.assist_count,
        Player_Stats_Per_Season.steal_count,
        Player_Stats_Per_Season.block_count
FROM Player_Stats_Per_Season
INNER JOIN Players ON Player_Stats_Per_Season.player_id = Players.player_id
INNER JOIN Games ON Player_Stats_Per_Season.season_id = Seasons.season_id

-- add new Player_Stats_Per_Season  --
INSERT INTO Player_Stats_Per_Season(player_id, season_id, average_minutes_per_game, field_goal_percentage, three_point_percentage, 
            two_point_percentage, free_throw_percentage, rebound_count, assist_count, steal_count,
            block_count)
VALUES ((SELECT player_id FROM Players WHERE (f_name = :player_fname_Input, l_name = :player_lnameInput)), 
        (SELECT season_id FROM Seasons WHERE season_year = :season_yearInput), 
        :average_minutes_per_game_numInput, 
        :field_goal_percentage_floatInput, 
        :three_point_percentage_floatInput, 
        :two_point_percentage_floatInput,
        :free_throw_percentage_floatInput,
        :rebound_count_numInput
        :assist_count_numInput,
        :steal_count_numInput,
        :block_count_numInput)


-- update Player_Stats_Per_Season data --


UPDATE Player_Stats_Per_Season 
SET player_id = (SELECT Players.player_id FROM Players WHERE (Players.f_name=:player_f_nameInput, Players.l_name=:player_l_nameInput)), 
    season_id = (SELECT Seasons.season_id FROM Seasons WHERE Seasons.season_year = :season_yearInput),
    minutes_per_game = :minutes_per_game_numInput,
    field_goal_percentage = :field_goal_percentage_floatInput,
    three_point_percentage = :three_point_percentage_floatInput,
    two_point_percentage = :two_point_percentage_floatInput,
    free_throw_percentage = :free_throw_percentage_floatInput, 
    rebound_count = :rebound_count_numInput, 
    assist_count = :assist_count_numInput, 
    steal_count = :steal_count_numInput,
    block_count = :block_count_numInput, 
    win = :win_numInput

WHERE Player_Stats_Per_Season.player_stats_per_season_id = :player_stats_per_season_id_numInput;


-- Delete Player_Stats_Per_Season --


DELETE FROM Player_Stats_Per_Season 
WHERE player_id= (SELECT Players.player_id FROM Players WHERE f_name=:f_nameInput, l_name= :l_nameInput) 
AND season_id = (SELECT season.season_id FROM Seasons WHERE season_year = :season_yearInput);




------------------------------------------------------------------------------
-- Team_Stats_Per_Season queries --
------------------------------------------------------------------------------
-- select all Team_Stats_Per_Season --
SELECT  Team_Stats_Per_Season.team_stats_per_season_id,
        Teams.team_id,
        Seasons.season_id,
        Team_Stats_Per_Season.rank,
        Team_Stats_Per_Season.win_count,
        Team_Stats_Per_Season.loss_count
FROM Team_Stats_Per_Season
INNER JOIN Teams ON Team_Stats_Per_Season.team_id = Teams.team_id
INNER JOIN Seasons ON Team_Stats_Per_Season.season_id = Seasons.season_id

-- add new Team_Stats_Per_Season  --
INSERT INTO Team_Stats_Per_Season(team_id, season_id, rank, win_count, loss_count)
VALUES ((SELECT team_id FROM Teams WHERE team_name = :team_nameInput), 
        (SELECT season_id FROM Seasons WHERE season_year = :season_yearInput), 
        :rank_numInput, 
        :win_count_numInput, 
        :loss_count_numInput)


-- update Team_Stats_Per_Season data --

UPDATE Team_Stats_Per_Season 
SET team_id = (SELECT Teams.team_id FROM Teams WHERE Teams.team_name=:team_nameInput), 
    season_id = (SELECT Seasons.season_id FROM Seasons WHERE Seasons.season_year = :season_yearInput),
    rank = :rank_numInput,
    win_count = :win_count_numInput,
    loss_count = :loss_count_numInput

WHERE Team_Stats_Per_Season.team_stats_per_season_id = :team_stats_per_season_id_numInput;


-- Delete Team_Stats_Per_Season --


DELETE FROM Team_Stats_Per_Season
WHERE team_id = (SELECT Teams.team_id FROM Teams WHERE team_name = :team_nameInput)) 
AND season_id = (SELECT season.game_id FROM Seasons WHERE season_year = :season_yearInput);


------------------------------------------------------------------------------
-- Drop Down queries --
------------------------------------------------------------------------------
-- mySQL query to grab all the stats in Player_Stats_Per_Game
SELECT * FROM Player_Stats_Per_Game

-- mySQL query to grab the player's names and ids to use in the drop down
SELECT player_id, CONCAT(f_name, ' ',l_name) AS name FROM Players

-- mySQL query to grab the game ids and dates to use in the drop down
SELECT game_id, game_date FROM Games