# book-manager
Django book managing system with review feature for each book.
# Features
1) CRUD operations for authors and for books by selecting an existing author.
2) Admin panel generated from the Django framework.
3) Registration and login.
4) Permissions for registered and unregistered users.
5) Search feature by author name or book title.

# Project Setup Python 3.6 required
1) Install virtual environment via `cmd` or `gitbash` - `pip install virtualenv`
2) Create virtual environment - `virtualenv bookenv`
3) Activate the environment - Windows users - `source bookenv/Scripts/activate`(if you are using `cmd`, `source` will be an unknown command so you will need to move to the directory where `activate` exist and type it in the console,
Linux users - `source bookenv/bin/activate`.
4) Install Django in the virtual environment - `pip install Django==1.9`
5) Navigate to the directory where the `manage.py` file exists - `book-manager/book-manager/mysite`.
6) Run project - `python manage.py runserver`


