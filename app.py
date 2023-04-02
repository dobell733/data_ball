from flask import Flask, render_template, json, redirect, request
from flask_mysqldb import MySQL
import os

app = Flask(__name__)

# app.config['MYSQL_HOST'] = 'sql9.freesqldatabase.com'
# app.config['MYSQL_USER'] = 'sql9609677'
# app.config['MYSQL_PASSWORD'] = 'IMTa9lULdh'
# app.config['MYSQL_DB'] = 'sql9609677'
# app.config['MYSQL_CURSORCLASS'] = "DictCursor"
DB_HOST = os.environ.get('JAWSDB_HOST')
DB_PORT = os.environ.get('JAWSDB_PORT')
DB_USER = os.environ.get('JAWSDB_USER')
DB_PASSWORD = os.environ.get('JAWSDB_PASSWORD')
DB_NAME = os.environ.get('JAWSDB_NAME')

mysql = MySQL(app)


# Routes
@app.route('/')
def home():
    # render home page
    return render_template("main.j2")

# import routes here to avoid ImportErrors
from games import game_routes
app.register_blueprint(game_routes)

from player_spg import player_spg_routes
app.register_blueprint(player_spg_routes)

from player_sps import player_sps_routes
app.register_blueprint(player_sps_routes)

from teams import teams_routes
app.register_blueprint(teams_routes)

from players import players_routes
app.register_blueprint(players_routes)

from seasons import seasons_routes
app.register_blueprint(seasons_routes)

from team_sps import team_sps_routes
app.register_blueprint(team_sps_routes)

from update_player_spg import update_player_spg_routes
app.register_blueprint(update_player_spg_routes)

from update_player import update_player_routes
app.register_blueprint(update_player_routes)
    
# Listener
if __name__ == "__main__":

    app.run(port=56031, debug=True)
