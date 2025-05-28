from app.connection import get_connection

class Youngster:
    @staticmethod
    def create(name, academy, player_id, team_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO youngsters (name, academy, player_id, team_id) VALUES (?, ?, ?, ?)",
            (name, academy, player_id, team_id)
        )
        conn.commit()
        conn.close()

    @staticmethod
    def all():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM youngsters")
        youngsters = cursor.fetchall()
        conn.close()
        return youngsters

    @staticmethod
    def find_by_team(team_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM youngsters WHERE team_id = ?", (team_id,))
        results = cursor.fetchall()
        conn.close()
        return results
