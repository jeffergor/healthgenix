import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

# Cargar los datos
data = pd.read_csv('C:\Users\User\OneDrive\Documentos\projecto 006\Cancer_Rates.csv')

# Separar las características (X) y la etiqueta (y)
X = data.drop(columns=['Breast_Can'])  # Cambia 'Breast_Can' según sea necesario
umbral = 0.5  # Ajusta según sea necesario
y = (data['Breast_Can'] > umbral).astype(int)  # Convertir a categórico

# Dividir los datos
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalizar los datos
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Crear y entrenar el modelo
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Evaluar el modelo
accuracy = model.score(X_test, y_test)
print(f'Precisión del modelo: {accuracy:.2f}')

# Graficar la precisión
sns.barplot(x=['Modelo'], y=[accuracy])
plt.title('Precisión del Modelo de Predicción de Cáncer')
plt.ylim(0, 1)
plt.ylabel('Precisión')
plt.show()
