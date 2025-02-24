"""
Script de suivi MLflow pour AutoCours.
Log le modèle et une sortie générée afin d'assurer le suivi des expérimentations.
"""

import mlflow
from app.models.llm_client import LLMClient

def log_model() -> None:
    """
    Log le modèle et la sortie générée via MLflow.
    """
    mlflow.set_experiment("AutoCours Model Logging")
    with mlflow.start_run():
        client = LLMClient()
        prompt = "Exemple de prompt pour tester le modèle."
        output = client.generate_text(prompt)
        mlflow.log_text(output, "generated_text.txt")
        mlflow.log_param("model_name", client.model_name)
        print("Modèle et sortie loggés avec MLflow.")

if __name__ == '__main__':
    log_model()
