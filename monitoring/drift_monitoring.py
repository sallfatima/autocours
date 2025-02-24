"""
Module pour la surveillance du drift du modèle.

Ce module analyse les prédictions du modèle et détecte toute déviation par rapport aux distributions attendues.
"""

import numpy as np

def detect_drift(predictions: list, expected_distribution: list) -> bool:
    """
    Compare la distribution des prédictions à celle attendue.

    Args:
        predictions (list): Liste des valeurs de sortie du modèle.
        expected_distribution (list): Distribution de référence.

    Returns:
        bool: True si un drift est détecté, sinon False.
    """
    # Comparaison des moyennes comme indicateur simple.
    if abs(np.mean(predictions) - np.mean(expected_distribution)) > 0.1:
        return True
    return False
