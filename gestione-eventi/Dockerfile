# Usa immagine PHP con Apache
FROM php:8.2-apache

# Abilita mod_rewrite (se utile)
RUN a2enmod rewrite

# Copia codice PHP nella cartella di Apache
COPY src/ /var/www/html/

