from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "<h1>Trabalho Fiap - 1MOBRBB</h1><h3>CLOUD ARCHITECTURE & DEVOPS</h2><h3>Alunos</h3><h4>Anderson André dos Santos</h4><h4>Adriano Bastos e Silva Moraes</h4><h4>Gustavo Souza Rodrigues</h4><h4>Luis Fernando de Sena Carita</h4><h4>Paulo Roberto Petrilho</h4>\nMBA! o/"

if __name__ == '__main__':
    # application.run()
    application.run(host='0.0.0.0',debug=True)
