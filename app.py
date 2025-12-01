from flask import Flask, render_template, request, jsonify
from logic import otimizar_agenda, calcular_equipe_minima

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

    # 1. Roda o algoritmo de Maximização de Lucro 
    resultado_otimo = otimizar_agenda(clean_jobs)
    
    # 2. Roda o algoritmo de Dimensionamento de Equipe (Para fazer tudo)
    resultado_equipe = calcular_equipe_minima(clean_jobs)
    
    # Combina as respostas
    resposta_final = {
        **resultado_otimo, # contem "lucro_total" e "jobs_escolhidos"
        "analise_equipe": resultado_equipe # contem "tamanho_equipe"
    }

    return jsonify(resposta_final)

if __name__ == '__main__':
    app.run(debug=True)