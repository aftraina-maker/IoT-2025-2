from flask import Flask, request, jsonify
from firebase_admin import credentials, firestore, initialize_app
import datetime  # <-- Faltava essa importação

app = Flask(__name__)

# ============================================================
# INICIALIZAÇÃO DO FIREBASE
# ============================================================
# A SDK do Firebase usará automaticamente a variável de ambiente GOOGLE_APPLICATION_CREDENTIALS
# que foi definida no docker-compose.yml.
initialize_app()
db = firestore.client()

# Referência à coleção no Firestore
dados_ref = db.collection("monitoramento_pragas")

# ============================================================
# ROTA 0: Health Check para o Grafana
# ============================================================
@app.route("/", methods=["GET"])
def health_check():
    return jsonify({"status": "ok"})


# ============================================================
# ROTA 1: Receber dados (POST)
# ============================================================
@app.route("/api/dados", methods=["POST"])
def receber_dados():
    data = request.json
    if not data:
        return jsonify({"erro": "JSON inválido"}), 400
    try:
        data["timestamp"] = datetime.datetime.now().isoformat()
        dados_ref.add(data)
        return jsonify({"mensagem": "Dado registrado com sucesso"}), 200
    except Exception as e:
        return jsonify({"erro": str(e)}), 500


# ============================================================
# ROTA 2: Listar dados (GET)
# ============================================================
@app.route("/api/dados", methods=["GET"])
def listar_dados():
    try:
        docs = dados_ref.stream()
        resultado = []
        for doc in docs:
            doc_dict = doc.to_dict()
            doc_dict["id"] = doc.id
            resultado.append(doc_dict)
        return jsonify(resultado), 200
    except Exception as e:
        return jsonify({"erro": str(e)}), 500


# ============================================================
# ROTA 3: Endpoint usado pelo Grafana para listar métricas
# ============================================================
@app.route("/search", methods=["POST"])
def search():
    distinct_pragas = set()
    for doc in dados_ref.stream():
        data = doc.to_dict()
        if 'tipo_praga' in data:
            distinct_pragas.add(data['tipo_praga'])
    return jsonify(list(distinct_pragas))


# ============================================================
# ROTA 4: Endpoint usado pelo Grafana para consultas (mapa)
# ============================================================
@app.route("/query", methods=["POST"])
def query():
    req = request.json
    try:
        from_time = datetime.datetime.fromisoformat(req['range']['from'].replace('Z', '+00:00'))
        to_time = datetime.datetime.fromisoformat(req['range']['to'].replace('Z', '+00:00'))

        docs = dados_ref.stream()
        
        # Estrutura da tabela para o Grafana
        table_response = [
            {
                "columns": [
                    {"text": "latitude", "type": "number"},
                    {"text": "longitude", "type": "number"},
                    {"text": "tipo_praga", "type": "string"},
                    {"text": "contagem", "type": "number"},
                    {"text": "id_armadilha", "type": "string"},
                    {"text": "timestamp", "type": "time"}
                ],
                "rows": [],
                "type": "table"
            }
        ]

        for doc in docs:
            doc_data = doc.to_dict()
            if all(k in doc_data for k in ['timestamp', 'contagem', 'latitude', 'longitude', 'tipo_praga', 'id_armadilha']):
                # Converte o timestamp do documento para datetime
                doc_time = datetime.datetime.fromisoformat(doc_data['timestamp'])
                
                # Filtra pelo range de tempo do Grafana
                if from_time <= doc_time <= to_time:
                    # Adiciona os dados como uma nova linha na tabela
                    table_response[0]["rows"].append([
                        doc_data['latitude'],
                        doc_data['longitude'],
                        doc_data['tipo_praga'],
                        doc_data['contagem'],
                        doc_data['id_armadilha'],
                        int(doc_time.timestamp() * 1000)  # Timestamp em milissegundos para o Grafana
                    ])

        return jsonify(table_response)

    except Exception as e:
        return jsonify([{"erro": str(e)}])  # Retorna erro dentro da estrutura esperada


# ============================================================
# ROTA 5: Placeholder (Grafana usa às vezes para anotações)
# ============================================================
@app.route("/annotations", methods=["POST"])
def annotations():
    return jsonify([])


# ============================================================
# EXECUÇÃO LOCAL
# ============================================================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

