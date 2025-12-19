from app.config.database import get_connection

class TransactionRepository:

    def create(self, portfolio_id, asset_id, quantity, price):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO Transactions (portfolio_id, asset_id, quantity, price)
            VALUES (?, ?, ?, ?)
            """,
            (portfolio_id, asset_id, quantity, price)
        )
        conn.commit()
        conn.close()

    def get_by_portfolio(self, portfolio_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT * FROM Transactions
            WHERE portfolio_id = ?
            """,
            (portfolio_id,)
        )
        transactions = cursor.fetchall()
        conn.close()
        return transactions