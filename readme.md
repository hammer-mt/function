# FUNCTION TEMPLATE
This is a template to use for Google Cloud Functions in Python.

## How to use

To create a new environment
- `python -m venv venv`
- `echo FOO: bar > .env.yaml`

If you install anything
- `pip install some_library`
- `pip freeze > requirements.txt`

To run for testing
- `venv\Scripts\activate`
- `pytest -v -s`
- `python main.py`

When finished testing
- `CTRL + C`
- `deactivate`
- `git add .`
- `git push`

To deploy to production
- `gcloud beta functions deploy function-name --trigger-http --runtime python37 --project project-name-1234 --allow-unauthenticated --entry-point=main --env-vars-file .env.yaml`