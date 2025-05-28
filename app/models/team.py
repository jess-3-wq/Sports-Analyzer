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
