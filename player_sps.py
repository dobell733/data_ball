# Citation for the following code:
# Date: 3/18/23
# Adapted from:
# https://canvas.oregonstate.edu/courses/1901738/pages/exploration-developing-in-flask?module_item_id=22733738 

from flask import Blueprint, Flask, render_template, json, redirect, request
from app import mysql

player_sps_routes = Blueprint('player_sps', __name__)

@player_sps_routes.route('/player_stats_per_season', methods=["POST", "GET"])
def player_stats_per_season():
    # read Player_Stats_Per_Season info
    if request.method == 'GET':
        # mySQL query to grab all the stats in Player_Stats_Per_Season and join player name and season year
        query = "SELECT Player_Stats_Per_Season.player_stats_per_season_id, Player_Stats_Per_Season.player_id, Player_Stats_Per_Season.season_id, CONCAT(Players.f_name, ' ', Players.l_name) AS player_name, Seasons.year, Player_Stats_Per_Season.average_minutes_per_game, Player_Stats_Per_Season.field_goal_percentage, Player_Stats_Per_Season.three_point_percentage, Player_Stats_Per_Season.two_point_percentage, Player_Stats_Per_Season.free_throw_percentage, Player_Stats_Per_Season.rebound_count, Player_Stats_Per_Season.assist_count, Player_Stats_Per_Season.steal_count, Player_Stats_Per_Season.block_count FROM Player_Stats_Per_Season INNER JOIN Players ON Player_Stats_Per_Season.player_id = Players.player_id INNER JOIN Seasons ON Player_Stats_Per_Season.season_id = Seasons.season_id"
        cursor = mysql.connection.cursor()
        cursor.execute(query)
        player_stats_data = cursor.fetchall()

        # mySQL query to grab the player's names and ids to use in the drop down
        query2 = "SELECT player_id, CONCAT(f_name, ' ',l_name) AS name FROM Players"
        cursor = mysql.connection.cursor()
        cursor.execute(query2)
        player_data = cursor.fetchall()

        # mySQL query to grab the season ids and years to use in the drop down
        query3 = "SELECT season_id, year FROM Seasons"
        cursor = mysql.connection.cursor()
        cursor.execute(query3)
        season_data = cursor.fetchall()
            
        return render_template("player_stats_per_season.j2", player_stats_data=player_stats_data, player_data=player_data, season_data=season_data)
    
    # insert a Player_Stats_Per_Season entry
    if request.method == 'POST':
        #activates if user presses the Add Player Season Stats button
        if request.form.get("Add_Player_Seasons_Stats"):
            # grab user form inputs
            player_id = request.form["player_id"]
            season_id = request.form["season_id"]
            average_minutes_per_game = request.form["minutes_per_game"]
            field_goal_percentage = request.form["field_goal_percentage"]
            three_point_percentage = request.form["three_point_percentage"]
            two_point_percentage = request.form["two_point_percentage"]
            free_throw_percentage = request.form["free_throw_percentage"]
            rebounds = request.form["rebounds"]
            assists = request.form["assists"]
            steals = request.form["steals"]
            blocks = request.form["blocks"]

            # add user inputs to database
            query = "INSERT INTO Player_Stats_Per_Season (player_id, season_id, average_minutes_per_game, field_goal_percentage, three_point_percentage, two_point_percentage, free_throw_percentage, rebound_count, assist_count, steal_count, block_count) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cursor = mysql.connection.cursor()
            cursor.execute(query, (player_id, season_id, average_minutes_per_game, field_goal_percentage, three_point_percentage, two_point_percentage, free_throw_percentage, rebounds, assists, steals, blocks))
            mysql.connection.commit()

            # redirect back to player stats per season page
            return redirect("/player_stats_per_season")
