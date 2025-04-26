import pytest
from app import app

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

    # Vérifie que le mot "prédiction :" est présent dans la réponse
    assert 'prédiction :' in response.data.decode()  # Utilisation de .decode() pour convertir en chaîne de caractères
