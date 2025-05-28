from app.connection import get_connection

class Team:
    @staticmethod
    def create(name, league):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO teams (name, league) VALUES (?, ?)", (name, league))
        conn.commit()
        conn.close()

    @staticmethod
    def all():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM teams")
        teams = cursor.fetchall()
        conn.close()
        return teams   

    @staticmethod
    def get_by_id(id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM teams WHERE id = ?", (id,))
        result = cursor.fetchone()
        conn.close()
        return result

    @staticmethod
    def update(id, name=None, league=None):
        conn = get_connection()
        cursor = conn.cursor()
        if name:
            cursor.execute("UPDATE teams SET name = ? WHERE id = ?", (name, id))
        if league:
            cursor.execute("UPDATE teams SET league = ? WHERE id = ?", (league, id))
        conn.commit()
        conn.close()

    @staticmethod
    def delete(id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM teams WHERE id = ?", (id,))
        conn.commit()
        conn.close()     
