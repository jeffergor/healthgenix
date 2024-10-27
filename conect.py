from flask import Flask, render_template, request, redirect, url_for
import numpy as np
import pandas as pd
# Asegúrate de que tu archivo de modelo esté en el mismo directorio
from my_model import model, scaler  # Cambia esto según el nombre real de tu archivo y objeto

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Obtener la secuencia genómica desde el formulario
    genomic_sequence = request.form['genomic_sequence']
    
    # Preprocesar la secuencia para hacer la predicción
    features = np.array([[len(genomic_sequence)]])  # Ejemplo simple
    features = scaler.transform(features)  # Normalizar características
    
    # Hacer la predicción
    risk_prediction = model.predict(features)[0]
    
    # Redirigir a la página de resultados con la predicción
    return render_template('result.html', prediction=risk_prediction)

if __name__ == '__main__':
    app.run(debug=True)
