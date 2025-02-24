from typing import Dict, Any
from app.prompts.generate_course import generate_course

def test_generate_course() -> None:
    """
    Teste la fonction de génération de cours pour vérifier qu'elle retourne
    une structure valide avec un titre et des modules non vides.
    """
    subject: str = "Machine Learning"
    course: Dict[str, Any] = generate_course(subject)
    assert "title" in course, "Le cours doit contenir un titre."
    assert course["title"] == "Cours sur Machine Learning", "Le titre doit correspondre au sujet."
    assert isinstance(course["modules"], list), "Les modules doivent être une liste."
    assert len(course["modules"]) > 0, "Il doit y avoir au moins un module."
