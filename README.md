 Bounty-Hunting
 
Bounty-Hunting is a Software Engineering semester project developed as part of the 6th semester coursework at Tribhuvan University.
The project demonstrates the application of software engineering principles — from requirements gathering and design to implementation and testing — in building a functional system.

Project Overview

- Designed as a case study project for learning structured software development.
- 
- Implements modular design with clear separation of concerns.
- 
- Focuses on user interaction, data management, and process flow.
- 
- Built with Python/Django (backend) and HTML/CSS/JavaScript (frontend).
  
Tech

Backend:Pythone(Django)

Database:Mysql

FrontEnd:HTML,CSS AND JavaScript

Getting Started

Prerequisites
• 	Python 3.8+

• 	pip (Python package manager)

• 	virtualenv (recommended)

Installation

 Clone the repository

- git clone https://github.com/GodANDDevil/Bounty-Hunting.git
  
- cd Bounty-Hunting

  Create a virtual environment

python -m venv venv

source venv/bin/activate   # Linux/Mac

venv\Scripts\activate      # Windows

 Install dependencies

-pip install -r requirements.txt

Run migrations

python manage.py migrate

Start the development server

python manage.py runserver

- Visit http://127.0.0.1:8000/ (127.0.0.1 in Bing) in your browser.

Project Structure

Bounty-Hunting/
│── bounty/          # Main Django app
│── db.sqlite3       # Database file
│── manage.py        # Django project manager
│── requirements.txt # Dependencies

Bounty-Hunting/

│── bounty/          # Main Django app

│── db.sqlite3       # Database file

│── manage.py        # Django project manager

│── requirements.txt # Dependencies

 Future Improvements
 
• 	Add user authentication and role-based access.

• 	Improve UI with Bootstrap/TailwindCSS.

• 	Deploy on Heroku/AWS for live demonstration.

• 	Extend documentation with UML diagrams and test cases.
