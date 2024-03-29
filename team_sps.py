from flask import Blueprint, Flask, render_template, json, redirect, request
from app import mysql

team_sps_routes = Blueprint('team_sps', __name__)

@team_sps_routes.route('/team_stats_per_season', methods=["POST", "GET"])
def team_stats_per_season():
    # read Player_Stats_Per_Season info
    if request.method == 'GET':
        # mySQL query to grab all the stats in Team_Stats_Per_Season and join season year and team rank
        query = "SELECT Team_Stats_Per_Season.team_stats_per_season_id, Team_Stats_Per_Season.team_id, Team_Stats_Per_Season.season_id, Teams.team_name, Seasons.year, Team_Stats_Per_Season.team_rank, Team_Stats_Per_Season.win_count, Team_Stats_Per_Season.loss_count FROM Team_Stats_Per_Season INNER JOIN Teams ON Team_Stats_Per_Season.team_id = Teams.team_id INNER JOIN Seasons ON Team_Stats_Per_Season.season_id = Seasons.season_id"
        cursor = mysql.connection.cursor()
        cursor.execute(query)
        team_stats_data = cursor.fetchall()

        # mySQL query to grab the team's ids and names to use in the drop down
        query2 = "SELECT team_id, team_name FROM Teams"
        cursor = mysql.connection.cursor()
        cursor.execute(query2)
        team_data = cursor.fetchall()

        # mySQL query to grab the season ids and years to use in the drop down
        query3 = "SELECT season_id, year FROM Seasons"
        cursor = mysql.connection.cursor()
        cursor.execute(query3)
        season_data = cursor.fetchall()
            
        return render_template("team_stats_per_season.j2", team_stats_data=team_stats_data, team_data=team_data, season_data=season_data)
    
    # insert a Team_Stats_Per_Season entry
    if request.method == 'POST':
        #activates if user presses the Add Team Season Stats button
        if request.form.get("Add_Team_Seasons_Stats"):
            # grab user form inputs
            team_id = request.form["team_id"]
            season_id = request.form["season_id"]
            rank = request.form["rank"]
            win_count = request.form["win_count"]
            loss_count =request.form["loss_count"]

            # add user inputs to database
            query = "INSERT INTO Team_Stats_Per_Season (team_id, season_id, team_rank, win_count, loss_count) VALUES (%s, %s, %s, %s, %s)"
            cursor = mysql.connection.cursor()
            cursor.execute(query, (team_id, season_id, rank, win_count, loss_count))
            mysql.connection.commit()

            # redirect back to player stats per season page
            return redirect("/team_stats_per_season")
  