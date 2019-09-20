# Développer

La méthode ci-dessous permet d'installer un environnement Python isolé avec les bonnes versions de paquet.
Si vous avez la chance d'être sur une distribution avec des paquets récents (ArchLinux…) vous n'en avez peut-être pas besoin.

```
# Créer un virtualenv python3 puis l'active
python3 -m venv venv
. venv/bin/activate

# Installation des dépendances
pip install -r requirements.txt

# Mise en place rapide de Django pour du dev
./manage.py migrate  # Exécute les migrations de la base de données
./manage.py compilemessages  # Compile les traductions
./manage.py createsuperuser  # Crée un super-utilisateur
./manage.py runserver  # Lancer un serveur de développement
```
