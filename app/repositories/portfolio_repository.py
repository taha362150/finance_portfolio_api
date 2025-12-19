from app.config.database import get_connection

class PortfolioRepository:

    def create(self, client_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Portfolios (client_id) VALUES (?)",
            (client_id,)
        )
        conn.commit()
        conn.close()

    def get_by_client(self, client_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM Portfolios WHERE client_id = ?",
            (client_id,)
        )
        portfolio = cursor.fetchone()
        conn.close()
        return portfolio
