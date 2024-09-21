from .veiculo_routes import veiculo_bp
from .motorista_routes import motorista_bp

def init_routes(app):
    app.register_blueprint(veiculo_bp)
    app.register_blueprint(motorista_bp)