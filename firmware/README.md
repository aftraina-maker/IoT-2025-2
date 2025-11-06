# Firmware
Roteiro:
- Coloque aqui o código do dispositivo (ex.: ESP32/Arduino).  
- Documente dependências (bibliotecas) e como compilar/gravar.

===============================================================================================================================

# 🐔 Aviário IoT Web – Monitoramento Ambiental com Node.js, React e Docker

Aplicação web para **monitoramento e automação de aviários**, integrando sensores IoT via MQTT.  
O sistema é dividido em **frontend (React)**, **backend (Node.js + Express)**, **banco de dados PostgreSQL**, e **broker MQTT (Mosquitto)** — todos orquestrados via **Docker Compose**.
Há ainda alguns arquivos relacionados à dependências.

---

## 📂 Estrutura de Pastas do Projeto

```bash
aviario-iot-web/
│
├── backend/                   # API REST e integração MQTT
│   ├── server.js              # Servidor Express principal
│   ├── db.js                  # Conexão e operações com PostgreSQL
│   ├── mqttHandler.js         # Comunicação com o broker MQTT
│   ├── package.json           # Dependências e scripts do backend
│   └── Dockerfile             # Configuração do container backend
│
├── frontend/                  # Interface web (React + Vite)
│   ├── src/                   # Códigos-fonte da interface
│   ├── package.json           # Dependências e scripts do frontend
│   └── Dockerfile             # Configuração do container frontend
│
├── mosquitto/                 # Configuração do broker MQTT
│   └── config/
│       └── mosquitto.conf     # Arquivo de configuração do Mosquitto
│
├── docker-compose.yml         # Orquestração dos containers
└── .env                       # Variáveis de ambiente do projeto
