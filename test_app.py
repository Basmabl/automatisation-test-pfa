# test_app.py

import pytest
from app import app, predict_visitors

# Test de la fonction predict_visitors
def test_predict_visitors():
    time = 12
    weather = 20
    prediction = predict_visitors(time, weather)
    assert isinstance(prediction, (float, int))
    assert 10 < prediction < 50

# Test de la route Flask '/'
@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home_route_post(client):
    data = {
        'heure': 12.0,
        'temperature': 20.0
    }
    response = client.post('/', data=data)
    assert response.status_code == 200
    assert b'Prediction' in response.data  # Assure-toi que la prédiction apparaît dans la page HTML

def test_home_route_get(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Prediction' not in response.data  # Pas de prédiction sur la page d'accueil par défaut

# Test de comportement avec des entrées invalides
def test_predict_visitors_invalid():
    with pytest.raises(ValueError):
        predict_visitors('invalid_time', 'invalid_temp')  # Devrait échouer pour des entrées non numériques
