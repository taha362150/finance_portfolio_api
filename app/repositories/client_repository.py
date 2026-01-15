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
    
####################################################################   
    
    def update(self, client_id, name, email):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE Clients SET name = ?, email = ? WHERE client_id = ?",
            (name, email, client_id)
        )
        conn.commit()
        updated_rows = cursor.rowcount
        conn.close()
        return updated_rows

    def delete(self, client_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM Clients WHERE client_id = ?",
            (client_id,)
        )
        conn.commit()
        deleted_rows = cursor.rowcount
        conn.close()
        return deleted_rows

