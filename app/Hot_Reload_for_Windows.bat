@echo off
chcp 65001 >nul
cd /d "%~dp0"

:: 1. 가상환경 활성화
if exist ".venv\Scripts\activate.bat" (
    call .venv\Scripts\activate
) else (
    echo ❌ Error: .venv not found.
    pause
    exit /b
)

echo ---------------------------------------------------
:: 특수기호 '&'를 빼고 안전한 문장으로 변경했습니다.
echo 🚀 Flet Hot Reload (Web Mode) Start!
echo [Web Mode] http://localhost:34636
echo ---------------------------------------------------

:: 2. Flet 내장 명령어로 핫리로드 및 웹서버 실행
:: --web: 웹 브라우저 모드로 실행
:: --port: 포트 번호 고정
:: -d: 디렉토리(폴더) 변경 감지 (핫리로드)
flet run --web --port 34636 -d main.py

pause