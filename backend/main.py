"""Ponto de entrada da API Synapse 3D"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Synapse 3D",
    description="Sistema de visão computacional para rede de farmácias",
    version="1.0.0",
)

# Configurar CORS para o frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em produção, especificar domínios
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {
        "message": "Synapse 3D API",
        "status": "online",
        "version": "1.0.0",
    }


@app.get("/health")
async def health():
    return {"status": "healthy"}


# Rotas serão adicionadas conforme o desenvolvimento avança:
# - /cameras (CRUD de câmeras por loja)
# - /stores (CRUD de lojas)
# - /heatmap (dados de heatmap)
# - /alerts (alertas de furto)
# - /ws (WebSocket para eventos em tempo real)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
