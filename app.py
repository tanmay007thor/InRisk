
import sys
import os
from flask import Flask
from routes.routes import product_bp
from error_handler import register_error_handlers


sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

app = Flask(__name__)


app.register_blueprint(product_bp, url_prefix="/products")


register_error_handlers(app)

if __name__ == "__main__":
    app.run(debug=True)
