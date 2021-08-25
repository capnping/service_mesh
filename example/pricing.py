from flask import Flask,jsonify, request


book_price = [
    {
        "name": 'war and peace',
        "price": 22.99
    }
    
]

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World"


@app.route('/book_list')
def get_book_list():
    return jsonify({"book_price": book_price})



@app.route('/book_info/<string:name>')
def get_book_info(name):
    for book in book_price:
        if book['name'] == name:
            return jsonify(book)


@app.route('/add_book', methods=['POST'])
def add_book():
    request_data = request.get_json()
    new_book = {
        "name": request_data['name'],
        'price': request_data['price']
    }
    book_price.append(new_book)

    return jsonify({"book_price": book_price})


app.run()