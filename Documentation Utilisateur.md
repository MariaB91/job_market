# Guide d'Installation

## Prérequis
- Docker
- Kubernetes
- Helm
- Git

## Étapes d'Installation
1. Clonez le dépôt :
   ```bash
   git clone [https://your-gitlab-repo.git](https://github.com/MariaB91/job_market.git)
   cd job_market

2. Construisez et démarrez les conteneurs Docker :
 ```bash
 docker-compose up --build

3. Déployez l'application sur Kubernetes :
```bash
kubectl apply -f kubernetes/deployment.yaml

4. Vérifiez le déploiement :
```bash
kubectl get pods

5. Accédez à l'application via l'adresse IP du LoadBalancer.

#### Guide d'Utilisation
```markdown
# Guide d'Utilisation

## Inscription et Connexion
- Accédez à la page d'inscription et créez un compte.
- Connectez-vous avec vos identifiants.

## Recherche d'Emplois
- Utilisez la barre de recherche pour trouver des offres d'emploi par mots-clés, localisation, etc.

## Recommandations Personnalisées
- Consultez la section des recommandations pour voir des emplois suggérés en fonction de votre profil.

## Publication d'Offres d'Emploi
- Pour les recruteurs, accédez à la section de publication pour créer, modifier ou supprimer des offres d'emploi.


