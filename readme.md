# What is Little Lemon
Little Lemon is a web application where employees from the restaurant "Little Lemon" can customize their own Menu and, book reservations for their customers. Employees can add, update, and delete menu items and reservations.

# Tech Stack
* Front-End:
    * HTML
    * CSS
* Back-End:
    * Python
    * Django
    * Django Rest Framework
* Database:
    * MySQL

# Features
* Get, Add, Update and Delete Menu items
* Get, Add, Update and Delete reservation Bookings

# How to Install and Run Little Lemon
1. Click the Green Code button and select "Download ZIP".
2. Open the zip file and run it in Visual Studio Code.
3. Open the project level directory and open "settings.py" file.
4. Under Databases, change the information to connect your database.
5. Open the terminal and make sure you are in the same directory where the "manage.py" file is in.
6. Run "pipenv shell" and "pipenv install". This will create a virtual environment and install the packages from the pipfile.
7. Run "python manage.py makemigrations" and "python manage.py migrate" to propogate the models and changes to your database schema.
8. Run "python manage.py runserver" to start server.
9. Open a web browser and go to "127.0.0.1:8000/restaurant/"
10. Browse and test out the features.

# NOTE: Little Lemon original purpose
Originally, the Little Lemon project was supposed to be a Back-End only project. It's purpose was to provide RESTful APIs for users to use to manage CRUD operations for a restaurant while communicating with other software components (such as their own front-end program, Postman, Insomnia, etc.). The Back-End utilized Django REST Framework and generics to create CRUD operations. As of now, it is a Full-Stack application with minimal functionality in the Fron-End and custom Back-End views to demonstrate the features of the project. 

# How to test RESTful API Endpoints (via Browsable API, Postman, Insomnia, etc.)
1. Go to restaurant > views.py file
2. Comment all "form_class" and functions under MenuItemsView, SingleMenuItemView, and DeleteSingleMenuItemView classes.
3. Comment all "booking" urls in the app level urls.py file.
4. Run "python manage.py runserver"
5. Test the endpoints below.

# Test urls:
* GET & POST: restaurant/menu/
* GET & PUT: restaurant/menu/<'input menu item id'>
* GET & DELETE: restaurant/menu/<'input menu item id'>/delete
* GET & POST: restaurant/bookings/tables
* GET, PUT, DELETE: restaurant/bookings/table/<'input booking id'>