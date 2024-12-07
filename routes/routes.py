
from flask import Blueprint
from controllers.product_controller import get_products, add_product


product_bp = Blueprint("products", __name__)


product_bp.route("/", methods=["GET"])(get_products)
product_bp.route("/", methods=["POST"])(add_product)
