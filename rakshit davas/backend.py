from flask import Flask, render_template, jsonify, send_from_directory
import os

app = Flask(__name__, template_folder=os.path.dirname(os.path.abspath(__file__)))


@app.route("/styleing.css")
def css():
    return send_from_directory(os.path.dirname(os.path.abspath(__file__)), "styleing.css")


# Sample products data
PRODUCTS = [
    {"id": 1, "name": "Classic T-Shirt", "price": 599, "old_price": 999, "badge": "Sale"},
    {"id": 2, "name": "Running Shoes", "price": 2499, "old_price": None, "badge": None},
    {"id": 3, "name": "Smart Watch", "price": 3999, "old_price": None, "badge": "New"},
    {"id": 4, "name": "Backpack", "price": 1299, "old_price": None, "badge": None},
]


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/products")
def get_products():
    return jsonify(PRODUCTS)


@app.route("/api/products/<int:product_id>")
def get_product(product_id):
    product = next((p for p in PRODUCTS if p["id"] == product_id), None)
    if product:
        return jsonify(product)
    return jsonify({"error": "Product not found"}), 404


if __name__ == "__main__":
    app.run(debug=True, port=5000)
