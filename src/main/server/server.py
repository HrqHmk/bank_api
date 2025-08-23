from flask import Flask
from flask_cors import CORS
from src.models.sqlite.settings.connection import db_connection_handler
from src.main.routes.individual_routes import individual_route_bp
from src.main.routes.legal_entity_routes import legal_entity_route_bp

db_connection_handler.connect_to_db()

app = Flask(__name__)
CORS(app)

app.register_blueprint(individual_route_bp)
app.register_blueprint(legal_entity_route_bp)
