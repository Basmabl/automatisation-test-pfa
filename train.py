from sklearn.linear_model import LinearRegression
import numpy as np

# Example dataset: [time, weather] -> number of visitors
X = np.array([
    [8, 15],  # 8 AM, 15°C
    [12, 20],  # 12 PM, 20°C
    [18, 18],  # 6 PM, 18°C
    [20, 10]   # 8 PM, 10°C
])  
y = np.array([10, 50, 30, 20])  # Number of visitors

# Train the model
model = LinearRegression()
model.fit(X, y)

# Function to make predictions
def predict_visitors(time, weather):
    return model.predict(np.array([[time, weather]]))[0]
heure = float(input("Entrez l'heure (0-23) : "))  # Demande une heure
temperature = float(input("Entrez la température : "))  # Demande une température

resultat = predict_visitors(heure, temperature)  # Prédiction du modèle
print(f"📊 Prédiction du nombre de visiteurs : {resultat:.2f}")  # Affiche le résultat

