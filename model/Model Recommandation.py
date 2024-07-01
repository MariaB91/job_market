# Code pour entraîner un modèle de recommandation
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Chargement des données
data = pd.read_csv('job_data.csv')
data = data[data['language'] == 'en']  # Ne garder que les données en anglais

# Prétraitement des données (extraction des caractéristiques pertinentes)
X = data[['feature1', 'feature2', 'feature3']]
y = data['job_applied']

# Division en ensembles de formation et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Entraînement du modèle
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Sauvegarde du modèle
import joblib
joblib.dump(model, 'recommendation_model.pkl') # Le modèle enregistré est produit par le code ci-dessus, et il est sauvegardé dans un fichier recommendation_model.pkl.
