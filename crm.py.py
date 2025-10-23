
pip install 
requests beautifulsoup4 polar_coordinates
numpy matplotlib scipy pandas seaborn scikit-Learn JupyterLab 
tensorflow keras nltk spacy gensim 
torch torchvision torchaudio transformers 
plotly dash boken 
flask django fastapi uvicorn gunicorn
    jupyterlab-git jupyterlab-lsp jupyterlab-toc 
    jupyterlab-dash jupyterlab-plotly
    pip install jupyterlab jupyterlab_code_formatter jupyterlab-system-monitor jupyterlab-theme-solarized-dark 
    jupyterlab-theme-solarized-light 
    crm_web/
├── app.py
├── templates/
│   ├── index.html
│   ├── adicionar.html
│   └── buscar.html
|── static/
|  |- styles.classcss
| | - script.J·s
|- requirements.txt 
flask_ sqlalchemy flask_wtf wtforms
from flask import Flask, render_template, request, redirect
import os
import json
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
clientes = []

@app.route('/')
def index():
    return render_template('index.html', clientes=clientes)

@app.route('/adicionar', methods=['GET', 'POST'])
def adicionar():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        telefone = request.form['telefone']
        empresa = request.form['empresa']
        clientes.append({
            'nome': nome,
            'email': email,
            'telefone': telefone,
            'empresa': empresa
        })
        return redirect('/')
    return render_template('adicionar.html')

@app.route('/buscar', methods=['GET'])
def buscar():
    termo = request.args.get('termo', '')
    resultados = [c for c in clientes if termo.lower() in c['nome'].lower()]
    return render_template('buscar.html', resultados=resultados, termo=termo)

if __name__ == '__main__':
    app.run(debug=True)
<!DOCTYPE html>
<html>
<head><title>CRM - Clientes</title></head>
<body>
    <h1>📋 Lista de Clientes</h1>
    <a href="/adicionar">➕ Adicionar Cliente</a> | 
    <a href="/buscar">🔍 Buscar Cliente</a>
    <ul>
        {% for cliente in clientes %}
        <li>{{ cliente.nome }} - {{ cliente.email }} - {{ cliente.telefone }} - {{ cliente.empresa }}</li>
        {% endfor %}
    </ul>
</body>
</html>
<!DOCTYPE html>
<html>
<head><title>Adicionar Cliente</title></head>
<body>
    <h1>➕ Novo Cliente</h1>
    <form method="post">
        Nome: <input type="text" name="nome"><br>
        Email: <input type="email" name="email"><br>
        Telefone: <input type="text" name="telefone"><br>
        Empresa: <input type="text" name="empresa"><br>
        <button type="submit">Salvar</button>
    </form>
</body>
</html>
<!DOCTYPE html>
<html>
<head><title>Buscar Cliente</title></head>
<body>
    <h1>🔍 Buscar Cliente</h1>
    <form method="get">
        Nome: <input type="text" name="termo" value="{{ termo }}">
        <button type="submit">Buscar</button>
    </form>
    <ul>
        {% for cliente in resultados %}
        <li>{{ cliente.nome }} - {{ cliente.email }} - {{ cliente.telefone }} - {{ cliente.empresa }}</li>
        {% endfor %}
    </ul>
</body>
</html>
<!DOCTYPE html>
<html>
<head><title>Buscar Cliente</title></head>
<body>
    <h1>🔍 Buscar Cliente</h1>
    <form method="get">
        Nome: <input type="text" name="termo" value="{{ termo }}">
        <button type="submit">Buscar</button>
    </form>
    <ul>
        {% for cliente in resultados %}
        <li>{{ cliente.nome }} - {{ cliente.email }} - {{ cliente.telefone }} - {{ cliente.empresa }}</li>
        {% endfor %}
    </ul>
</body>
</html>
# Ensure the required packages are installed

required_packages = [
    "requests", "beautifulsoup4", "polar_coordinates",
    "numpy", "matplotlib", "scipy", "pandas", "seaborn", "scikit-learn", "jupyterlab",
    "tensorflow", "keras", "nltk", "spacy", "gensim",
    "torch", "torchvision", "torchaudio", "transformers",
    "plotly", "dash", "bokeh",
    "flask", "django", "fastapi", "uvicorn", "gunicorn",
    "jupyterlab-git", "jupyterlab-lsp", "jupyterlab-toc",
    "jupyterlab-dash", "jupyterlab-plotly",
    "jupyterlab_code_formatter", "jupyterlab-system-monitor",
    "jupyterlab-theme-solarized-dark", "jupyterlab-theme-solarized-light",
    "flask_sqlalchemy", "flask_wtf", "wtforms"
]

for package in required_packages:
    os.system(f"pip install {package}")
    print(f"Installed {package}")
    # Corrigindo o erro de importação e duplicidade
    # Removendo linha incorreta:
    # from tensorflow .keras.lyers import Dense
gitclone https://github.com/Godofredo-BS/CRM-Guilherme-Queiroz-.git
git config --global user.name "Seu Nome"
git config --global user.email "seu email"@example.com
crm = CRM()
    crm.buscar_cliente(termo)
    elif opcao == "4":
        print("Saindo do CRM. Até mais!")
        break
    git clone https://github.com/Godofredo-BS/CRM-Guilherme-Queiroz-.git
cd seu-repositorio
code .
git init
git add .
git commit -m "Primeiro commit"
app = Flask(__name__)
DATA_FILE = os.path.join(os.path.dirname(__file__), "clientes.json")

def load_clientes():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_clientes(clientes):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(clientes, f, ensure_ascii=False, indent=2)

clientes = load_clientes()

@app.route("/")
def index():
    return render_template("index.html", clientes=clientes)

@app.route("/adicionar", methods=["GET", "POST"])
def adicionar():
    if request.method == "POST":
        nome = request.form.get("nome", "").strip()
        email = request.form.get("email", "").strip()
        telefone = request.form.get("telefone", "").strip()
        empresa = request.form.get("empresa", "").strip()

        if nome:  # minimal validation
            cliente = {"nome": nome, "email": email, "telefone": telefone, "empresa": empresa}
            clientes.append(cliente)
            save_clientes(clientes)
            return redirect(url_for("index"))

    return render_template("adicionar.html")

@app.route("/buscar", methods=["GET"])
def buscar():
    termo = request.args.get("termo", "").strip()
    if termo:
        resultados = [c for c in clientes if termo.lower() in c.get("nome", "").lower()]
    else:
        resultados = []
    return render_template("buscar.html", resultados=resultados, termo=termo)

if __name__ == "__main__":
    # Use 0.0.0.0 only when you want it reachable from other machines
    app.run(debug=True)
git clone https://github.com/Godofredo-BS/CRM-Guilherme-Queiroz-.git
cd CRM-Guilherme-Queiroz-
code .
git add .
git commit -m "Atualizações no app e templates"
git push
pasta: crm_web/arquivo: .env
FLASK_ENV=development
FLASK_APP=app.py
SECRET_KEY=uma-chave-super-secreta
PORT=5000
DATABASE_URL=sqlite:///crm.debug.db
import os
from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default-key')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///crm.db')
import os
from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default-key')
pip install python-dotenv
from dotenv import load_dotenv
load_dotenv()







    

    

