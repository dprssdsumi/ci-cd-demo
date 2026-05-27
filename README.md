# CI/CD Demo — Flask + GitHub Actions + Docker

A simple Python Flask REST API with a full CI/CD pipeline using GitHub Actions and Docker.

## What the pipeline does

Every time you push to `main`, GitHub Actions automatically:
1. Spins up a fresh Ubuntu environment
2. Installs Python dependencies
3. Runs all pytest tests
4. Reports ✅ pass or ❌ fail

## Project Structure
```
ci-cd-demo/
├── app/
│   └── main.py              # Flask app (4 endpoints)
├── tests/
│   └── test_app.py          # 6 pytest tests
├── .github/
│   └── workflows/
│       └── ci.yml           # GitHub Actions pipeline
├── Dockerfile               # Container definition
├── requirements.txt
└── .gitignore
```

## API Endpoints
| Endpoint | Description | Example |
|----------|-------------|---------|
| `GET /` | Status check | `{"status": "running"}` |
| `GET /health` | Health check | `{"status": "healthy"}` |
| `GET /add/<a>/<b>` | Add two numbers | `/add/3/7` → `{"result": 10}` |
| `GET /reverse/<text>` | Reverse a string | `/reverse/hello` → `{"result": "olleh"}` |

## Run locally with Docker
```bash
# Build the image
docker build -t ci-cd-demo .

# Run the container
docker run -p 5000:5000 ci-cd-demo

# Visit http://localhost:5000
```

## Run tests locally
```bash
pip install -r requirements.txt
pytest tests/ -v
```

## Run tests output example
```
tests/test_app.py::test_home              PASSED
tests/test_app.py::test_health            PASSED
tests/test_app.py::test_add               PASSED
tests/test_app.py::test_add_negatives     PASSED
tests/test_app.py::test_reverse           PASSED
tests/test_app.py::test_reverse_single_char PASSED

6 passed in 0.21s
```
