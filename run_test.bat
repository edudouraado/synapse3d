@echo off
echo ========================================
echo  SYNAPSE 3D - TESTE DA CAMERA
echo ========================================
echo.

if not exist "backend\venv" (
    echo ERRO: Execute primeiro o setup_and_run.bat
    pause
    exit /b 1
)

cd backend
call venv\Scripts\activate
python ..\test_camera.py
cd ..
pause
