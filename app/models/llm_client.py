"""
Client pour interagir avec le modèle de langage Hugging Face et enregistrer les métriques avec MLflow.
"""

from typing import Any
import os
import mlflow
from transformers import AutoTokenizer, AutoModelForCausalLM
from app.secrets_manager import load_secrets


class LLMClient:
    """
    Client LLM qui se charge d'appeler le modèle et de logguer les paramètres
    et métriques associés via MLflow.

    Respecte le principe de responsabilité unique.
    """

    def __init__(self) -> None:
        self.model_name: str = "KingNish/Qwen2.5-0.5b-Test-ft"
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModelForCausalLM.from_pretrained(self.model_name)
        self.api_key: str = load_secrets().get("LLM_API_KEY", "votre_api_key")
        self.api_url: str = load_secrets().get("LLM_API_URL", "https://api.example.com/generate")


    def generate_text(self, prompt: str, max_length: int = 100) -> str:
        """
        Génère du texte à partir d'un prompt en utilisant le modèle.

        Args:
            prompt (str): Le prompt de génération.
            max_length (int, optional): Longueur maximale du texte généré. Par défaut 100.

        Returns:
            str: Le texte généré.
        """
        input_ids = self.tokenizer.encode(prompt, return_tensors="pt")
        output_ids = self.model.generate(input_ids, max_length=max_length, do_sample=True)
        text: str = self.tokenizer.decode(output_ids[0], skip_special_tokens=True)
        
        # Enregistrement avec MLflow.
        mlflow.log_param("prompt", prompt)
        mlflow.log_metric("output_length", len(text))
        
        return text
