import pandas as pd

# Leer el archivo CSV
data = pd.read_csv('/content/Child 1 Genome.csv')

# Verificar las primeras filas del DataFrame
print(data.head())

# Supongamos que la columna que contiene la secuencia se llama 'sequence'
genomic_sequence = data['sequence'][0]  # Asegúrate de ajustar el índice según tu DataFrame

# Preprocesar la secuencia (ejemplo)
features = np.array([[len(genomic_sequence)]])

# Normalizar las características
features = scaler.transform(features)

# Hacer la predicción
risk_prediction = model.predict(features)
print(f'Predicción de riesgo: {risk_prediction[0]}')

