from app import app
from app.routes import routes
import sys

app.register_blueprint(routes, url_prefix="")


if __name__ == "__main__":
    app.run(debug=True)