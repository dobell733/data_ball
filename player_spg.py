from flask import Blueprint, Flask, render_template, json, redirect, request
from app import mysql

player_spg_routes = Blueprint('player_spg_routes', __name__)

@player_spg_routes.route('/player_stats_per_game', methods=["POST", "GET"])
def player_stats_per_game():
    # read Player_Stats_Per_Game info
    if request.method == 'GET':
        # mySQL query to grab all the stats in Player_Stats_Per_Game and join player name and game date
        query = "SELECT Player_Stats_Per_Game.player_stats_per_game_id, Player_Stats_Per_Game.player_id, Player_Stats_Per_Game.game_id, CONCAT(Players.f_name, ' ', Players.l_name) AS player_name, Games.game_date, Player_Stats_Per_Game.minutes_per_game, Player_Stats_Per_Game.field_goal_percentage, Player_Stats_Per_Game.three_point_percentage, Player_Stats_Per_Game.two_point_percentage, Player_Stats_Per_Game.free_throw_percentage, Player_Stats_Per_Game.rebound_count, Player_Stats_Per_Game.assist_count, Player_Stats_Per_Game.steal_count, Player_Stats_Per_Game.block_count, Player_Stats_Per_Game.win FROM Player_Stats_Per_Game INNER JOIN Players ON Player_Stats_Per_Game.player_id = Players.player_id INNER JOIN Games ON Player_Stats_Per_Game.game_id = Games.game_id"
        cursor = mysql.connection.cursor()
        cursor.execute(query)
        player_stats_data = cursor.fetchall()

        # mySQL query to grab the player's names and ids to use in the drop down
        query2 = "SELECT player_id, CONCAT(f_name, ' ',l_name) AS name FROM Players"
        cursor = mysql.connection.cursor()
        cursor.execute(query2)
        player_data = cursor.fetchall()

        # mySQL query to grab the game ids and dates to use in the drop down
        query3 = "SELECT game_id, game_date FROM Games"
        cursor = mysql.connection.cursor()
        cursor.execute(query3)
        game_data = cursor.fetchall()
            
        return render_template("player_stats_per_game.j2", player_stats_data=player_stats_data, player_data=player_data, game_data=game_data)
    
    # insert a Player_Stats_Per_Game entry
    if request.method == 'POST':
        #activates if user presses the Add Player Stats button
        if request.form.get("Add_Player_Stats"):
            # grab user form inputs
            player_id = request.form["player_id"]
            game_id = request.form["game_id"]
            minutes_per_game = request.form["minutes_per_game"]
            field_goal_percentage = request.form["field_goal_percentage"]
            three_point_percentage = request.form["three_point_percentage"]
            two_point_percentage = request.form["two_point_percentage"]
            free_throw_percentage = request.form["free_throw_percentage"]
            rebounds = request.form["rebounds"]
            assists = request.form["assists"]
            steals = request.form["steals"]
            blocks = request.form["blocks"]
            win = request.form["win"]

            # add user inputs to database
            query = "INSERT INTO Player_Stats_Per_Game (player_id, game_id, minutes_per_game, field_goal_percentage, three_point_percentage, two_point_percentage, free_throw_percentage, rebound_count, assist_count, steal_count, block_count, win) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cursor = mysql.connection.cursor()
            cursor.execute(query, (player_id, game_id, minutes_per_game, field_goal_percentage, three_point_percentage, two_point_percentage, free_throw_percentage, rebounds, assists, steals, blocks, win))
            mysql.connection.commit()

            # redirect back to player stats per game page
            return redirect("/player_stats_per_game")
        
        #activates if user presses the Update Player Stats button
        if request.form.get("Update_Player_Stats"):
            # grab user form inputs
            player_id = request.form["player_id"]
            game_id = request.form["game_id"]
            minutes_per_game = request.form["minutes_per_game"]
            field_goal_percentage = request.form["field_goal_percentage"]
            three_point_percentage = request.form["three_point_percentage"]
            two_point_percentage = request.form["two_point_percentage"]
            free_throw_percentage = request.form["free_throw_percentage"]
            rebounds = request.form["rebounds"]
            assists = request.form["assists"]
            steals = request.form["steals"]
            blocks = request.form["blocks"]
            win = request.form["win"]

            # update selected entry in database
            query = "UPDATE Player_Stats_Per_Game SET player_id=%s, game_id=%s, minutes_per_game=%s, field_goal_percentage=%s, three_point_percentage=%s, two_point_percentage=%s, free_throw_percentage=%s, rebound_count=%s, assist_count=%s, steal_count=%s, block_count=%s, win=%s WHERE player_id=%s AND game_id=%s"
            cursor = mysql.connection.cursor()
            cursor.execute(query, (player_id, game_id, minutes_per_game, field_goal_percentage, three_point_percentage, two_point_percentage, free_throw_percentage, rebounds, assists, steals, blocks, win, player_id, game_id))
            mysql.connection.commit()

            # redirect back to player stats per game page
            return redirect("/player_stats_per_game")
    
@player_spg_routes.route("/delete_player_stat/<string:player_stats_per_game_id>")
def delete_pspg(player_stats_per_game_id):
    query = "DELETE FROM Player_Stats_Per_Game WHERE player_stats_per_game_id = '%s'" % (player_stats_per_game_id)
    cursor = mysql.connection.cursor()
    cursor.execute(query)
    mysql.connection.commit()

    return redirect('/player_stats_per_game')
