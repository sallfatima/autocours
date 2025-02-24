"""
API REST pour AutoCours utilisant FastAPI.
Fournit un endpoint pour générer un cours à partir d'un sujet.
"""

from fastapi import FastAPI, Query
from typing import Dict, Any
from app.prompts.generate_course import generate_course

app = FastAPI(title="AutoCours API")

@app.get("/generate", response_model=Dict[str, Any])
def generate(subject: str = Query(..., description="Sujet du cours à générer")) -> Dict[str, Any]:
    """
    Génère et retourne un cours basé sur le sujet passé en paramètre.

    Args:
        subject (str): Le sujet du cours à générer.

    Returns:
        Dict[str, Any]: Un dictionnaire contenant le cours généré.
    """
    course = generate_course(subject)
    return course

# Pour lancer l'API en local, utilisez par exemple :
# uvicorn app.api:app --reload --port 8000
