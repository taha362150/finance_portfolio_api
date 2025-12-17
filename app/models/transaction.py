class Transaction:
    def __init__(self, transaction_id, portfolio_id, asset_id, quantity, price):
        self.transaction_id = transaction_id
        self.portfolio_id = portfolio_id
        self.asset_id = asset_id
        self.quantity = quantity
        self.price = price