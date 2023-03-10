from flask import Blueprint, Flask, render_template, json, redirect, request
from app import mysql

players_routes = Blueprint('players', __name__)

@players_routes.route('/players', methods=["POST", "GET"])
def players():
    # read Teams info
    if request.method == 'GET':
        # mySQL query to grab all the stats in Players
        query = "SELECT * FROM Players"
        cursor = mysql.connection.cursor()
        cursor.execute(query)
        players_data = cursor.fetchall()

        query2 = "SELECT team_id, team_name FROM Teams"
        cursor = mysql.connection.cursor()
        cursor.execute(query2)
        teams_data = cursor.fetchall()
 
        return render_template("players.j2", players_data=players_data, teams_data=teams_data)
    
    # insert a Teams entry
    if request.method == 'POST':
        #activates if user presses the Add Player button
        if request.form.get("Add_Player"):
            # grab user form inputs
            team_id = request.form["team_id"]
            f_name = request.form["f_name"]
            l_name = request.form["l_name"]
            position = request.form["position"]
            age = request.form["age"]
            salary = request.form["salary"]
            
            # add user inputs to database
            query = "INSERT INTO Players (team_id, f_name, l_name, position, age, salary) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor = mysql.connection.cursor()
            cursor.execute(query, (team_id, f_name, l_name, position, age, salary))
            mysql.connection.commit()

            # redirect back to games page
            return redirect("/players")
        

from app import mysql 