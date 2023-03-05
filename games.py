from flask import Blueprint, Flask, render_template, json, redirect, request  

game_routes = Blueprint('game_routes', __name__)

@game_routes.route('/games', methods=["POST", "GET"])
def games():
    # read Games info
    if request.method == 'GET':
        # mySQL query to grab all the stats in Games
        query = "SELECT * FROM Games"
        cursor = mysql.connection.cursor()
        cursor.execute(query)
        games_data = cursor.fetchall()

        # mySQL query to grab the team ids and names to use in the drop down
        query2 = "SELECT team_id, team_name FROM Teams"
        cursor = mysql.connection.cursor()
        cursor.execute(query2)
        team_data = cursor.fetchall()
            
        return render_template("games.j2", games_data=games_data, team_data=team_data)
    
    # insert a Games entry
    if request.method == 'POST':
        #activates if user presses the Add Game button
        if request.form.get("Add_Game"):
            # grab user form inputs
            home_team_id = request.form["home_team_id"]
            away_team_id = request.form["away_team_id"]
            game_date = request.form["game_date"]

            # add user inputs to database
            query = "INSERT INTO Games (home_team_id, away_team_id, game_date) VALUES (%s, %s, %s)"
            cursor = mysql.connection.cursor()
            cursor.execute(query, (home_team_id, away_team_id, game_date))
            mysql.connection.commit()

            # redirect back to games page
            return redirect("/games")

# keep this here to avoid ImportError
from app import mysql     