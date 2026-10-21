# 🧠 Synapse 3D

Sistema de visão computacional para rede de farmácias — rastreamento de atenção do cliente, prevenção de furto e visualização 3D de lojas.

---

## 🏪 Sobre o Projeto

O **Synapse 3D** é uma solução de inteligência artificial para varejo farmacêutico, desenvolvida para uma rede de **40 lojas no estado do Ceará**. Aproveita o sistema de câmeras de segurança já existente para gerar insights sobre o comportamento do cliente dentro de cada loja.

### O que o sistema faz

| Funcionalidade | Descrição |
|---------------|-----------|
| 🔥 Heatmap de Atenção | Onde os clientes mais olham e passam mais tempo |
| 🚨 Detecção de Furto | Comportamentos suspeitos em tempo real |
| 🏗️ Visualização 3D | Mapa interativo e tridimensional de cada loja |
| 📊 Dashboard Centralizado | Acompanhamento de todas as 40 lojas em uma interface |
| 📱 Alertas em Tempo Real | Notificações imediatas de eventos suspeitos |

---

## 🛠️ Stack Tecnológica

### Backend
- Python 3.11+, FastAPI, OpenCV, YOLOv8, PyTorch
- PostgreSQL, Redis

### Frontend
- React 18, Three.js, React Three Fiber, Tailwind CSS, Vite

### Infraestrutura
- Docker & Docker Compose, Nginx

---

## 📁 Estrutura do Projeto

```
synapse3d/
├── README.md
├── docker-compose.yml
├── .gitignore
├── backend/
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── .env.example
│   ├── main.py
│   └── video_processor.py
├── frontend/
│   ├── Dockerfile
│   ├── nginx.conf
│   ├── package.json
│   ├── vite.config.js
│   ├── index.html
│   └── src/
│       ├── main.jsx
│       ├── index.css
│       ├── App.jsx
│       └── components/
│           ├── StoreMap3D.jsx
│           ├── HeatmapView.jsx
│           └── TheftAlerts.jsx
└── shared/
    ├── models.py
    └── cameras_example.json
```

---

## 🚀 Como Executar

### Pré-requisitos
- Docker e Docker Compose instalados
- Câmeras IP com suporte a RTSP

### 1. Clone o repositório

```bash
git clone https://github.com/edudouraado/synapse3d.git
cd synapse3d
```

### 2. Configure o ambiente

```bash
cp backend/.env.example backend/.env
```

Edite o arquivo `backend/.env` com as configurações das suas câmeras e banco de dados.

### 3. Suba os containers

```bash
docker-compose up -d
```

### 4. Acesse o sistema

| Serviço | URL |
|---------|-----|
| 🖥️ Dashboard | http://localhost:3000 |
| 🔌 API Backend | http://localhost:8000 |
| 📚 Documentação da API | http://localhost:8000/docs |

---

## 📷 Configuração de Câmeras

Edite o arquivo `shared/cameras_example.json` com as informações das suas câmeras:

```json
{
  "cameras": [
    {
      "id": "cam_001",
      "name": "Entrada - Loja Matriz",
      "store_id": "store_001",
      "rtsp_url": "rtsp://usuario:senha@ip_da_camera:554/stream",
      "position_x": 0,
      "position_y": 2.5,
      "position_z": 0,
      "rotation_y": 0
    }
  ],
  "stores": [
    {
      "id": "store_001",
      "name": "Farmácia Matriz",
      "city": "Fortaleza",
      "address": "Av. Principal, 123",
      "floor_plan_url": null,
      "model_3d_url": null
    }
  ]
}
```

### Campos importantes

| Campo | Descrição |
|-------|-----------|
| `rtsp_url` | URL do fluxo de vídeo da câmera (formato RTSP) |
| `position_x, y, z` | Posição da câmera no espaço 3D da loja (em metros) |
| `rotation_y` | Rotação da câmera em graus no eixo Y |
| `store_id` | Identificador da loja a qual a câmera pertence |

---

## 🗺️ Roadmap de Implementação

| Fase | Objetivo | Prazo Estimado |
|------|----------|----------------|
| 1 | Conectar 1-2 lojas piloto e validar detecção | 1-2 semanas |
| 2 | Implementar heatmap de atenção + YOLOv8 | 2-4 semanas |
| 3 | Criar modelos 3D de cada loja | 2-3 semanas |
| 4 | Detecção de comportamento suspeito (furtos) | 3-4 semanas |
| 5 | Escalar para todas as 40 lojas | 1-2 meses |

---

## ⚠️ LGPD e Privacidade

Como o sistema captura imagens de clientes, é essencial seguir a **LGPD (Lei Geral de Proteção de Dados)**:

1. **Sinalização visível**: Afixe placas informando sobre o uso de câmeras e análise de vídeo
2. **Processamento local**: Processe as imagens localmente sempre que possível
3. **Não armazene rostos**: O sistema detecta pessoas, não identifica indivíduos
4. **Retenção de dados**: Defina uma política clara de exclusão de vídeos e imagens
5. **Anonimização**: Considere desfocar rostos nas gravações armazenadas

---

## 🤝 Contribuição

1. Faça um fork do repositório
2. Crie uma branch para sua feature: `git checkout -b feature/minha-feature`
3. Commit suas mudanças: `git commit -m 'feat: adiciona minha feature'`
4. Push para a branch: `git push origin feature/minha-feature`
5. Abra um Pull Request

---

## 📄 Licença

Este projeto é de uso interno da rede de farmácias. Entre em contato para informações sobre licenciamento.

---

Desenvolvido por Eduardo Dourado para SB Farma.
