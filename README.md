Prerequisites

Python 3.13
Git

A GitHub repository for CI/CD

Setup Instructions

Clone the repository:

git clone <your-repository-url>
cd hello_flask_CI_CD



Create and activate a virtual environment:

python -m venv .venv
.venv\Scripts\activate  # On Windows
# source .venv/bin/activate  # On macOS/Linux



Install dependencies:

pip install -r requirements.txt



Run the Flask application:

python app/main.py

The app will be available at http://127.0.0.1:5000.



Run unit tests:

python -m pytest tests/



Run BDD tests:

behave features/

CI/CD Pipeline

The project uses GitHub Actions for CI/CD, defined in .github/workflows/ci.yml. The pipeline:





Triggers on push and pull_request events to the main branch.



Sets up Python 3.13 on an Ubuntu environment.



Installs dependencies from requirements.txt.



Runs unit tests with pytest.



Runs BDD tests with behave.

To check the pipeline:





Push changes to your GitHub repository.



View the workflow logs in the "Actions" tab of your repository.

Development Notes





Flask: The app is defined in app/main.py. Add new routes and features as needed.



Unit Tests: Located in tests/test_main.py. Use pytest for testing.



BDD Tests: Feature files are in features/, with step definitions in features/steps/. Use behave for BDD testing.



Dependencies: Managed in requirements.txt. Update with pip freeze > requirements.txt after installing new packages.



Favicon: The app may return a 404 for favicon.ico. Add a static/favicon.ico file to resolve this.

Troubleshooting





File not found errors: Ensure app/main.py exists and is referenced correctly in commands.



Dependency issues: Verify all required packages (e.g., Flask, pytest, behave) are in requirements.txt.



Pipeline failures: Check GitHub Actions logs for detailed error messages.

Future Improvements





Add deployment steps to the CI/CD pipeline (e.g., deploy to Heroku or Vercel).



Include code linting (e.g., flake8) in the pipeline.



Add more comprehensive unit and BDD tests.