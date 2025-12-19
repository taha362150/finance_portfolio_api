from app.config.database import get_connection

class ClientRepository:
    def create(self, name, email):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Clients (name, email) VALUES (?, ?)",
            (name, email)
        )
        conn.commit()
        conn.close()

    def get_all(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Clients")
        rows = cursor.fetchall()
        conn.close()
        return rows