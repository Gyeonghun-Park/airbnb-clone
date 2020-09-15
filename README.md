# Airbnb Cloning using Django

### **View Completed Site: [LandBnb](http://airbnb-clone2-dev.us-east-1.elasticbeanstalk.com/)**

Cloning Airbnb with Python, Django, Tailwind and more... 💖🐍

### Django Project Folder & File Structure

- [config folder](./config) is master folder
- rest of folders are just applications: applications are group of functionalities.

### [Project configuration folder's](./config) structure

- settings.py: you can refer to installed default apps in django. Look at django documentation links to find out.
- init.py helps to work like python package
- urls.py: controls url of the website. Can also be established under application.

### Individual application folders' structure

- apps.py: configuration file which is installed [at the project's settings.py](./config/settings.py)
- models.py: describing how database look like.
- admin.py: reflects changes on models.py to admin panel
- views.py: function that renders html
- urls.py: you can create urls.py under an application.like /users/profile, /users/delete, /users/register etc.

## [Notes #1 Initializing a Django Project](./_notes/1_Creating_a_Django_Project.md)

- Making Virtual Environment
- Installing django
- Selecting linter as flake8 and formatter as black
- SECURITY TIP: HOW TO KEEP SECRET_KEY SAFE

## [Notes #2 Building Applications and Models](./_notes/2_Building_Applications_and_Models.md)

- Building Users Applications inheriting Django's AbstractUsers class
- Building Core Application to reduce repetitive configuration in each applications.
- Building Rooms, Reviews, Reservations, Lists, Conversatiosn application
  1. register on settings.py
  2. shape database with models.py
  3. connect admin panel page with database at admin.py
  4. Make migrations and migrate

## [Notes #3: Making Admin Panel & Using Django Queryset](./_notes/3_Building_Admin_Panel.md)

```
<QuerySet [<User: myam>]>
```

- Querysets are list.
  - Objects are either manytomany, or foreignkey(=onetomany).
  - In the example above, <User: myam> is foreignkey.
- Adding fields to admin panel
- "super" in Python

## [Notes #4: Seeding Data to Database, not through Admin Panel](<./_notes/4_Seeding_Data_(NOT_by_Admin)_&_Fake_Data.md>)

- Seedng fake data using faker
- Seeding list files to database

## [Notes #5: Views and URLs](./_notes/5_Views_and_URLs.md)

- Use Django Template for formatting HTML file that Django can render
- urls.py is request
- views.py is response

## [Notes #6: Users app Login, Logout and Sign up](./_notes/6_Users_app_Login_Logout_and_Sign_up.md)

- Using OAuth to log user in with Github & Kakao

  - Users are redirected to request their GitHub identity
  - Users are redirected back to your site by GitHub
  - Your app accesses the API with the user's access token

## [Notes #7: Web decoration with Tailwind and Gulp](./_notes/7_Web_Design.md)

- [Calling tailwind css as class names in html](https://tailwindcss.com/)
- Extensions
  - Use Tailwind CSS intelilisense for tailwind class lookup
  - DON'T FORGET TO RESTART VSCODE AFTER INSTALL

## [Notes #8: Deploying airbnb clone application using AWS Elastic Beanstalk](./_notes/8_Deployment_to_AWS.mdd)

- Ongoing...

### My development environment

- System: zsh 5.4.2 (x86_64-ubuntu-linux-gnu) on Windows 10 Education N(1909)
- Python 3.8.2 (default, Feb 26 2020, 02:56:10) [GCC 7.4.0] on linux

##
