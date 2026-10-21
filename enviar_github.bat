@echo off
echo ========================================
echo  CONFIGURANDO GIT E ENVIANDO PARA GITHUB
echo  Projeto: Synapse 3D
echo ========================================
echo.

REM Verificar se estamos na pasta correta
if not exist "docker-compose.yml" (
    echo ERRO: Execute este script dentro da pasta do projeto
    echo (onde esta o arquivo docker-compose.yml)
    pause
    exit /b 1
)

echo [1/6] Configurando identidade do Git...
git config user.name "Eduardo"
git config user.email "edudouraado@users.noreply.github.com"

echo [2/6] Adicionando repositorio remoto...
git remote remove origin 2>nul
git remote add origin https://github.com/edudouraado/synapse3d.git

echo [3/6] Renomeando branch para main...
git branch -M main

echo [4/6] Adicionando todos os arquivos...
git add .

echo [5/6] Fazendo commit...
git commit -m "feat: inicializar projeto Synapse 3D - sistema de visao computacional para farmacias"

echo [6/6] Enviando para o GitHub...
git push -u origin main

echo.
echo ========================================
echo  CONCLUIDO!
echo  Seu projeto esta em:
echo  https://github.com/edudouraado/synapse3d
echo ========================================
pause
