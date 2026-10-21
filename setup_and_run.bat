@echo off
echo ========================================
echo  SYNAPSE 3D - CONFIGURACAO E EXECUCAO
echo  Projeto: Visao Computacional para Farmacias
echo ========================================
echo.

REM Verificar se estamos na pasta correta
if not exist "backend\main.py" (
    echo ERRO: Execute este script dentro da pasta C:\github\synapse3d
    echo (onde esta a pasta backend)
    pause
    exit /b 1
)

echo [1/5] Verificando Python...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERRO: Python nao encontrado ou nao esta no PATH.
    echo Instale o Python em https://www.python.org/ e marque "Add Python to PATH"
    pause
    exit /b 1
)

echo [2/5] Criando ambiente virtual (se nao existir)...
cd backend
if not exist "venv" (
    python -m venv venv
    if %errorlevel% neq 0 (
        echo ERRO: Falha ao criar ambiente virtual
        cd ..
        pause
        exit /b 1
    )
)

echo [3/5] Instalando dependencias (pode demorar alguns minutos)...
call venv\Scripts\activate
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo ERRO: Falha ao instalar dependencias
    cd ..
    pause
    exit /b 1
)

echo [4/5] Copiando arquivo de variaveis de ambiente...
if not exist ".env" (
    copy .env.example .env
)

echo [5/5] Iniciando API Synapse 3D...
echo.
echo ========================================
echo  API rodando em: http://localhost:8000
echo  Documentacao: http://localhost:8000/docs
echo  Pressione Ctrl+C para parar
echo ========================================
echo.
python main.py

cd ..
pause
