import requests, json, random, time, datetime, os

# === CONFIGURAÇÃO ===
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(BASE_DIR, "config.json")) as f:
    CONFIG = json.load(f)

API_URL = CONFIG["api_url"]
INTERVALO = CONFIG["intervalo_envio_segundos"]

# === FUNÇÃO DE GERAÇÃO DE DADOS ===
def gerar_dado():
    pragas = ["Broca-da-cana", "Cigarrinha", "Lagarta", "Pulgão"]
    dado = {
        "id_armadilha": random.choice(CONFIG["armadilhas"]),
        "tipo_praga": random.choice(pragas),
        "contagem": random.randint(0, 60),
        "latitude": CONFIG["latitude_base"] + random.uniform(-0.01, 0.01),
        "longitude": CONFIG["longitude_base"] + random.uniform(-0.01, 0.01),
        "timestamp": datetime.datetime.now().isoformat()
    }
    return dado

# === LOOP DE ENVIO ===
print("🚀 Iniciando simulador de armadilhas IoT...\n")
while True:
    dado = gerar_dado()
    try:
        r = requests.post(API_URL, json=dado, timeout=5)
        status = "✅ Sucesso" if r.status_code == 200 else f"⚠️ Erro {r.status_code}"
        print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] {status}: {dado}")
    except Exception as e:
        print(f"❌ Falha ao enviar: {e}")
    time.sleep(INTERVALO)

