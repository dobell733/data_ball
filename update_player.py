from flask import Blueprint, Flask, render_template, json, redirect, request
from app import mysql

update_player_routes = Blueprint('update_player_routes', __name__)

@update_player_routes.route('/edit_player/<string:player_id>', methods=["GET"])
def get_player_info_by_id(player_id):
    # # read Player_Stats_Per_Game info
    if request.method == 'GET':
        # mySQL query to grab all the stats in Player_Stats_Per_Game
        query = "SELECT player_id, team_id, f_name, l_name, position, age, salary, CONCAT(f_name, ' ',l_name) AS name FROM Players WHERE player_id=%s"
        cursor = mysql.connection.cursor()
        cursor.execute(query, (player_id,))
        selected_player_data = cursor.fetchall()

        # mySQL query to grab the player's names and ids to use in the drop down
        query2 = "SELECT player_id, CONCAT(f_name, ' ',l_name) AS name FROM Players"
        cursor = mysql.connection.cursor()
        cursor.execute(query2)
        player_data = cursor.fetchall()

        # mySQL query to grab the game ids and dates to use in the drop down
        query3 = "SELECT team_id, team_name FROM Teams"
        cursor = mysql.connection.cursor()
        cursor.execute(query3)
        team_data = cursor.fetchall()
                
        return render_template("edit_player.j2", selected_player_data=selected_player_data, player_data=player_data, team_data=team_data)