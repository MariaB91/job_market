# Exemple de Dockerfile pour MySQL
FROM mysql:8.0

ENV MYSQL_DATABASE job_board
ENV MYSQL_USER user
ENV MYSQL_PASSWORD password
ENV MYSQL_ROOT_PASSWORD rootpassword

COPY init.sql /docker-entrypoint-initdb.d/
