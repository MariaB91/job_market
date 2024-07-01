# Documentation CI/CD

## Configuration GitLab CI/CD
- Le fichier `.gitlab-ci.yml` définit trois étapes : build, test, et deploy.
- **Build** : Construction de l'image Docker de l'application.
- **Test** : Exécution des tests unitaires dans un conteneur Docker.
- **Deploy** : Déploiement de l'application sur Kubernetes.

## Variables d'Environnement
- `DATABASE_URL` : URL de connexion à la base de données MySQL.

## Déploiement
- L'image Docker est poussée au registre Docker de GitLab.
- Kubernetes est utilisé pour déployer l'application via le fichier `kubernetes/deployment.yaml`.
