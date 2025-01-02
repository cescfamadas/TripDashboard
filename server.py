from flask import Flask, jsonify
import pandas as pd
from Config import Config
import Database as db
import routes

app = None


def create_app():
    global app
    app = Flask(__name__)
    app.config.from_object(Config)
    app = routes.create_routes(app)

    @app.errorhandler(404)
    def not_found_error(error):
        return jsonify({"error": "Not found", "message": str(error)}), 404
    dades = pd.read_csv(Config.DATA_FILE)

    db_instance = db.Database()
    dades.to_sql('products', db_instance.conn,
                 index=False, if_exists='replace')
    return app


if __name__ == '__main__':
    dades = pd.read_csv(Config.DATA_FILE)

    db_instance = db.Database()
    dades.to_sql('products', db_instance.conn,
                 index=False, if_exists='replace')

    app = create_app()

    app.run(debug=True)
