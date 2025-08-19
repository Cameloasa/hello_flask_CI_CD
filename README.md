# Hello Flask CI/CD

## Prerequisites

* Python 3.13
* Git
* GitHub repository for CI/CD

## Setup Instructions

### 1. Clone the repository

```bash
git clone <repo-url>
cd hello_flask_CI_CD
```

### 2. Create and activate a virtual environment

**Windows:**

```powershell
python -m venv .venv
.venv\Scripts\activate
```

**macOS/Linux:**

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Flask application

```bash
python app/main.py
```

Access the app at: [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Running Tests

### Unit tests

```bash
python -m pytest tests/
```

### BDD tests

```bash
behave features/
```

## CI/CD Pipeline

* GitHub Actions workflow: `.github/workflows/ci.yml`
* Triggers: `push` and `pull_request` events on `main`
* Steps:

  1. Set up Python 3.13 on Ubuntu
  2. Install dependencies
  3. Run unit tests with pytest
  4. Run BDD tests with behave
* View workflow logs in GitHub Actions tab

## Development Notes

* Flask app: `app/main.py` (add routes/features as needed)
* Unit tests: `tests/test_main.py`
* BDD tests: `features/` (step definitions: `features/steps/`)
* Dependencies: `requirements.txt` (update with `pip freeze > requirements.txt` after installing new packages)
* Optional: Add `static/favicon.ico` to avoid 404 for favicon

## Troubleshooting

* File not found: check `app/main.py`
* Dependency issues: verify packages in `requirements.txt`
* Pipeline failures: see GitHub Actions logs

## Future Improvements

* Deployment steps in CI/CD (Heroku, Vercel)
* Code linting (flake8)
* More comprehensive unit and BDD tests
