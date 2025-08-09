# 🛠️ Django Machine Test Project

This is a Django REST API project with PostgreSQL as the database. It supports client management, project assignments, and user authentication.

---

## 📌 Features
- Register, edit, and delete clients
- Fetch client information
- Add new projects for a client
- Assign users to projects
- Retrieve assigned projects for the logged-in user
- Admin panel for managing users (Django default)
- PostgreSQL database

---

## 📂 Project Structure
'''machine_test/
│
├── api/ # API app with views, serializers, and URLs
├── machine_test/ # Main Django project settings
├── manage.py # Django project manager
├── requirements.txt # Python dependencies
└── README.md # Documentation'''

---

## 🚀 Installation Guide

### 1️⃣ Prerequisites
Make sure you have installed Python 3.10+, PostgreSQL with pgAdmin, and Git.

### 2️⃣ Setup Instructions

- git clone https://github.com/YOUR_USERNAME/machine_test.git
- cd machine_test
- python -m venv venv
- venv\Scripts\activate # For Windows PowerShell

OR
- source venv/bin/activate # For Mac/Linux
- pip install -r requirements.txt


---

### 3️⃣ Configure PostgreSQL
- Create a database named `machine_db` in pgAdmin.
- Create a user with a username and password.
- Give the user all privileges on `machine_db`.
- Update `machine_test/settings.py`:
  DATABASES = {
'default': {
'ENGINE': 'django.db.backends.postgresql',
'NAME': 'machine_db',
'USER': 'your_username',
'PASSWORD': 'your_password',
'HOST': 'localhost',
'PORT': '5432',
}
}

---

### 4️⃣ Apply Migrations and Create Superuser
- python manage.py makemigrations 
- python manage.py migrate 
- python manage.py createsuperuser 

---

### 5️⃣ Run the Server
python manage.py runserver

---

## 🌐 Access
- Admin Panel: http://127.0.0.1:8000/admin/
- API Endpoints: http://127.0.0.1:8000/api/

---

## 📡 API Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/clients/` | Register a new client |
| GET | `/api/clients/` | Fetch clients info |
| PUT/PATCH | `/api/clients/{id}/` | Edit client info |
| DELETE | `/api/clients/{id}/` | Delete client |
| POST | `/api/projects/` | Add new project for a client & assign users |
| GET | `/api/my-projects/` | Retrieve projects assigned to logged-in user |

---

## 📦 Export Dependencies
pip freeze > requirements.txt

---

## 🤝 Contributing
Pull requests are welcome! For major changes, open an issue first to discuss what you’d like to change.





