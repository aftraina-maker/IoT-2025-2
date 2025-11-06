import requests, json, random, time, datetime

with open("config.json") as f:
    CONFIG = json.load(f)

def gerar_dado():
    pragas = ["Broca-da-cana", "Cigarrinha", "Lagarta", "Pulgão"]
    return {
        "id_armadilha": random.choice(CONFIG["armadilhas"]),
        "tipo_praga": random.choice(pragas),
        "contagem": random.randint(0, 80),
        "latitude": CONFIG["latitude_base"] + random.uniform(-0.01, 0.01),
        "longitude": CONFIG["longitude_base"] + random.uniform(-0.01, 0.01),
        "timestamp": datetime.datetime.now().isoformat()
    }

while True:
    dado = gerar_dado()
    r = requests.post(CONFIG["api_url"], json=dado)
    print(f"Enviado: {dado} | Status: {r.status_code}")
    time.sleep(CONFIG["intervalo_envio_segundos"])
