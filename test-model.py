# test_model.py

import pytest
from app import predict_visitors  # Importation directe de la fonction depuis app.py
from unittest.mock import patch

def test_predict_visitors():
    # Simulation des entrées utilisateur
    with patch('builtins.input', side_effect=[12, 20]):  # Simule '12' pour l'heure et '20' pour la température
        time = float(input())  # Simule l'entrée de l'heure
        weather = float(input())  # Simule l'entrée de la température
        result = predict_visitors(time, weather)  # Appel de la fonction de prédiction
        print(f"Prédiction du modèle : {result}")
        assert result > 30 and result < 60  # Vérifie que la prédiction est dans l'intervalle attendu

