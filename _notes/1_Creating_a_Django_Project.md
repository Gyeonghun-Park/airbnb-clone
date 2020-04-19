# 2. Creating a Django Project

### How to Initiate Project

```shell
pipenv shell
```

- initiate virtual environment for project in the project's directory

- it will take some time for initial setup

- In order to exit the virtual environment, deactivate

  ```shel
  deactivate
  ```

  - or exit the virtual environment, If "UNKNOWN VIRTUAL ENVIRONMENT is already activated" error

    ```shell
    exit
    ```

- **MAKE SURE YOU ARE INSIDE THE BUBBLE.**

- Then, setup configuration for the django.

- **It's okay to use pip inside of virtual environment, but download log of packages won't be recorded on pipfile**

```shell
pipenv install django
django-admin startproject config
```

- Drag config directory and manage.py file out of the original config directory. Manually change the config directory of the project (NOT USING CONSOLE)

- You can change python settings on the low deck of VSCode.

- Go to manage.py Python file. VSCode will tell you to setup linter and formatter.

  - Recommending flake 8 as linter. it is automatically recommended through vscode

  - Recommending black as formatter.

    - If formatter isn't recommended bia VSCode, then commence the following:

      ```shell
      pipenv install black --dev --pre
      ```

  - Selecting linter and formatter for the project is recorded on .vscode/settings.json file

### manage.py: database and server

- **[Refer to manage.py related Django documents here](https://docs.djangoproject.com/en/3.0/ref/django-admin/)**

- Run your server, Where pipenv is activated (= inside the bubble).

```shell
python manage.py runserver
```

Or, if you want to run on different port,

```shell
python manage.py runserver 7000
```

- You'll have localhost connection.
- You can also access to admin panel page, which is http://127.0.0.1:8000/admin/login/?next=/admin/
- Without manage.py, database table doesn't exist. Thus this kind of error will appear on console log, if you run server for the second time.
  **You have 17 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions. Run 'python manage.py migrate' to apply them.**
- SQL needs to learn how database look like.
- You change the shape of data(=creating migration), and migrate to update database
- Updating Database: Django shapes the data(or change the shape), you create migration, you apply migration
- Therefore, configurate SQL(Structured Queried Language) database with

```shell
python manage.py migrate
```

### Security & Other Tips

- [Make .gitignore file referencing this link](https://github.com/github/gitignore/blob/master/Python.gitignore)
- For those uploaded their django repository publicly, keep your SECRET_KEY in settings.py away from the others!
  - [English Instructiions on how to keep SECRET_KEY safe](https://www.quora.com/Is-it-possible-to-change-the-secret-key-of-a-Django-application-after-it-deployment-in-production-If-so-what-would-be-the-impacts)
  - [SECRET_KEY를 안전하게 보관하는 법 국문 가이드](https://wayhome25.github.io/django/2017/07/11/django-settings-secret-key/)
- Even if you successfully removed SECRET_KEY from settings.py, git history of the file is still accessible in github on public. So it is still dangerous to keep(or to publish) your repo as public repo.
  - [WARNING: all of your GIT history will be cleared after commencing the next process][follow the steps of this link in order to clear up git history, and commit as initial commit.](https://gist.github.com/stephenhardy/5470814)
  - If files & file contents were to be pages in a book, Git history is like bookmarks. Clearing git history will not affect current files/directories on your project.
  - However, removing git history means your previous versions(NOT current versions) are inaccessible. For example, you can’t revert your project files to version you worked on a week ago.
- [In Django documentation, you can even look up the code.](https://docs.djangoproject.com/en/2.2/_modules/django/contrib/auth/password_validation/#CommonPasswordValidator)
- On VSCode Windows, CMD + Mouse Click on function to see the source code

### Projects vs. apps

[What’s the difference between a project and an app? An app is a Web application that does something – e.g., a Weblog system, a database of public records or a small poll app. A project is a collection of configuration and apps for a particular website. A project can contain multiple apps. An app can be in multiple projects.](https://docs.djangoproject.com/en/3.0/intro/tutorial01/)

- Django project is group of applications (= just say Django is a group of functions).
- When to create application / when not to create application is important.
- We should not have so much functionality in one folder(=application)
- **You should be able to describe an application in one sentence.** If you use the word "and", then it should be diferent application. **Divide and conquer**
- For example, listing application will be consisted with functions as such: Create list, Read List, Update List and delete list
