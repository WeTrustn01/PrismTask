from app import db
#trade Model
class Trade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    currency = db.Column(db.String(80))
    quantity = db.Column(db.Integer)
    direction = db.Column(db.String(80))

    def __init__(self, currency, quantity, direction):
        self.currency = currency
        self.quantity = quantity
        self.direction = direction
