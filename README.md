# AutoCours

AutoCours est une application qui génère automatiquement des cours à partir d'un sujet donné, 
enrichie par un module RAG et utilisant un modèle LLM (KingNish/Qwen2.5-0.5b-Test-ft) pour produire du contenu.

## Fonctionnalités

- Interface interactive avec Streamlit (chatbot)
- API REST avec FastAPI
- Génération de cours enrichie avec RAG
- Export en PDF et PowerPoint
- Suivi du modèle avec MLflow et gestion des données avec DVC
- Orchestration via Airflow
- CI/CD avec Jenkins, Ansible et Terraform
- Déploiement avec Docker, Docker Compose et Kubernetes
- Surveillance de la performance et du drift du modèle via Prometheus et Grafana
- Pipeline de fine-tuning automatisé en cas de drift détecté
- Sécurité via JWT/OAuth2

## Installation

1. Cloner le dépôt :
   ```bash
   git clone https://github.com/sallfatima/autocours.git
   cd autocours

2. Installer les dépendances avec Poetry :
    ```bash
    docker-compose up --build

3. Lancer l'application en local avec Docker Compose :
    ```bash

    docker-compose up --build

