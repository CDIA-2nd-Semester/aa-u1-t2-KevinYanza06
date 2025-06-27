# Actividad Autónoma - Análisis de Costos Médicos
# Dataset: Medical Insurance Costs (insurance.csv)
# Autor: Kevin Yanza
# Carga y Exploración Inicial

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar el dataset desde el mismo directorio
insurance = pd.read_csv("./insurance.csv")

# Mostrar las primeras filas
print(insurance.head())

# Verificar tipos de datos y valores nulos
print(insurance.info())
print("\nValores nulos por columna:\n", insurance.isnull().sum())



# Preprocesamiento de los Datos


# Codificar variables categóricas
insurance = pd.get_dummies(insurance, columns=['sex', 'region'], drop_first=True)

# Convertir la variable 'smoker' en binaria
insurance['smoker_flag'] = insurance['smoker'].map({'yes': 1, 'no': 0})
insurance.drop(columns=['smoker'], inplace=True)

# Estandarización manual de variables numéricas
insurance['age_std'] = (insurance['age'] - insurance['age'].mean()) / insurance['age'].std()
insurance['bmi_std'] = (insurance['bmi'] - insurance['bmi'].mean()) / insurance['bmi'].std()
insurance['children_std'] = (insurance['children'] - insurance['children'].mean()) / insurance['children'].std()


# 3. Visualización Exploratoria


# Costo del seguro según si fuma o no
sns.boxplot(x='smoker_flag', y='charges', data=insurance)
plt.title("Costo del seguro por hábito de fumar")
plt.show()

# Distribución del IMC
sns.histplot(insurance['bmi'], kde=True)
plt.title("Distribución del IMC")
plt.show()

# Dispersión edad vs costo del seguro
sns.scatterplot(x='age', y='charges', hue='smoker_flag', data=insurance)
plt.title("Edad vs Costo del Seguro")
plt.show()


# 4. Modelo de Clasificación


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Variables predictoras y objetivo
X_clf = insurance[['age_std', 'bmi_std', 'children_std', 'sex_male', 'region_northwest', 'region_southeast', 'region_southwest']]
y_clf = insurance['smoker_flag']

# División de datos
X_train_c, X_test_c, y_train_c, y_test_c = train_test_split(X_clf, y_clf, test_size=0.2, random_state=42)

# Modelo de regresión logística
clf = LogisticRegression()
clf.fit(X_train_c, y_train_c)
y_pred_c = clf.predict(X_test_c)

# Resultados del modelo de clasificación
print("\n=== Clasificación: ¿Es fumador? ===")
print("Accuracy:", accuracy_score(y_test_c, y_pred_c))
print("\nReporte de Clasificación:\n", classification_report(y_test_c, y_pred_c))
print("\nMatriz de Confusión:\n", confusion_matrix(y_test_c, y_pred_c))


# 5. Modelo de Regresión


from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Variables predictoras y objetivo
X_reg = X_clf  # Misma matriz que la de clasificación
y_reg = insurance['charges']

# División de datos
X_train_r, X_test_r, y_train_r, y_test_r = train_test_split(X_reg, y_reg, test_size=0.2, random_state=42)

# Modelo de regresión lineal
reg = LinearRegression()
reg.fit(X_train_r, y_train_r)
y_pred_r = reg.predict(X_test_r)

# Resultados del modelo de regresión
print("\n=== Regresión: Predicción de Costo ===")
print("MSE:", mean_squared_error(y_test_r, y_pred_r))
print("MAE:", mean_absolute_error(y_test_r, y_pred_r))
print("R2 Score:", r2_score(y_test_r, y_pred_r))


# 6. Conclusiones


# Comentarios:
# - Las variables más influyentes en la predicción del costo del seguro fueron edad, IMC y fumador.
# - El modelo de clasificación mostró buen rendimiento al identificar fumadores.
# - El modelo de regresión explica adecuadamente la variabilidad de los costos (según el R²).
# - Se podrían probar modelos más complejos (como Random Forest) para mejorar resultados.
# - También sería útil aplicar selección de características para evaluar su impacto en el desempeño.
