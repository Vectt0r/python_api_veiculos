from flask import Flask
from database import db
from routes import init_routes
from config import Config  # Certifique-se de importar a configuração

app = Flask(__name__)
app.config.from_object(Config)  # Carrega a configuração

# Inicializa a conexão com o banco de dados
db.init_app(app)

# Inicializa as rotas
init_routes(app)

if __name__ == '__main__':
    app.run(debug=True)
