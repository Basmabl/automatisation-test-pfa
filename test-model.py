# test_app.py

import pytest
from app import predict_visitors

# Test de la fonction predict_visitors
def test_predict_visitors():
    # Cas de test avec des entrées simples
    time = 12  # 12h
    weather = 20  # 20°C
    prediction = predict_visitors(time, weather)

    # Vérifie que la prédiction est un nombre
    assert isinstance(prediction, (float, int))

    # Vérifie que la prédiction est dans un intervalle logique
    assert 10 < prediction < 50
