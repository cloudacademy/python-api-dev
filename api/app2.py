#!/usr/bin/python3
from flask import Flask, jsonify, request, abort, make_response

app = Flask(__name__)

# In-memory data store for demonstration purposes
books = [
    {'id': 1, 'title': '1984', 'author': 'George Orwell'},
    {'id': 2, 'title': 'To Kill a Mockingbird', 'author': 'Harper Lee'},
    {'id': 3, 'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald'}
]

# Helper function to get a book by ID
def get_book(book_id):
    return next((book for book in books if book['id'] == book_id), None)

# Resource: Book List
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify({'books': books})

# Resource: Single Book
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book_by_id(book_id):
    book = get_book(book_id)
    if book is None:
        abort(404)
    return jsonify(book)

# Resource: Create a new Book
@app.route('/books', methods=['POST'])
def create_book():
    if not request.json or not 'title' in request.json:
        abort(400)
    new_book = {
        'id': books[-1]['id'] + 1 if books else 1,
        'title': request.json['title'],
        'author': request.json.get('author', "")
    }
    books.append(new_book)
    return jsonify(new_book), 201

# Resource: Update an existing Book
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = get_book(book_id)
    if book is None:
        abort(404)
    if not request.json:
        abort(400)
    book['title'] = request.json.get('title', book['title'])
    book['author'] = request.json.get('author', book['author'])
    return jsonify(book)

# Resource: Delete a Book
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = get_book(book_id)
    if book is None:
        abort(404)
    books.remove(book)
    return jsonify({'result': True})

# Error handling
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad request'}), 400)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)