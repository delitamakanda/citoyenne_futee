# 🧠 Citoyen·ne & Futé·e – API Restful

Plateforme pédagogique en Django REST Framework pour développer la culture financière et citoyenne des jeunes (8–18 ans).

---

## 🚀 Objectif du projet

- Éduquer les enfants/adolescents à la gestion de l’argent, aux institutions et à la citoyenneté.
- Fournir une API scalable pour une application web/mobile (type Duolingo).
- Gérer la progression, les badges, les leçons et les rôles (élève, enseignant, parent, admin).

---

## 🏗️ Stack technique

- **Django 5.x**
- **Django REST Framework**
- **Wagtail (CMS leçons, facultatif)**
- **JWT pour l’authentification**
- **Redis (XP / classements)**

---

## 📁 Structure du projet
```
apps/
├── accounts/ ← Authentification, rôles utilisateurs
├── lessons/ ← Leçons, questions, choix
├── progress/ ← Suivi de progression des utilisateurs
├── gamification/ ← Badges, XP, classements
├── feedback/ ← Retours utilisateurs
├── common/ ← Mixins, enums, utils
config/ ← Settings Django (base/dev/prod)
```


## ⚙️ Installation locale

### 1. Cloner le repo
```bash
git clone https://github.com/delitamakanda/citoyenne_futee
cd citoyenne-futee-backend
```

### 2. Créer un environnement virtuel
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Configurer les variables d’environnement
Créer un fichier .env :

```env
DJANGO_SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=postgres://user:password@localhost:5432/futee
```

### 4. Lancer la base et les migrations
```bash
python manage.py migrate
python manage.py createsuperuser
```

### 5. Lancer le serveur
```bash
python manage.py runserver
```

## 🔐 Authentification
* JWT (via djangorestframework-simplejwt)
* Endpoints :
  * `/api/token/` (login)
  * `/api/token/refresh/ `
  * `/api/auth/register/`

## 🧪 Tests
```bash
python manage.py test
```

## 📚 API Documentation
Accessible via Swagger :

```bash
http://localhost:8000/api/docs/
```

## ✅ À venir
* Intégration du CMS Wagtail pour l’édition des contenus éducatifs 
* Endpoint public d’exploration des leçons 
* Intégration CI/CD GitHub Actions

## 📜 Licence
MIT © 2025 - Citoyen·ne & Futé·e
