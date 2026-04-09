from flask import Flask, jsonify, request, abort
from datetime import datetime

app = Flask(__name__)

books = [
    {
        "id": 1,
        "title": "Cien años de soledad",
        "author": "Gabriel García Márquez",
        "available": True,
        "loaned_to": None,
        "loan_date": None,
    }
]
next_id = 2

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Biblioteca simple lista", "books": len(books)})

@app.route("/books", methods=["GET"])
def list_books():
    return jsonify(books)

@app.route("/books", methods=["POST"])
def add_book():
    global next_id
    data = request.get_json() or {}
    title = data.get("title")
    author = data.get("author")

    if not title or not author:
        abort(400, description="Se requieren 'title' y 'author'.")

    book = {
        "id": next_id,
        "title": title,
        "author": author,
        "available": True,
        "loaned_to": None,
        "loan_date": None,
    }
    books.append(book)
    next_id += 1
    return jsonify(book), 201

@app.route("/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    book = next((b for b in books if b["id"] == book_id), None)
    if not book:
        abort(404, description="Libro no encontrado.")
    return jsonify(book)

@app.route("/books/<int:book_id>/loan", methods=["POST"])
def loan_book(book_id):
    data = request.get_json() or {}
    user = data.get("user")
    if not user:
        abort(400, description="Se requiere el campo 'user'.")
    book = next((b for b in books if b["id"] == book_id), None)
    if not book:
        abort(404, description="Libro no encontrado.")
    if not book["available"]:
        abort(400, description="El libro ya está prestado.")

    book["available"] = False
    book["loaned_to"] = user
    book["loan_date"] = datetime.utcnow().isoformat() + "Z"
    return jsonify(book)

@app.route("/books/<int:book_id>/return", methods=["POST"])
def return_book(book_id):
    book = next((b for b in books if b["id"] == book_id), None)
    if not book:
        abort(404, description="Libro no encontrado.")
    if book["available"]:
        abort(400, description="El libro no está prestado.")

    book["available"] = True
    book["loaned_to"] = None
    book["loan_date"] = None
    return jsonify(book)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
