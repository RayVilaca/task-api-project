# Task API Project

[![CI](https://github.com/RayVilaca/task-api-project/actions/workflows/ci.yml/badge.svg)](https://github.com/RayVilaca/task-api-project/actions/workflows/ci.yml)  [![Integration Tests](https://github.com/RayVilaca/task-api-project/actions/workflows/integration-tests.yml/badge.svg)](https://github.com/RayVilaca/task-api-project/actions/workflows/integration-tests.yml)  [![Security](https://github.com/RayVilaca/task-api-project/actions/workflows/security.yml/badge.svg)](https://github.com/RayVilaca/task-api-project/actions/workflows/security.yml)  [![Docker Publish](https://github.com/RayVilaca/task-api-project/actions/workflows/docker-publish.yml/badge.svg)](https://github.com/RayVilaca/task-api-project/actions/workflows/docker-publish.yml)  [![codecov](https://codecov.io/gh/RayVilaca/task-api-project/branch/main/graph/badge.svg)](https://codecov.io/gh/RayVilaca/task-api-project)

---

## 📌 Overview
Task API Project is a **Flask-based backend service** for task management.  
It is containerized with **Docker Compose** and integrated with CI/CD pipelines, security scans, and unit test coverage validation.

---

## 🏗️ Project Architecture
```
task-api-project/
├── .github/
│ └── workflows/
|   ├── ci.yml
|   ├── docker-publish.yml
|   ├── integration-tests.yml
|   └── security.yml
├── task-api/
│ ├── app.py
│ ├── models/
│ ├── routes/
│ └── schemas/
├── tests/
│ ├── unit/
│ ├── integration/
│ └── conftest.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```


---

## ⚙️ Features
- ✅ **Flask REST API** for task management  
- ✅ Unit test coverage >80%  
- ✅ CI with GitHub Actions  
- ✅ Vulnerability scanning using **Trivy**  
- ✅ Containerized with **Docker Compose**  

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- Docker

### Installation
```bash
git clone https://github.com/RayVilaca/task-api-project.git
cd task-api-project
pip install -r requirements.txt
```

### Run with Docker compose
```bash
docker compose up -d
```

### 🧪 Running Tests
```bash
pytest --cov=app tests/
```

---

## 🔐 Security

- ✅ Automated scans using Trivy
- ✅ Checks for HIGH and CRITICAL vulnerabilities only
- ✅ Option to ignore unfixed vulnerabilities

---

## 📈 CI/CD

This project uses GitHub Actions for:
- ✅ Build & test automation
- ✅ Security scanning
- ✅ Coverage reporting
- ✅ Docker image builds (for CD)
