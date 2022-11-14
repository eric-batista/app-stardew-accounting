run:
	python3.10 -m uvicorn src.app:app --reload

run-frontend:
	python3.10 -m streamlit run frontend/main.py
