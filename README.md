# job_market
# Présentation du Projet

## Objectifs
Créer un job board basé sur un modèle de recommandation, utilisant des technologies modernes pour le scraping, l'API, la gestion des données, et le déploiement.

## Contexte
Les utilisateurs recherchent des offres d'emploi adaptées à leurs compétences et préférences. Notre job board vise à améliorer l'expérience utilisateur en fournissant des recommandations personnalisées.

## Description Générale
Le projet collecte des données d'offres d'emploi de plusieurs sources, stocke ces données dans une base de données, les expose via une API, et utilise un modèle de recommandation pour suggérer des emplois pertinents aux utilisateurs.

# Spécifications Fonctionnelles

## Fonctionnalités Principales
- **Recherche d'Emplois** : Permet aux utilisateurs de rechercher des offres d'emploi par mots-clés, localisation, etc.
- **Recommandations Personnalisées** : Offre des recommandations d'emplois basées sur le profil de l'utilisateur.
- **Gestion des Utilisateurs** : Inscription, connexion, et gestion des profils utilisateurs.
- **Gestion des Offres d'Emploi** : Création, mise à jour, et suppression des offres d'emploi par les recruteurs.

## Flux Utilisateur
1. L'utilisateur s'inscrit et crée un profil.
2. L'utilisateur recherche des offres d'emploi.
3. L'utilisateur reçoit des recommandations personnalisées.
4. L'utilisateur postule aux offres d'emploi.

## Cas d'Utilisation
- **UC01 : Recherche d'Emplois**
- **UC02 : Recommandation d'Emplois**
- **UC03 : Gestion du Profil Utilisateur**
- **UC04 : Publication d'Offres d'Emploi**

# Spécifications Techniques

## Architecture du Système
- **Frontend** : Interface utilisateur 
- **Backend** : API FastAPI
- **Base de Données** : MySQL
- **Modèle de Recommandation** : Implémenté en Python
- **Déploiement** : Docker, Kubernetes
- **CI/CD** : GitLab

## Diagrammes UML
Inclure des diagrammes UML pour les cas d'utilisation, les classes, et les séquences.

## Choix Technologiques
- **Langage de Programmation** : Python
- **Framework Web** : FastAPI
- **Base de Données** : MySQL
- **Orchestrateur de Conteneurs** : Kubernetes
- **CI/CD** : GitLab CI/CD

