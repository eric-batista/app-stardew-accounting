format:
	@poetry run isort src
	@poetry run black src
	@poetry run autoflake --in-place --remove-unused-variables --remove-all-unused-imports src

run:
	python3.10 -m uvicorn src.app:app --reload

run-frontend:
	python3.10 -m streamlit run frontend/main.py
