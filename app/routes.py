from app import app, db
from flask import render_template, flash, redirect, request, jsonify, json, Response
from app.models import Trade
from flask_marshmallow import Marshmallow

#used to jsonify Models
ma = Marshmallow(app)

class TradeSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id', 'currency', 'quantity', 'direction')

trade_schema = TradeSchema()
trades_schema = TradeSchema(many=True)
#route for interacting with a single trade
@app.route('/trades/<int:trade_id>', methods=['GET', 'PATCH', 'DELETE'])
def tradeID(trade_id):
    #if a get request
    if request.method == 'GET':
        trade = Trade.query.get(trade_id)
        result = trade_schema.dump(trade)

        return jsonify(result)
    #if a patch request
    elif request.method == 'PATCH':
        trade = Trade.query.get(trade_id)
        #get params from the form
        currency = request.form.get('currency')
        quantity = request.form.get('quantity')
        direction = request.form.get('direction')

        trade.currency = currency
        trade.quantity = quantity
        trade.direction = direction

        db.session.commit()
        #reurn json
        result = trade_schema.dump(trade)
        return jsonify(result)
    #if a delete request
    elif request.method == 'DELETE':
        trade = Trade.query.get(trade_id)
        db.session.delete(trade)
        db.session.commit()

        result = trade_schema.dump(trade)
        return jsonify(result)

    else:
        return 'Err: Bad Request!'

#either get all trades or create a trade
@app.route('/trades', methods=['GET', 'POST'])
def trade():
    if request.method == 'GET':
        trades = Trade.query.all()
        result = trades_schema.dump(trades)
        return jsonify(result)

    elif request.method == 'POST':
        currency = request.form.get('currency')
        quantity = request.form.get('quantity')
        direction = request.form.get('direction')

        trade = Trade(currency, quantity, direction)

        db.session.add(trade)
        db.session.commit()

        result = trade_schema.dump(trade)
        return jsonify(result)

    else:
        return 'Err: Bad Request for /trades'

#home page route
@app.route('/')
def index():
    return render_template('index.html')
