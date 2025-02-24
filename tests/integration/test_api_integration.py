import requests

def test_api_generate() -> None:
    """
    Test d'intégration pour vérifier le flux complet via l'API FastAPI.
    Ce test nécessite que le serveur soit lancé sur localhost:8000.
    """
    response = requests.get("http://localhost:8000/generate", params={"subject": "Data Science"})
    assert response.status_code == 200, "L'API doit renvoyer un code 200."
    data = response.json()
    assert "title" in data, "La réponse doit contenir un titre."
    assert "modules" in data, "La réponse doit contenir des modules."
