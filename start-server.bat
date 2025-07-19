@echo off
echo ========================================
echo    Servidor Web Local - Python
echo ========================================
echo.

echo 🔧 Verificando Python...
py --version

if %errorlevel% neq 0 (
    echo ❌ Python não encontrado!
    echo Verifique se o Python está instalado e configurado.
    pause
    exit /b 1
)

echo ✅ Python encontrado!
echo.
echo 🚀 Iniciando o servidor...
echo.
echo 📁 Diretório atual: %cd%
echo 🌐 URL: http://localhost:8080
echo ⏹️  Para parar: Ctrl+C
echo.

py server.py

pause 