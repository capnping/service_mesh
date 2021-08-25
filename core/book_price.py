import os
import sys
import random
import logging

from flask import Flask, request, render_template, jsonify, abort
from flask_cors import CORS

app = Flask(__name__, instance_relative_config=True)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:root@db/main' # On Docker
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///main.sqlite3" # To test on local
CORS(app)

logger = logging.getLogger(f'Custom App {os.environ.get("VER")}')
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

try:
    from db import db, Prices
except: # TODO fix circular imports !!!
    from .db import db, Prices
    
db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
def index():    
    return render_template('price.html', books=Prices.query.all(), version=os.environ.get('VER'))


@app.route('/book/add_book/', methods=['POST'])
def add_book():
    """
    Example Request:
    ----------------
    {
        "book_name": "MyBook",
        "book_price": "29.00"
    }
    """
    content = request.get_json()
    try:
        print(content)
        book = Prices(**content)
        db.session.add(book)
        db.session.commit()
    except Exception as e:
        abort(400, str(e))

    return jsonify({
        'message': 'success',
        'version': os.environ.get('VER')
    })


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
