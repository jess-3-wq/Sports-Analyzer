from app.connection import get_connection

def initialize_database():
    conn = get_connection()
    cursor = conn.cursor()
    with open("app/schema.sql", "r") as f:
        cursor.executescrippt(f.read())
    conn.commit()
    conn.close()
    print("Database and tables created")

if __name__ == "__main__":
    initialize_database()        