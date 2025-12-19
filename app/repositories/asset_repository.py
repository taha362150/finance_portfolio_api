from app.config.database import get_connection

class AssetRepository:

    def create(self, name, asset_type, current_price):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO Assets (name, asset_type, current_price)
            VALUES (?, ?, ?)
            """,
            (name, asset_type, current_price)
        )
        conn.commit()
        conn.close()

    def get_all(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Assets")
        assets = cursor.fetchall()
        conn.close()
        return assets