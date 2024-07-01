import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
import spacy

# Charger et nettoyer les données
data = pd.read_csv('job_data.csv')
nlp = spacy.load("en_core_web_sm")
data = data[data['language'] == 'en']

# Prétraitement des données (extraction des caractéristiques pertinentes)
X = data[['feature1', 'feature2', 'feature3']]
y = data['job_applied']

# Division en ensembles de formation et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Entraînement du modèle
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Sauvegarde du modèle
joblib.dump(model, 'recommendation_model.pkl')
