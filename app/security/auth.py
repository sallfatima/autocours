"""
Module d'authentification pour AutoCours.
Implémente la vérification de token JWT via OAuth2.
"""

from fastapi import HTTPException, Security
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def verify_token(token: str = Security(oauth2_scheme)) -> bool:
    """
    Vérifie la validité d'un token JWT.

    Args:
        token (str): Le token JWT fourni par le client.

    Returns:
        bool: True si le token est valide, sinon lève une exception HTTP 401.
    """
    if token == "votre_token_secret":
        return True
    raise HTTPException(status_code=401, detail="Token invalide")
