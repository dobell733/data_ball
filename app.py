from flask import Flask, render_template, json, redirect
from flask_mysqldb import MySQL
from flask import request
import os

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'classmysql.engr.oregonstate.edu'
app.config['MYSQL_USER'] = 'cs340_belldo'
app.config['MYSQL_PASSWORD'] = '2444' #last 4 of onid
app.config['MYSQL_DB'] = 'cs340_belldo'
app.config['MYSQL_CURSORCLASS'] = "DictCursor"


mysql = MySQL(app)


# Routes
@app.route('/')
def home():

    # render home page
    return render_template("main.j2")

@app.route('/player_stats_per_game', methods=["POST", "GET", "PUT"])
def player_spg():
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
        
    # read Player_Stats_Per_Game info
    if request.method == 'GET':
        # mySQL query to grab all the stats in Player_Stats_Per_Game
        query = "SELECT * FROM Player_Stats_Per_Game"
        cursor = mysql.connection.cursor()
        cursor.execute(query)
        player_stats_data = cursor.fetchall()

        # mySQL query to grab the player's names and ids to use in the drop down
        query2 = "SELECT player_id, CONCAT(f_name, ' ',l_name) AS name FROM Players"
        cursor = mysql.connection.cursor()
        cursor.execute(query2)
        player_data = cursor.fetchall()

        # mySQL query to grab the game ids and dats to use in the drop down
        query3 = "SELECT game_id, game_date FROM Games"
        cursor = mysql.connection.cursor()
        cursor.execute(query3)
        game_data = cursor.fetchall()
            
        return render_template("player_stats_per_game.j2", player_stats_data=player_stats_data, player_data=player_data, game_data=game_data)

    
# Listener
if __name__ == "__main__":

    app.run(port=56031, debug=True)
