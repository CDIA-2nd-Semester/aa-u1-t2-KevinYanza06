# Tema: Evaluación de Autos
# Nombre: Kevin Yanza
# Fecha: 06/07/2025
# Asignatura: Programación 2 - Actividad Autónoma 6
# Dataset: Car Evaluation


# 1. Importación de librerías

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report


# 2. Cargar dataset

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/car/car.data"
columnas = ['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety', 'class']
df = pd.read_csv(url, names=columnas)

# Mostrar las primeras filas
print("Primeras filas del dataset:")
print(df.head())


# 3. Verificar valores nulos

print("\nValores nulos por columna:")
print(df.isnull().sum())


# 4. Codificación de variables categóricas

df_encoded = df.apply(LabelEncoder().fit_transform)
print("\nDatos codificados:")
print(df_encoded.head())


# 5. Visualización exploratoria

sns.countplot(x='class', data=df)
plt.title('Distribución de Clases')
plt.xlabel('Clase del auto')
plt.ylabel('Frecuencia')
plt.show()


# 6. División en entrenamiento y prueba

X = df_encoded.drop('class', axis=1)
y = df_encoded['class']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# 7. Modelo 1: Regresión Logística

lr = LogisticRegression(max_iter=200)
lr.fit(X_train, y_train)
pred_lr = lr.predict(X_test)

# 8. Modelo 2: Árbol de Decisión

dt = DecisionTreeClassifier()
dt.fit(X_train, y_train)
pred_dt = dt.predict(X_test)


# 9. Evaluación de modelos

print("\n--- Regresión Logística ---")
print("Accuracy:", accuracy_score(y_test, pred_lr))
print(classification_report(y_test, pred_lr))

print("\n--- Árbol de Decisión ---")
print("Accuracy:", accuracy_score(y_test, pred_dt))
print(classification_report(y_test, pred_dt))
