# 💻 Project

![preview of the project](.github/app_preview.png 'Contact Book Project Preview')

ContactBook is a personal project created to save, organize and display all the contacts of a micro, small and medium enterprise.
The first goal of the project is to ciment knoladge of the programming languages evolved in the project. This was also my first project creating all the back-end and front-end by myself.

The back-end was built with Python and it's Django Framework, that connects directly all the contacts information in the database. Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design.
In this project I used the MySQL Workbench as database and the free and open source Xampp as cross-platform web server solution stack package.
The front-end was built with HTML and CSS. 

## Features
### Display contacts by A-Z organized by groups
Contacts organized by Alphabethic order
![preview of the project](.github/app_preview.png 'Contact Book Project Preview')

Contacts organized by groups
![contacts organized by groups](.github/groups_preview.png 'Contact Book organized by groups preview')

### Add contacts
![add contacts form](.github/addContact_preview.png 'To add a contact form preview')

### Delete and Edit contacts
To edit or/and delete a contact just click the buttons
![edit and delete contacts buttons](.github/edit_delete.png 'To edit or/and delete a contact just click the buttons')

### Connection with the database
Everytime you add, edit or delete contacts from the app, you can check the update at the database.

Groups preview:
![groups preview](.github/database_preview_groups.png 'Groups preview')

Contacts information preview:
![contacts information preview](.github/database_preview.png 'Contacts information preview')

# 🛠️​ Technologies

This project was developed with the following technologies:

- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
- [Python](https://www.python.org/doc/)
- [Django](https://docs.djangoproject.com/en/4.1/)
- [MySQL Workbench](https://dev.mysql.com/doc/)


# ⚙️Setup

## Run locally

Create and go to the directory where you want to place the repository

```bash
    cd directory
```

Clone the project

```bash
  git clone https://github.com/ma-oliveiramarques/contact-book.git

```

Go to the project directory

```bash
  cd contact-book
```

Open in Pycharm

```bash
  code .
```

To run locally and mimic my setup, you will need to have:
- the web-server [Xampp](https://www.apachefriends.org/);
- database [MySQL Workbench](https://www.mysql.com/downloads/);
- [Python](https://www.python.org/downloads/) - used the version 3.10.7;
- [Django](https://www.djangoproject.com/download/) - used the version 4.1.1:
  - Create a virtual environment
  - ```pip install Django==4.1.1```
  - ```$ python -m django --version```
  - ``django-admin startproject agenda``
  - Update ```agenda/settings.py``` to configure:
   ```SECRET_KEY``` (your secret key), ```DATABASE``` (the name of your database in MySQL) and ```STATIC_ROOT``` entries
  ```./manage.py startapp agenda``` , to create the welcome page's app
  - ``python manage.py createsuperuser``
  - ``py manage.py runserver`` : http://127.0.0.1:8000/
  - ``py manage.py makemigrations``
  - ``py manage.py migrate``

  
# 📝​ License

MIT
