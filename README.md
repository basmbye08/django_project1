# Fatima's Restaurant Web Application

A Django web application for showcasing restaurant products and communicating with customers. Visitors can browse and search products, learn about the restaurant, submit contact messages, and create accounts. Administrators can manage products and review customer messages through Django Admin.

## Features

- Restaurant homepage with featured content
- Product listing with pagination
- Product search by name, description, or category
- About and contact pages
- Contact form with database-backed messages
- User registration, login, and logout
- Protected product access for authenticated users
- Django Admin management for products and contact messages
- Image uploads using Pillow
- Responsive Bootstrap-based templates

## Technology Stack

- Python
- Django 6.0.6
- SQLite
- Bootstrap 5
- Pillow
- python-dotenv

## Project Structure

```text
.
├── manage.py                 # Django command-line utility
├── project1/                 # Project settings and URL configuration
├── test1/                    # Main application
├── media/                    # Uploaded media files
├── db.sqlite3                # Development database
├── requirement.txt           # Python dependencies
└── PROJECT_DOCUMENTATION.md  # Detailed project documentation
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/basmbye08/django_project1.git
cd django_project1
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv

# Linux/macOS
source .venv/bin/activate

# Windows PowerShell
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirement.txt
```

### 4. Configure the secret key

Create a `.env` file in the project root:

```env
SECRET_KEY=replace-this-with-a-secure-secret-key
```

Do not commit real secrets to version control.

### 5. Apply migrations

```bash
python manage.py migrate
```

### 6. Start the development server

```bash
python manage.py runserver
```

Open <http://127.0.0.1:8000/> in your browser.

## Common URLs

| Page | URL |
|---|---|
| Home | `/` |
| Products | `/product/` |
| Search | `/findproduct/` |
| About | `/about/` |
| Contact | `/contact/` |
| Login | `/loginuser/` |
| Signup | `/signupuser/` |
| Admin | `/admin/` |

To create an administrator account, run:

```bash
python manage.py createsuperuser
```

## Testing

Run the Django test suite with:

```bash
python manage.py test
```

## Deployment Notes

This project is configured primarily for development. Before deploying to production, configure a secure `SECRET_KEY`, set appropriate `ALLOWED_HOSTS`, use a production-ready database, serve static and media files safely, and review Django's deployment checklist.

## License

No license has been specified for this project.
