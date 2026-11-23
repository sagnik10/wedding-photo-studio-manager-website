<!-- SAGNIK10-STYLE-HEADER -->
<div align="center">
  <a href="https://github.com/sagnik10"><img src="https://img.shields.io/badge/Sagnik_Sen-Full-Stack%20Web-275cce?style=flat-square" alt="Category" /></a>
  <img src="https://img.shields.io/badge/Stack-Python-192a43?style=flat-square" alt="Stack" />
  <img src="https://img.shields.io/badge/License-MIT-54647a?style=flat-square" alt="License" />
</div>

<p align="center">
  <a href="https://sagnik10.github.io/SagnikSenPortfolio/">Portfolio</a> ·
  <a href="https://github.com/sagnik10">GitHub Profile</a> ·
  <a href="https://github.com/sagnik10/sagnik-sen-antigravity-plugin">Antigravity Plugin</a>
</p>

---
<!-- /SAGNIK10-STYLE-HEADER -->
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


<!-- SAGNIK10-STYLE-FOOTER -->
---
<p align="center">
  Maintained by <a href="https://github.com/sagnik10"><strong>Sagnik Sen</strong></a> ·
  <a href="https://sagnik10.github.io/SagnikSenPortfolio/">Portfolio &amp; 1-on-1 Teaching</a> ·
  <a href="https://www.linkedin.com/in/sagnik-sen-0a70431a8/">LinkedIn</a>
</p>
<!-- /SAGNIK10-STYLE-FOOTER -->