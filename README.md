# devsecops-pipeline-automation
Automated DevSecOps pipeline: CI/CD, SAST (Semgrep/Bandit/CodeQL), DAST (OWASP ZAP), Gitleaks secret scanning, Docker image scanning, Kubernetes manifest validation."

devsecops-pipeline-automation/
├── README.md
├── .gitignore
├── app/
│   ├── main.py
│   ├── requirements.txt
│   └── tests/
│       └── test_main.py
├── docker/
│   ├── Dockerfile
│   └── .dockerignore
├── k8s/
│   ├── deployment.yaml
│   ├── service.yaml
│   └── kustomization.yaml
├── scripts/
│   └── ci-check.sh
├── docs/
│   └── 01-pipeline-architecture.md
└── .github/
    ├── dependabot.yml
    └── workflows/
        ├── ci.yml                # build + unit tests
        ├── sast-pipeline.yml     # gitleaks + semgrep + bandit + trivy + codeql
        ├── dast-pipeline.yml     # ZAP
        └── container-k8s-scan.yml
