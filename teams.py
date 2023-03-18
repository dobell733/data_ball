# Citation for the following code:
# Date: 3/18/23
# Adapted from:
# https://canvas.oregonstate.edu/courses/1901738/pages/exploration-developing-in-flask?module_item_id=22733738 

from flask import Blueprint, Flask, render_template, json, redirect, request
from app import mysql

teams_routes = Blueprint('teams', __name__)

@teams_routes.route('/teams', methods=["POST", "GET"])
def teams():
    # read Teams info
    if request.method == 'GET':
        # mySQL query to grab all the stats in Teams
        query = "SELECT * FROM Teams"
        cursor = mysql.connection.cursor()
        cursor.execute(query)
        teams_data = cursor.fetchall()
            
        return render_template("teams.j2", teams_data=teams_data)
    
    # insert a Teams entry
    if request.method == 'POST':
        #activates if user presses the Add Team button
        if request.form.get("Add_Team"):
            # grab user form inputs
            team_name = request.form["team_name"]

            # add user inputs to database
            query = "INSERT INTO Teams (team_name) VALUES (%s)"
            cursor = mysql.connection.cursor()
            cursor.execute(query, (team_name,))
            mysql.connection.commit()

            # redirect back to games page
            return redirect("/teams")
        