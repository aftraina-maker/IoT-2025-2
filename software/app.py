
import cv2
import numpy as np
from flask import Flask, request, jsonify
from flask_cors import CORS
import io

# 1. Inicialização do Backend Flask
app = Flask(__name__)
# Habilita CORS para permitir requisições do frontend
CORS(app)

# 2. Definição dos Ranges de Maturação (HSV para Morango)
# Estes valores podem ser ajustados para outras frutas ou condições de iluminação
HSV_RANGES = {
    "morango": {
        "imaturo": {
            "lower": np.array([40, 50, 50]),
            "upper": np.array([80, 255, 255])
        },
        "ideal": {
            "lower": np.array([0, 150, 150]),
            "upper": np.array([10, 255, 255])
        },
        "maduro": {
            "lower": np.array([0, 200, 100]),
            "upper": np.array([5, 255, 200])
        }
    },
    "banana": {
        "imaturo": {
            "lower": np.array([30, 100, 100]), # Green
            "upper": np.array([70, 255, 255])
        },
        "ideal": {
            "lower": np.array([20, 100, 100]), # Yellow
            "upper": np.array([30, 255, 255])
        },
        "maduro": {
            "lower": np.array([10, 100, 100]), # Brownish/Darker Yellow
            "upper": np.array([20, 255, 255])
        }
    }
}

# 3. Endpoint da API para Análise de Imagem
@app.route('/api/analyze', methods=['POST'])
def analyze_image():
    # Verifica se o arquivo de imagem foi enviado na requisição
    if 'file' not in request.files:
        return jsonify({"error": "Nenhum arquivo enviado"}), 400

    file = request.files['file']
    
    # Lê os bytes da imagem em memória
    in_memory_file = io.BytesIO()
    file.save(in_memory_file)
    data = np.frombuffer(in_memory_file.getvalue(), dtype=np.uint8)
    
    # Decodifica a imagem usando OpenCV (o padrão é BGR)
    img_bgr = cv2.imdecode(data, cv2.IMREAD_COLOR)
    if img_bgr is None:
        return jsonify({"error": "Não foi possível ler a imagem"}), 400

    # Converte de BGR para RGB para o cálculo da cor dominante correta
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

    # 4. Processamento da Imagem
    # Foca na região central da imagem para evitar ruídos de fundo
    h, w, _ = img_bgr.shape
    crop_img = img_bgr[h//4 : 3*h//4, w//4 : 3*w//4]

    # Converte a imagem cortada para o espaço de cores HSV
    hsv_img = cv2.cvtColor(crop_img, cv2.COLOR_BGR2HSV)
    
    # Calcula a média dos valores de H, S, V na região central
    mean_hsv = np.mean(hsv_img, axis=(0, 1))
    
    # 5. Classificação do Estágio de Maturação
    status = "desconhecido"
    fruit = request.form.get('fruit', 'banana') # Assume 'banana' if not specified
    if fruit not in HSV_RANGES:
        return jsonify({"error": f"Fruta '{fruit}' não suportada"}), 400
    
    ranges = HSV_RANGES[fruit]

    # Compara a média HSV com os ranges predefinidos
    if (ranges["ideal"]["lower"][0] <= mean_hsv[0] <= ranges["ideal"]["upper"][0]) and \
       (ranges["ideal"]["lower"][1] <= mean_hsv[1] <= ranges["ideal"]["upper"][1]) and \
       (ranges["ideal"]["lower"][2] <= mean_hsv[2] <= ranges["ideal"]["upper"][2]):
        status = "ideal"
        maturacao_percentual = 85
        recomendacao = "Colher agora"
    elif (ranges["maduro"]["lower"][0] <= mean_hsv[0] <= ranges["maduro"]["upper"][0]) and \
         (ranges["maduro"]["lower"][1] <= mean_hsv[1] <= ranges["maduro"]["upper"][1]) and \
         (ranges["maduro"]["lower"][2] <= mean_hsv[2] <= ranges["maduro"]["upper"][2]):
        status = "maduro"
        maturacao_percentual = 100
        recomendacao = "Processar imediatamente"
    elif (ranges["imaturo"]["lower"][0] <= mean_hsv[0] <= ranges["imaturo"]["upper"][0]) and \
         (ranges["imaturo"]["lower"][1] <= mean_hsv[1] <= ranges["imaturo"]["upper"][1]) and \
         (ranges["imaturo"]["lower"][2] <= mean_hsv[2] <= ranges["imaturo"]["upper"][2]):
        status = "imaturo"
        maturacao_percentual = 30
        recomendacao = "Aguardar para colher"
    else:
        # Caso não se encaixe em nenhum range conhecido
        maturacao_percentual = 0
        recomendacao = "Análise inconclusiva"

    # 6. Extração da Cor Dominante (Média RGB)
    # Redimensiona para performance e calcula a cor média
    resized_img_rgb = cv2.resize(img_rgb, (150, 150), interpolation=cv2.INTER_AREA)
    dominant_color_rgb = np.mean(resized_img_rgb, axis=(0, 1)).astype(int)

    # 7. Montagem e Retorno da Resposta JSON
    response_data = {
        "fruta": fruit,
        "status": status,
        "maturacao_percentual": maturacao_percentual,
        "recomendacao": recomendacao,
        "cor_dominante_rgb": dominant_color_rgb.tolist(),
        "hsv_medio_detectado": mean_hsv.astype(int).tolist()
    }
    
    return jsonify(response_data)

# Ponto de entrada para executar o servidor Flask
if __name__ == '__main__':
    # Executa na rede local (0.0.0.0) para ser acessível por outros dispositivos
    app.run(host='0.0.0.0', port=5000, debug=True)
