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

    @staticmethod
    def get_by_id(id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM youngsters WHERE id = ?", (id,))
        result = cursor.fetchone()
        conn.close()
        return result

    @staticmethod
    def update(id, name=None, academy=None, player_id=None, team_id=None):
        conn = get_connection()
        cursor = conn.cursor()
        if name:
            cursor.execute("UPDATE youngsters SET name = ? WHERE id = ?", (name, id))
        if academy:
            cursor.execute("UPDATE youngsters SET academy = ? WHERE id = ?", (academy, id))
        if player_id:
            cursor.execute("UPDATE youngsters SET player_id = ? WHERE id = ?", (player_id, id))
        if team_id:
            cursor.execute("UPDATE youngsters SET team_id = ? WHERE id = ?", (team_id, id))
        conn.commit()
        conn.close()

    @staticmethod
    def delete(id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM youngsters WHERE id = ?", (id,))
        conn.commit()
        conn.close()    
