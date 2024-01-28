from api_client import get
import pandas as pd
import requests

'''
racine_api = 'http://127.0.0.1:8000'


Modèles utilisés:
- 'optimal_rfr_model.pkl' : Modèle de Régression par Forêt aléatoire.
- 'optimal_linear_regression_model.pkl' : Modèle de Régression Linéaire.

Endpoints API:
1. `/prix_m2`: Prédiction du prix au mètre carré en fonction de la longitude et la latitude.
2. `/prix_m2_two`: Prédiction du prix au mètre carré en fonction du nombre de pièces, de la surface habitable, du prix au mètre carré, du code postal, de la longitude et la latitude.

'''

import pickle
from fastapi import FastAPI, HTTPException
import uvicorn


# Fonction pour effectuer une prédiction avec deux features (n_pieces, surface_habitable, prix_m2, code_postal, longitude, latitude)
def predict_two(model, n_pieces, surface_habitable, prix_m2, code_postal, longitude, latitude):
    if model is None:
        raise HTTPException(status_code=503, detail="Modèle non chargé")
    input_data = [[n_pieces, surface_habitable, prix_m2, code_postal, longitude, latitude]]
    return model.predict(input_data)[0]


# Route pour effectuer la prédiction du prix au mètre carré en fonction de la longitude et la latitude
def prix_m2(longitude: float, latitude: float):
    # Chargement du modèle à chaque appel
    loaded_model = load_model('optimal_rfr_model.pkl')
    
    # Vérification du chargement du modèle
    if loaded_model is None:
        raise HTTPException(status_code=503, detail="Modèle non chargé")

    # Prédiction
    prediction = predict(loaded_model, longitude, latitude)
    return {'predicted_prix_m2': prediction}
    

# Route pour effectuer la prédiction du prix au mètre carré en fonction de plusieurs features
def prix_m2_two(n_pieces: int, surface_habitable: float, prix_m2: float, code_postal: int, longitude: float, latitude: float):
    # Chargement du modèle à chaque appel
    loaded_model = load_model('optimal_linear_regression_model.pkl')
    
    # Vérification du chargement du modèle
    if loaded_model is None:
        raise HTTPException(status_code=503, detail="Modèle non chargé")

    # Prédiction
    prediction = predict_two(loaded_model, n_pieces, surface_habitable, prix_m2, code_postal, longitude, latitude)
    
    return {'predicted_prix_m2': prediction}


