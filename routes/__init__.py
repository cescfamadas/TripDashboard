from .trip import trip_bp
from .plot import plot_bp


def create_routes(server):
    server.register_blueprint(trip_bp, url_prefix='/trip')
    server.register_blueprint(plot_bp, url_prefix='/plot')
    return server
