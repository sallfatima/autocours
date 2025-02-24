import json
import os
from typing import Dict

def load_secrets(file_path: str = "app/secrets/config.json") -> Dict[str, str]:
    """
    Charge les secrets depuis un fichier JSON.

    Args:
        file_path (str): Chemin du fichier de configuration des secrets.

    Returns:
        Dict[str, str]: Dictionnaire contenant les secrets.

    Raises:
        FileNotFoundError: Si le fichier de configuration n'existe pas.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Le fichier de secrets n'existe pas: {file_path}")
    with open(file_path, "r", encoding="utf-8") as f:
        secrets = json.load(f)
    return secrets
