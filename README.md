# Frontend : Dossier .app

## Installation du Frontend
### Prérequis : Installer Node.js et npm
1. Accédez au dossier du projet : Allez dans le dossier .app du projet avec la commande suivante :

Copier le code
```bash

cd .app
```

2 .Installez les dépendances : Utilisez npm pour installer les dépendances du projet :
```bash
pnpm install
```

3. Lancez le projet : Pour démarrer le serveur de développement, utilisez la commande suivante
```bash
npm run dev
```

4. Cela démarrera le frontend et vous pourrez y accéder à l'adresse suivante dans votre navigateur :
### http://localhost:3000


# Backend : Dossier FakeAPI

FakeAPI est une API basée sur Flask qui propose divers endpoints pour gérer les données utilisateurs, y compris le téléchargement et la visualisation d’images d’utilisateurs.

## Installation du Backend

### Prérequis : Installer Python et Pip

1. Cloner le dépôt

Tout d'abord accéder au dossier :

```bash
cd FakeAPI
```

2. Créer un environnement virtuel
Il est recommandé de créer un environnement virtuel pour gérer les dépendances du projet :

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


```bash
source venv/bin/activate
```

Windows :


```bash
venv\Scripts\activate
```
4. Installer les dépendances
Une fois l’environnement virtuel activé, installez les packages requis avec :

```bash
pip install -r requirements.txt
```

5. Démarrer l'application
Vous êtes maintenant prêt à démarrer l'application Flask :

```bash
# Si vous exécutez directement
python.app
```
6. Cela démarrera le backend et vous pourrez y accéder à l'adresse suivante dans votre navigateur :
### http://localhost:5000


# API 

### Pour assurer le bon fonctionnement de l'application, remplissez la base de données à l'aide de ces API en utilisant POSTMAN.

## User APIs
### API Post http://127.0.0.1:5000/api/v1/user

API pour créer des utilisateurs

#### Créer 3 utilisateurs avec cette API



Sélectionnez méthode POST.

En-têtes (Headers)
Postman gère automatiquement la plupart des en-têtes, mais assurez-vous que Content-Type est réglé sur multipart/form-data lors de l’ajout de fichiers.

Corps de la Requête (Body)
Sélectionnez Body > form-data, et ajoutez les paires clé-valeur suivantes. Assurez-vous de marquer photo comme File en cliquant sur le menu déroulant à côté du nom de la clé.

Clé	            Valeur
civility_id	    1
firstname	      John
lastname	      Doe
username	      johndoe
email	         john.doe@example.com
laboratory_id	 1
password	     password123
division_id	   1
group_id	     1
photo	         Sélectionnez votre image

### API Get http://127.0.0.1:5000/api/v1/user/user_id

API pour récupérer des utilisateurs

## Supervisor APIs

### API Post http://127.0.0.1:5000/api/v1/user










