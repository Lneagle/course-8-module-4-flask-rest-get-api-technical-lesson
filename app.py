# app.py

from flask import Flask, jsonify, request

app = Flask(__name__)

# Mock product data
data = [
    {"id": 1, "name": "Laptop", "price": 899.99, "category": "electronics"},
    {"id": 2, "name": "Book", "price": 14.99, "category": "books"},
    {"id": 3, "name": "Desk", "price": 199.99, "category": "furniture"},
]

@app.route("/products", methods=["GET"])
def get_products():
    category = request.args.get("category")
    if category:
        filtered = [item for item in data if item["category"] == category]
        return jsonify(filtered), 200
    return jsonify(data), 200

# GET /products/<id> to return a single product by ID
@app.route("/products/<int:id>", methods=["GET"])
def get_single_product(id):
    product = next((item for item in data if item["id"] == id), None)
    if not product:
        return ("Product not found", 404)
    return jsonify(product) 

if __name__ == "__main__":
    app.run(debug=True)
