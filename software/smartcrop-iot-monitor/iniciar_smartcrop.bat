@echo off
echo ===========================================
echo  🚀 Iniciando SmartCrop IoT Monitor...
echo ===========================================

cd /d C:\smartcrop-iot-monitor

echo.
echo 🐳 Subindo containers (API, Grafana e Simulador)...
docker-compose up -d

echo.
echo 🔍 Verificando status:
docker ps

echo.
echo ✅ Ambiente SmartCrop IoT ativo!
echo 🌐 Grafana:  http://localhost:3001
echo 🌐 API:      http://localhost:5000/api/dados
pause
