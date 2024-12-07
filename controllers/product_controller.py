
from flask import jsonify, request
from services.product_service import ProductService


product_service = ProductService()

def get_products():
    """
    GET /products
    Return the list of products.
    """
    products = product_service.get_all_products()
    return jsonify(products), 200

def add_product():
    """
    POST /products
    Add a new product after validating input.
    """
    try:
        new_product = request.get_json()

        
        if not new_product:
            return jsonify({"error": "No product data provided"}), 400
        if "title" not in new_product or "price" not in new_product or "category" not in new_product:
            return jsonify({"error": "Product must include 'title', 'price', and 'category'"}), 400

        
        product_service.add_product(new_product)
        return jsonify(product_service.get_all_products()), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500
