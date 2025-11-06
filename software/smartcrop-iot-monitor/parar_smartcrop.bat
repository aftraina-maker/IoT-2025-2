@echo off
echo ===========================================
echo  🚫 Encerrando SmartCrop IoT Monitor...
echo ===========================================

cd /d C:\smartcrop-iot-monitor

echo.
echo 🧩 Parando containers...
docker-compose down

echo.
echo 🧹 Limpando containers antigos...
docker container prune -f

echo.
echo ✅ Todos os serviços foram parados com segurança!
pause
