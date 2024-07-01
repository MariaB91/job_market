# Dockerfile pour MySQL
FROM mysql:8.0

# Définition des variables d'environnement pour la configuration de MySQL
ENV MYSQL_DATABASE job_board
ENV MYSQL_USER user
ENV MYSQL_PASSWORD password
ENV MYSQL_ROOT_PASSWORD rootpassword

# Copie du script d'initialisation de la base de données dans le conteneur
COPY init.sql /docker-entrypoint-initdb.d/
