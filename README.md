

# Backend : Dossier FakeAPI

FakeAPI est une API basée sur Flask qui propose divers endpoints pour gérer les données utilisateurs, y compris le téléchargement et la visualisation d’images d’utilisateurs.

## Installation du Backend

##Prérequis : Installer Python et Pip

### 1. Cloner le dépôt

Tout d'abord accéder au dossier :

```bash
cd FakeAPI
```

2. Créer un environnement virtuel
Il est recommandé de créer un environnement virtuel pour gérer les dépendances du projet :


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

Copier le code

```bash
source venv/bin/activate
```

Windows :
Copier le code

```bash
venv\Scripts\activate
```
4. Installer les dépendances
Une fois l’environnement virtuel activé, installez les packages requis avec :

Copier le code
```bash
pip install -r requirements.txt
```

5. Démarrer l'application
Vous êtes maintenant prêt à démarrer l'application Flask :

Copier le code
```bash
# Si vous exécutez directement
python.app
```
6. Cela démarrera le backend et vous pourrez y accéder à l'adresse suivante dans votre navigateur :
http://localhost:5000

# Frontend : Dossier .app

## Installation du Frontend
##Prérequis : Installer Node.js et npm
1. Accédez au dossier du projet : Allez dans le dossier .app du projet avec la commande suivante :

Copier le code
```bash

cd .app
```

2 .Installez les dépendances : Utilisez npm pour installer les dépendances du projet :
```bash
npm install
```

3. Lancez le projet : Pour démarrer le serveur de développement, utilisez la commande suivante
```bash
npm run dev
```

4. Cela démarrera le frontend et vous pourrez y accéder à l'adresse suivante dans votre navigateur :
http://localhost:3000




