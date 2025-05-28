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

    @staticmethod
    def get_by_id(id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM players WHERE id = ?", (id,))
        result = cursor.fetchone()
        conn.close()
        return result

    @staticmethod
    def update(id, name=None, position=None, team_id=None):
        conn = get_connection()
        cursor = conn.cursor()
        if name:
            cursor.execute("UPDATE players SET name = ? WHERE id = ?", (name, id))
        if position:
            cursor.execute("UPDATE players SET position = ? WHERE id = ?", (position, id))
        if team_id:
            cursor.execute("UPDATE players SET team_id = ? WHERE id = ?", (team_id, id))
        conn.commit()
        conn.close()

    @staticmethod
    def delete(id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM players WHERE id = ?", (id,))
        conn.commit()
        conn.close()    
