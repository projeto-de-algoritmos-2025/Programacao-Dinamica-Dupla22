from flask import Flask, render_template, request, jsonify
from logic import otimizar_agenda

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular', methods=['POST'])
def calcular():
    data = request.json
    jobs = data.get('jobs', [])
    
    clean_jobs = []
    for j in jobs:
        try:
            clean_jobs.append({
                'nome': j['nome'],
                'inicio': int(j['inicio']),
                'fim': int(j['fim']),
                'valor': float(j['valor']),
                'id': j['id']
            })
        except ValueError:
            continue

    if not clean_jobs:
        return jsonify({"error": "Dados inválidos"}), 400

    resultado = otimizar_agenda(clean_jobs)
    return jsonify(resultado)

if __name__ == '__main__':
    app.run(debug=True)