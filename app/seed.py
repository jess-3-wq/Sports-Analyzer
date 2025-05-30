import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.models.team import Team
from app.models.player import Player
from app.models.youngster import Youngster

teams = [
    ("Arsenal", "Premier League"),
    ("Manchester City", "Premier League"),
    ("Liverpool", "Premier League")
]

print("Top teams....")
for name, league in teams:
       print(f"Inserting team: {name}, league: {league}")
    Team.create(name, league)

from app.connection import get_connection

def get_team_id_by_name(name):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM teams WHERE name = ?", (name,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None

arsenal_id = get_team_id_by_name("Arsenal")
mancity_id = get_team_id_by_name("Manchester City")
liverpool_id = get_team_id_by_name("Liverpool")

print("My top players....")

players = [
    ("Bukayo Saka", "Winger", arsenal_id),
    ("William Saliba", "Center back", arsenal_id),
    ("Martin Ødegaard", "Midfielder", arsenal_id),
    ("Erling Haaland", "Striker", mancity_id),
    ("Kevin De Bruyne", "Midfielder", mancity_id),
    ("Mohamed Salah", "Winger", liverpool_id),
     ("Van Djik", "Center back", liverpool_id),

]

for name, position, team_id in players:
       print(f"Inserting player: {name}, team_id: {team_id}")
    Player.create(name, position, team_id)

def get_player_id_by_name(name): 
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM players WHERE name = ?", (name,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None   

saka_id = get_player_id_by_name("Bukayo Saka")
haaland_id = get_player_id_by_name("Erling Haaland")
saliba_id = get_player_id_by_name("William Saliba")
djik_id = get_player_id_by_name("Van Djik")

print("best youngsters...")
youngsters = [
    ("Ethan Nwaneri", "Arsenal Academy", saka_id, arsenal_id),
    ("Oscar Bobb", "City Academy", haaland_id, mancity_id),
    ("Lewis-Skelly", "Arsenal Academy", saliba_id, arsenal_id),
    ("Bradely", "Liverpool Academy", djik_id, liverpool_id)

]

for name, academy, player_id, team_id in youngsters:
       print(f"Inserting youngster: {name},player_id:{player_id} team_id: {team_id}")
    Youngster.create(name, academy, player_id, team_id)

print("Teams are complete")    
