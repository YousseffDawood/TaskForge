# TaskForge

A role-based project management web application built with Django. TaskForge allows teams to manage projects, assign tasks, track progress, and communicate through comments — all with a clean, modern interface.

---

## Features

- **Role-based access control** — Three distinct roles: Admin, Employee, and Customer, each with specific permissions
- **Project management** — Customers create projects, admins manage them, employees execute them
- **Task system** — Admins create and assign tasks to employees within projects
- **Comments** — Admins and employees can communicate directly on tasks
- **Notifications** — Users get notified when project or task status changes
- **Status tracking** — Projects and tasks move through Todo → In Progress → Done
- **Admin panel** — Admins can oversee all projects, users, and team members

---

## Roles

| Role | Permissions |
|---|---|
| **Customer** | Create projects, view own projects, receive notifications |
| **Employee** | View assigned projects, update task status, comment on tasks |
| **Admin** | Full access — manage projects, assign tasks, add members, update statuses |

---

## Tech Stack

- **Backend** — Django 4.x
- **Database** — PostgreSQL
- **Auth** — Django AbstractUser with custom roles
- **Frontend** — Django Templates, vanilla CSS, vanilla JS

---

## Installation

```bash
# Clone the repository
git clone https://github.com/YousseffDawood/taskforge.git
cd taskforge

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your database credentials

# Run migrations
python manage.py migrate

# Create admin user
python manage.py shell
# Then run:
# from accounts.models import User
# User.objects.create_user(username='admin', password='yourpassword', roles='ADMIN', is_staff=True)

# Start the server
python manage.py runserver
```

---

## Project Structure

```
taskforge/
├── accounts/          # Custom user model and authentication
├── project/           # Projects, tasks, comments, notifications
├── templates/         # All HTML templates
│   ├── base.html
│   ├── home.html
│   ├── accounts/
│   └── project/
├── manage.py
└── requirements.txt
```

---

## Screenshots

<img width="1915" height="944" alt="10" src="https://github.com/user-attachments/assets/17bb5252-b0e5-4a4d-aec1-e3dea6626c3f" /><img width="1919" height="945" alt="9" src="https://github.com/user-attachments/assets/03599966-8405-4dff-bcf7-5285b2a7b96f" />
<img width="1897" height="942" alt="8" src="https://github.com/user-attachments/assets/b3ab7c96-a9b6-4dc7-b923-f8220cd0d1ed" />
<img width="1916" height="947" alt="7" src="https://github.com/user-attachments/assets/16af3a5f-2252-4218-8867-cef830bb8f3c" />
<img width="1911" height="937" alt="6" src="https://github.com/user-attachments/assets/b3d52145-163f-4ddf-bf1f-e124107a5673" />
<img width="1909" height="945" alt="5" src="https://github.com/user-attachments/assets/3feda677-964b-4b60-b3ce-e177d351a623" />
<img width="1910" height="942" alt="4" src="https://github.com/user-attachments/assets/006ca028-9979-49a0-9007-a77a4213a1b7" />
<img width="1907" height="946" alt="3" src="https://github.com/user-attachments/assets/4ad0465e-eedc-4d3c-b9e8-fec45a297be0" />
<img width="1913" height="944" alt="2" src="https://github.com/user-attachments/assets/7a0c3096-e7a8-4550-b610-a1f4828c1d64" />
<img width="1913" height="943" alt="1" src="https://github.com/user-attachments/assets/63d63c40-450e-4982-8ec0-070115f657db" />

---

## Roadmap

- [ ] REST API with Django REST Framework
- [ ] Email notifications
- [ ] File attachments on tasks
- [ ] Project deadlines and due dates
- [ ] Activity log per project

---

## Author

**Youssef Dawood**
GitHub: [@YousseffDawood](https://github.com/YousseffDawood)

---

> Built as a portfolio project to demonstrate Django backend development, role-based access control, and real-world project management concepts.
