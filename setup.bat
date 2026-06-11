@echo off
echo === ResearchMind Setup ===
echo.

python -m venv venv
call venv\Scripts\activate

pip install -r requirements.txt

if not exist .env (
    copy .env.example .env
    echo.
    echo *** IMPORTANT: Open .env and paste your GROQ_API_KEY ***
    echo *** Get a free key at https://console.groq.com ***
    echo.
)

echo.
echo Setup complete! Now:
echo 1. Edit .env and add your GROQ_API_KEY
echo 2. Run:  venv\Scripts\activate
echo 3. Run:  python -m streamlit run app.py
pause
