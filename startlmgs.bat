REM Start Streamlit app
start cmd /k streamlit run app.py

echo Application Starting....
REM Wait a few seconds for Streamlit to start
timeout /t 5 > nul

REM Open browser to Streamlit URL
start http://localhost:8501