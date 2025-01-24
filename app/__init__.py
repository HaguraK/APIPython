from flask import Flask

from blueprint.livros import auth_bp

app = Flask(__name__)

app.register_blueprint(auth_bp)

app.run(port=5000,host='localhost',debug=True)