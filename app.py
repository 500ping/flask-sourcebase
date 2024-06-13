from flasgger import Swagger
from flask import Flask
from flask_migrate import Migrate

from src import settings
from src.apis.v1 import api_v1
from src.commons.database import db

# Create app
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = settings.db_url

# Setup database
db.init_app(app)
app.app_context().push()
migrate = Migrate(app, db)

# Setup swagger
swagger = Swagger(app)

# Register api route
app.register_blueprint(api_v1, url_prefix="/api/v1")

if __name__ == "__main__":
    app.run(port=5000, debug=settings.debug)
