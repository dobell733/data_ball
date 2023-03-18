# Citation for the following code:
# Date: 3/18/23
# Adapted from:
# https://canvas.oregonstate.edu/courses/1901738/pages/exploration-developing-in-flask?module_item_id=22733738 

from flask import Blueprint, Flask, render_template, json, redirect, request
from app import mysql

update_player_spg_routes = Blueprint('update_player_spg_routes', __name__)

@update_player_spg_routes.route('/edit_player_stat/<string:stats_per_game_id>', methods=["GET"])
def get_player_info_by_id(stats_per_game_id):
    # # read Player_Stats_Per_Game info
    if request.method == 'GET':
        # mySQL query to grab all the stats in Player_Stats_Per_Game
        query = "SELECT * FROM Player_Stats_Per_Game WHERE player_stats_per_game_id=%s"
        cursor = mysql.connection.cursor()
        cursor.execute(query, (stats_per_game_id,))
        selected_player_data = cursor.fetchall()

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
                
        return render_template("edit_pspg.j2", selected_player_data=selected_player_data, player_data=player_data, game_data=game_data)