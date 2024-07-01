# Dockerfile pour une application FastAPI
FROM python:3.9-slim

# Définition du répertoire de travail
WORKDIR /app

# Copie des fichiers de dépendances et installation des paquets Python nécessaires
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copie de tous les fichiers de l'application dans le répertoire de travail
COPY . .

# Commande par défaut pour démarrer l'application FastAPI avec Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
