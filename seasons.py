from flask import Blueprint, Flask, render_template, json, redirect, request
from app import mysql

seasons_routes = Blueprint('seasons', __name__)

@seasons_routes.route('/seasons', methods=["POST", "GET"])
def seasons():
    # read Teams info
    if request.method == 'GET':
        # mySQL query to grab all the stats in Seasons
        query = "SELECT * FROM Seasons"
        cursor = mysql.connection.cursor()
        cursor.execute(query)
        seasons_data = cursor.fetchall()

        return render_template("seasons.j2", seasons_data=seasons_data)
    
    # insert a Seasons entry
    if request.method == 'POST':
        #activates if user presses the Add Season button
        if request.form.get("Add_Season"):
            # grab user form inputs
            year = request.form["year"]
            
            # add user inputs to database
            query = "INSERT INTO Seasons (year) VALUES (%s)"
            cursor = mysql.connection.cursor()
            cursor.execute(query, (year,))
            mysql.connection.commit()

            # redirect back to seasons page
            return redirect("/seasons")
    
from app import mysql