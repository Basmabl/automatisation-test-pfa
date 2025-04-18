import pytest
from train import predict_visitors  # Import your function

def test_predict_visitors():
    result = predict_visitors(12, 20) 
    print(f"Prédiction du modèle : {result}")  # Noon, 20°C
     
    assert result > 30 and result < 60  # Expected visitors around 50
