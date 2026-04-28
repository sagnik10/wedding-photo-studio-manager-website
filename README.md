# Wedding Photo Studio Manager

A Django-powered web application designed to streamline wedding photography studio operations, from client booking to project delivery.

## Overview

This project is a full-stack web application built using Django that helps photography studios manage their workflow. It provides tools to handle client bookings, organize project data, and maintain structured operations for wedding photography businesses.

## Features

* Client booking management
* Project tracking and organization
* Client data management
* Workflow handling
* Django admin panel
* SQLite database integration

## Tech Stack

* Backend: Django (Python)
* Database: SQLite3
* Frontend: HTML, CSS (Django Templates)
* Environment: Virtual environment (venv)

## Project Structure

```
wedding-photo-studio-manager-website/
│── wedding_platform/
│── venv/
│── db.sqlite3
│── manage.py
│── .gitignore
```

## Installation and Setup

1. Clone the repository

```
git clone https://github.com/sagnik10/wedding-photo-studio-manager-website.git
cd wedding-photo-studio-manager-website
```

2. Create virtual environment

```
python -m venv venv
```

3. Activate virtual environment

Windows:

```
venv\\Scripts\\activate
```

Mac/Linux:

```
source venv/bin/activate
```

4. Install dependencies

```
pip install django
```

5. Run migrations

```
python manage.py migrate
```

6. Start development server

```
python manage.py runserver
```

7. Open in browser

```
http://127.0.0.1:8000/
```

## Admin Access

Create a superuser:

```
python manage.py createsuperuser
```

Access admin panel:

```
http://127.0.0.1:8000/admin/
```

## Future Improvements

* User authentication system
* Image upload and gallery management
* Payment integration
* Dashboard and analytics
* Deployment (AWS, Heroku, Docker)

## Contributing

Fork the repository and submit a pull request.

## License

This project is open-source and available under the MIT License.

## Author

Sagnik Sen

## Support

If you find this project useful, consider giving it a star on GitHub.
