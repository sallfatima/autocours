"""
Module de génération de cours pour AutoCours.
Utilise le module RAG pour enrichir le prompt de génération.
"""

from typing import Dict, Any
from app.rag.rag_client import RAGClient

def generate_course(subject: str) -> Dict[str, Any]:
    """
    Génère le contenu d'un cours en enrichissant le prompt avec du contexte via RAG.

    Args:
        subject (str): Le sujet du cours.

    Returns:
        Dict[str, Any]: Un dictionnaire contenant le titre et la liste des modules du cours.
    """
    # Récupérer le contexte pertinent via le module RAG.
    rag_client = RAGClient()
    context_list = rag_client.retrieve_context(subject)
    context: str = " ".join(context_list)
    
    # Construction du prompt enrichi.
    prompt: str = (
        f"Génère un cours détaillé sur '{subject}' en intégrant le contexte suivant : {context}"
    )
    
    # Simulation de génération de cours.
    course: Dict[str, Any] = {
        "title": f"Cours sur {subject}",
        "modules": [
            {"title": "Introduction", "content": f"Introduction au {subject}. Contexte : {context}"},
            {"title": "Contenu principal", "content": f"Développement détaillé sur {subject} en utilisant le contexte : {context}"},
            {"title": "Conclusion", "content": f"Résumé et conclusion sur {subject}."}
        ]
    }
    return course
