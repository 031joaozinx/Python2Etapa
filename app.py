# Cenário: A - Locadora
# Aluno: Seu Nome

from flask import Flask
from models import db
from controllers import locadora_bp

app = Flask(__name__)

# Configuração do banco de dados
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///banco.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "123456"

# Inicializa o banco
db.init_app(app)

# Registra o Blueprint
app.register_blueprint(locadora_bp)

# Cria as tabelas
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)