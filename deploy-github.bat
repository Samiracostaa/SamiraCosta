@echo off
echo ========================================
echo    Deploy no GitHub Pages
echo ========================================
echo.

echo 🔧 Verificando Git...
git --version

if %errorlevel% neq 0 (
    echo ❌ Git não encontrado!
    echo Baixe e instale o Git: https://git-scm.com/
    pause
    exit /b 1
)

echo ✅ Git encontrado!
echo.

echo 📁 Inicializando repositório Git...
git init

echo 📝 Adicionando arquivos...
git add .

echo 💾 Fazendo commit...
git commit -m "Primeiro commit - Portfólio Samira"

echo 🌿 Configurando branch main...
git branch -M main

echo.
echo 🔗 Agora você precisa conectar ao GitHub:
echo.
echo 1. Vá para https://github.com
echo 2. Crie um repositório chamado: portfolio-samira
echo 3. Copie a URL do repositório
echo 4. Cole aqui quando solicitado
echo.

set /p REPO_URL="Cole a URL do repositório (ex: https://github.com/SEU_USUARIO/portfolio-samira.git): "

echo.
echo 🔗 Conectando ao GitHub...
git remote add origin %REPO_URL%

echo 🚀 Enviando para o GitHub...
git push -u origin main

echo.
echo ✅ Arquivos enviados com sucesso!
echo.
echo 🌐 Agora configure o GitHub Pages:
echo 1. Vá para o repositório no GitHub
echo 2. Settings → Pages
echo 3. Source: Deploy from a branch
echo 4. Branch: main
echo 5. Folder: / (root)
echo 6. Save
echo.
echo 🔗 Sua URL será: https://SEU_USUARIO.github.io/portfolio-samira
echo.

pause 