from flask import Flask, render_template, request
from sklearn.linear_model import LinearRegression
import numpy as np

app = Flask(__name__)

# Exemple de dataset
X = np.array([
    [8, 15],  # 8 AM, 15°C
    [12, 20],  # 12 PM, 20°C
    [18, 18],  # 6 PM, 18°C
    [20, 10]   # 8 PM, 10°C
])  
y = np.array([10, 50, 30, 20])  # Nombre de visiteurs

# Entraînement du modèle
model = LinearRegression()
model.fit(X, y)

# Fonction de prédiction
def predict_visitors(time, weather):
    return model.predict(np.array([[time, weather]]))[0]

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = None
    if request.method == 'POST':
        heure = float(request.form['heure'])
        temperature = float(request.form['temperature'])
        prediction = predict_visitors(heure, temperature)
    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000)

