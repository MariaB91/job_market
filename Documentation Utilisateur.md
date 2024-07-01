# Guide d'Installation

## Prérequis
- Docker
- Kubernetes
- Helm
- Git

## Étapes d'Installation
1. Clonez le dépôt :
   ```bash
   git clone https://your-gitlab-repo.git
   cd your-gitlab-repo

2. Construisez et démarrez les conteneurs Docker :
  ```bash
 docker-compose up --build

3. Déployez l'application sur Kubernetes :

```bash
kubectl apply -f kubernetes/deployment.yaml
