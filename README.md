<img width="1913" height="943" alt="1" src="https://github.com/user-attachments/assets/1a61e6da-8540-4c29-b7c3-bfafbc4f762e" />
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

> Coming soon

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
