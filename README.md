# Urban Issues Platform

## Description
La plateforme "Urban Issues" permet aux citoyens de signaler des problèmes urbains tels que des déchets, des routes endommagées, des coupures d'eau, des défaillances d'éclairage public, etc. Les utilisateurs peuvent suivre la résolution de ces problèmes en temps réel.

## Fonctionnalités
- Signalement de problèmes urbains
- Suivi en temps réel de l'état des problèmes signalés
- Interface d'administration pour gérer les problèmes
- Notifications pour les mises à jour de statut

## Prérequis
- Python 3.x
- Django 3.x ou supérieur
- Une base de données (SQLite par défaut, mais peut être configurée pour d'autres)

## Installation
1. Clonez le dépôt :
   ```
   git clone <URL_DU_DEPOT>
   cd urban-issues-platform
   ```

2. Créez un environnement virtuel et activez-le :
   ```
   python -m venv venv
   source venv/bin/activate  # Sur Windows utilisez `venv\Scripts\activate`
   ```

3. Installez les dépendances :
   ```
   pip install -r requirements.txt
   ```

4. Appliquez les migrations :
   ```
   python manage.py migrate
   ```

5. Démarrez le serveur de développement :
   ```
   python manage.py runserver
   ```

## Utilisation
- Accédez à l'application via `http://127.0.0.1:8000/`
- Utilisez l'interface pour signaler des problèmes et suivre leur statut.

## Contribuer
Les contributions sont les bienvenues ! Veuillez soumettre une demande de tirage pour toute amélioration ou correction.

## License
Ce projet est sous licence MIT. Veuillez consulter le fichier LICENSE pour plus de détails.

## NOM
Ndeye Diengue Khady Fall Songdé Diop
Assa Ndiaye
Momar Bosse Ndoye
Aichatou Diallo