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
            
            # change the front end value to a value that back end can understand if team_id is set to NULL
            if team_id == "NULL":
                team_id = None

            # add user inputs to database
            query = "INSERT INTO Players (team_id, f_name, l_name, position, age, salary) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor = mysql.connection.cursor()
            cursor.execute(query, (team_id, f_name, l_name, position, age, salary))
            mysql.connection.commit()

            # redirect back to games page
            return redirect("/players")
        
        #activates if user presses the Update Player button
        if request.form.get("Update_Player"):
            # grab user form inputs
            player_id = request.form["player_id"]
            team_id = request.form["team_id"]
            first_name = request.form["f_name"]
            last_name = request.form["l_name"]
            position = request.form["position"]
            age = request.form["age"]
            salary = request.form["salary"]

            # change the front end value to a value that back end can understand if team_id is set to NULL
            if team_id == "NULL":
                team_id = None

            # update selected entry in database
            query = "UPDATE Players SET team_id=%s, f_name=%s, l_name=%s, position=%s, age=%s, salary=%s WHERE player_id=%s"
            cursor = mysql.connection.cursor()
            cursor.execute(query, (team_id, first_name, last_name, position, age, salary, player_id))
            mysql.connection.commit()

            # redirect back to players page
            return redirect("/players")
        
@players_routes.route("/delete_player/<string:player_id>")
def delete_player(player_id):
    query = "DELETE FROM Players WHERE player_id = '%s'" % (player_id)
    cursor = mysql.connection.cursor()
    cursor.execute(query)
    mysql.connection.commit()

    return redirect('/players')


from app import mysql 