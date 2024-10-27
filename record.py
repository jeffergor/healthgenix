import pandas as pd
import numpy as np

# Leer el archivo CSV
data = pd.read_csv('/content/Child 1 Genome.csv')

# Imprimir los nombres de las columnas
print(data.columns)

# Verificar el contenido del DataFrame
print(data.head())

# Si hay una columna con la secuencia, asegúrate de cambiar el nombre de la columna si es necesario.
# Aquí se asume que tienes una columna llamada 'sequence' (ajusta esto según tus datos).
genomic_sequence = data['genotype'].values  # Cambiar a la columna que contiene la información relevante

# Definición de la clase CRISPRSimulator
class CRISPRSimulator:
    def __init__(self, sequence):
        self.sequence = sequence

    def simulate_edit(self, gRNA):
        # Simular la eliminación de la secuencia gRNA
        if gRNA in self.sequence:
            self.sequence = self.sequence.replace(gRNA, '')
            return True
        return False

# Crear una instancia del simulador usando la primera secuencia del DataFrame
simulador = CRISPRSimulator(''.join(genomic_sequence))  # Convertir a string si es necesario

# Definir el gRNA
gRNA = 'AGGCTAGCTAG'  # Cambia esto según tus necesidades

# Simular la edición
if simulador.simulate_edit(gRNA):
    print('Edición CRISPR realizada con éxito.')
else:
    print('No se pudo realizar la edición CRISPR.')
