import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier  # O RandomForestRegressor según lo que necesites

# Cargar los datos
data = pd.read_csv('C:\Users\User\OneDrive\Documentos\projecto 006\Cancer_Rates.csv')

# Ver las primeras filas del DataFrame para entender su estructura
print(data.head())
print(data.columns)  # Verificar las columnas del DataFrame

# Separar las características (X) y la etiqueta (y)
X = data.drop(columns=['Breast_Can'])  # Cambia 'Breast_Can' según sea necesario

# Opción 1: Para clasificación
# Convertir la variable continua a categórica
umbral = 0.5  # Ajusta según sea necesario
y = (data['Breast_Can'] > umbral).astype(int)  # 1 si > umbral, 0 si <= umbral

# Opción 2: Para regresión
# y = data['Breast_Can']  # Mantener como continuo si eliges regresión

# Dividir los datos
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalizar los datos
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Crear el modelo de predicción
model = RandomForestClassifier()  # O RandomForestRegressor si usas regresión
model.fit(X_train, y_train)

# Evaluar el modelo
accuracy = model.score(X_test, y_test)  # Cambia esto a score para regresión
print(f'Precisión del modelo: {accuracy:.2f}')
