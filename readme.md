# FakeAPI

FakeAPI est une API basée sur Flask qui propose divers endpoints pour gérer les données utilisateurs, y compris le téléchargement et la visualisation d’images d’utilisateurs.

## Installation du projet

### 1. Cloner le dépôt

Tout d'abord, clonez ce dépôt sur votre machine locale :

```bash
git clone <url-de-votre-dépôt>
cd FakeAPI
2. Créer un environnement virtuel
Il est recommandé de créer un environnement virtuel pour gérer les dépendances du projet :
```

Copier le code
```bash
# Sur macOS/Linux
python3 -m venv venv
```
```bash
# Sur Windows
python -m venv venv
```

3. Activer l'environnement virtuel
Pour activer l'environnement virtuel, utilisez les commandes suivantes :

macOS/Linux :

bash
Copier le code
source venv/bin/activate
Windows :

bash
Copier le code
venv\Scripts\activate
4. Installer les dépendances
Une fois l’environnement virtuel activé, installez les packages requis avec :

bash
Copier le code
pip install -r requirements.txt
5. Configurer les variables d'environnement (optionnel)
Si votre projet nécessite des variables d’environnement spécifiques (comme une clé secrète pour Flask), créez un fichier .env dans le dossier FakeAPI avec les variables nécessaires. Par exemple :

plaintext
Copier le code
FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=votre_cle_secrete
6. Créer le dossier uploads
Créez un dossier nommé uploads à la racine du projet pour stocker les images téléchargées par les utilisateurs.

bash
Copier le code
mkdir uploads
7. Démarrer l'application
Vous êtes maintenant prêt à démarrer l'application Flask :

bash
Copier le code
# Si vous exécutez directement
flask run

# Ou spécifiez le module de l'application si nécessaire
FLASK_APP=app.py flask run
