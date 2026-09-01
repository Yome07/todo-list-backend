# 📝 Todo List Backend

API REST backend pour une application de gestion de tâches (Todo List), construite avec **Django** et **Django REST Framework**.
Exercice dans le cadre de la formation Software Engineer de Liora

## 🛠️ Technologies

- **Python** 3.12
- **Django** 6.0.3
- **Django REST Framework** 3.17.1
- **SQLite** (développement) / **PostgreSQL** (production)
- **WhiteNoise** pour les fichiers statiques
- **django-cors-headers** pour la gestion CORS
- **Gunicorn** pour le déploiement en production

## 📦 Modèles de données

### Category
| Champ  | Type          | Description              |
|--------|---------------|--------------------------|
| `id`   | Auto          | Identifiant unique       |
| `name` | CharField(255)| Nom de la catégorie      |

### Task
| Champ          | Type           | Description                      |
|----------------|----------------|----------------------------------|
| `id`           | Auto           | Identifiant unique               |
| `description`  | TextField      | Description de la tâche          |
| `is_completed` | BooleanField   | Statut d'achèvement (défaut: False) |
| `created_at`   | DateTimeField  | Date de création (auto)          |
| `category`     | ForeignKey     | Catégorie associée               |

## 🔗 Endpoints de l'API

| Méthode | Endpoint               | Description                        |
|---------|------------------------|------------------------------------|
| GET     | `/api/categories/`     | Liste toutes les catégories        |
| POST    | `/api/categories/`     | Crée une nouvelle catégorie        |
| GET     | `/api/categories/{id}/`| Détail d'une catégorie             |
| PUT     | `/api/categories/{id}/`| Met à jour une catégorie           |
| DELETE  | `/api/categories/{id}/`| Supprime une catégorie             |
| GET     | `/api/tasks/`          | Liste toutes les tâches            |
| POST    | `/api/tasks/`          | Crée une nouvelle tâche            |
| GET     | `/api/tasks/{id}/`     | Détail d'une tâche                 |
| PUT     | `/api/tasks/{id}/`     | Met à jour une tâche               |
| DELETE  | `/api/tasks/{id}/`     | Supprime une tâche                 |

## 🚀 Installation & Lancement

### Prérequis

- Python 3.12+

### Étapes

1. **Cloner le dépôt**
   ```bash
   git clone <url-du-repo>
   cd todo-list-backend
   ```

2. **Créer et activer l'environnement virtuel**
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Linux/macOS
   .venv\Scripts\activate      # Windows
   ```

3. **Installer les dépendances**
   ```bash
   pip install -r requirements.txt
   ```

4. **Appliquer les migrations**
   ```bash
   python manage.py migrate
   ```

5. **Lancer le serveur de développement**
   ```bash
   python manage.py runserver
   ```

L'API sera disponible sur `http://127.0.0.1:8000/api/`.

## ⚙️ Configuration

Le projet utilise des fichiers de settings séparés :

| Fichier                  | Usage                              |
|--------------------------|------------------------------------|
| `settings/base.py`       | Configuration commune              |
| `settings/development.py`| Développement (SQLite, DEBUG=True) |
| `settings/production.py` | Production (PostgreSQL, DEBUG=False)|

### Variables d'environnement (production)

| Variable              | Description                                |
|-----------------------|--------------------------------------------|
| `SECRET_KEY`          | Clé secrète Django                         |
| `ALLOWED_HOSTS`       | Hôtes autorisés (séparés par des virgules) |
| `DATABASE_URL`        | URL de connexion PostgreSQL                |
| `CORS_ALLOWED_ORIGINS`| Origines CORS autorisées                   |

## 🌐 CORS

En développement, les origines suivantes sont autorisées :
- `http://localhost:5173`
- `http://127.0.0.1:5173`

Cela permet l'intégration avec un frontend (React/Vite) en développement local.

## 📄 Licence

Ce projet est à usage personnel/éducatif.