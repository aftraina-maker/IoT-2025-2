from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import datetime

app = FastAPI()

# In-memory data store
data_store = []

@app.get("/")
def health_check():
    return {"status": "ok"}

@app.post("/api/dados")
async def receive_data(request: Request):
    """Recebe dados e adiciona timestamp atual"""
    new_data = await request.json()
    new_data["timestamp"] = datetime.datetime.now().isoformat()
    data_store.append(new_data)
    return {"status": "success"}

@app.post("/search")
async def search():
    """Retorna as séries disponíveis (nomes das pragas)"""
    pragas = sorted(set(item["tipo_praga"] for item in data_store))
    return pragas

@app.post("/query")
async def query(request: Request):
    """Retorna os dados formatados para o Grafana"""
    req_json = await request.json()
    response = []

    # Cria uma série para cada tipo de praga
    pragas = sorted(set(item["tipo_praga"] for item in data_store))
    for praga in pragas:
        datapoints = [
            [item["contagem"], int(datetime.datetime.fromisoformat(item["timestamp"]).timestamp() * 1000)]
            for item in data_store
            if item["tipo_praga"] == praga
        ]
        response.append({
            "target": praga,
            "datapoints": datapoints
        })
    return JSONResponse(content=response)

@app.post("/annotations")
async def annotations():
    """Retorna lista vazia (não usado por enquanto)"""
    return []

# 🚀 Executar localmente
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)
