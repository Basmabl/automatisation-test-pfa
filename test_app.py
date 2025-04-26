import pytest
from app import app, predict_visitors

def test_predict_visitors():
    X_train = [[1], [2], [3]]
    y_train = [2, 4, 6]
    prediction = predict_visitors(X_train, y_train, 4)
    assert prediction == 8

def test_home_route_get():
    tester = app.test_client()
    response = tester.get('/')
    assert response.status_code == 200
    assert b"Prediction" in response.data  # Vérifie que le mot Prediction est dans le HTML

def test_home_route_post():
    tester = app.test_client()
    response = tester.post('/', data={'month': '5'})
    assert response.status_code == 200
    assert b"Predicted visitors:" in response.data  # Le texte que tu affiches après prédiction


def test_home_route_get():
    tester = app.test_client()
    response = tester.get('/')
    assert response.status_code == 200
    assert b"Prediction" in response.data  # Vérifie que le mot Prediction est dans le HTML

def test_home_route_post():
    tester = app.test_client()
    response = tester.post('/', data={'month': '5'})
    assert response.status_code == 200
    assert b"Predicted visitors:" in response.data  # Le texte que tu affiches après prédiction
