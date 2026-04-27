Network Management Application
Overview

This is a Django-based web application for managing network-related data such as devices, employees, and management networks. The application provides a web interface for viewing and organizing network information.

Project Structure
manage.py : Django command-line utility
db.sqlite3 : Default database (SQLite)
network_management/ : Main project configuration (settings, URLs)
netmanagement/ : Core application (models, views, templates, forms)
static/ : CSS and static files
templates/ : HTML templates for UI

Requirements
Python 3.10 or higher
pip (Python package manager)
Virtual environment (recommended)

Installation Instructions
WINDOWS
Extract the project folder.
Open Command Prompt and navigate to the project directory:
cd path\to\network_management
Create a virtual environment:
python -m venv venv
Activate the virtual environment:
venv\Scripts\activate
Install dependencies:
pip install django
Apply database migrations:
python manage.py migrate
Run the development server:
python manage.py runserver
Open your browser and go to:
http://127.0.0.1:8000/

MAC (macOS / Linux)
Extract the project folder.
Open Terminal and navigate to the project directory:
cd /path/to/network_management
Create a virtual environment:
python3 -m venv venv
Activate the virtual environment:
source venv/bin/activate
Install dependencies:
pip install django
Apply database migrations:
python3 manage.py migrate
Run the development server:
python3 manage.py runserver
Open your browser and go to:
http://127.0.0.1:8000/

Usage
Access the homepage to view network data.
Navigate through pages to view employee and management network details.
View individual device details via the interface.

Notes
The project uses SQLite by default (no setup required).
Ensure the virtual environment is activated before running commands.
Static files (CSS) are included in the project.

Troubleshooting
If "python not recognized", ensure Python is added to your system PATH.
If port 8000 is in use, run:
python manage.py runserver 8001
