import pytest
from train import predict_visitors
from unittest.mock import patch  # Pour patcher input()

def test_predict_visitors():
    # Patch l'input pour simuler les entrées utilisateur
    with patch('builtins.input', side_effect=['12', '20']):  # Heure et température simulées
        time = int(input())  # Récupérer l'heure simulée
        weather = int(input())  # Récupérer la température simulée
        result = predict_visitors(time, weather)  # Passer les arguments à la fonction
        print(f"Prédiction du modèle : {result}")
        assert result > 30 and result < 60  # Vérifier que le nombre de visiteurs est dans la plage attendue
