format:
	@poetry run isort src
	@poetry run black src
	@poetry run autoflake --in-place --remove-unused-variables --remove-all-unused-imports src

run-backend:
	@poetry run uvicorn src.app:app --reload

run-frontend:
	@poetry run streamlit run frontend/main.py
