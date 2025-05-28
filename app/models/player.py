from app.connection import get_connection

class Player:
    @staticmethod
    def create(name, position, team_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO players (name, position, team_id) VALUES (?, ?, ?)",
            (name, position, team_id)
        )
        conn.commit()
        conn.close()

    @staticmethod
    def all():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM players")
        players = cursor.fetchall()
        conn.close()
        return players

    @staticmethod
    def find_by_team(team_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM players WHERE team_id = ?", (team_id,))
        players = cursor.fetchall()
        conn.close()
        return players
