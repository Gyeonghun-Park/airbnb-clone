# 7. Web Design

## 19 Intro to Tailwind CSS

### What is Gulp?

- SCSS -> ugly CSS
- New JavaScript -> Old JavaScript
- Pug.js -> ugly HTML
- uploading to github automization

we do not utilize babel nor yarn for this project

```shell
npm init
npm install gulp gulp-postcss gulp-sass gulp-csso node-sass auto-prefixer -D
npm install tailwindcss -D
```

- If you don't do npm init, then node modules will be installed in upper directory with npm on it
- initialize tailwind css

```shell
npx tailwindcss init
```

### Compile scss to css

- make alias on package.json

  ```json
  "scripts": {
      "css": "gulp"
    }
  ```

- compile scss into css file

  ```shell
  npm run css
  ```

### Integrating css to HTML

- static path: http://127.0.0.1:8000/static/css/styles.css

- loading static path to html: replacing http://127.0.0.1:8000/static to tag {static}

  ```html
  {% load static %} <link rel="stylesheet" href="{% static "css/styles.css" %}">
  ```

- CSS is already done by tailwind css at styles.css

- Call tailwind css by using class="tailwind-css-classname"
  [Refer tailwind css document for classnames](https://tailwindcss.com/docs/border-color)

- em is relative to closest font-size

- rem is relative to root font size

## 20 Design

### [Cloning Airbnb login](./templates/users/login.html)

- Example page for Cloning

  ![airbnb login page for cloning](_img/airbnb_login.png)

## 21 User Profile, Edit Profile, Change Password

### [The messages framework](https://docs.djangoproject.com/en/3.0/ref/contrib/messages/)

- Quite commonly in web applications, you need to display a one-time notification message (also known as “flash message”) to the user after processing a form or some other types of user input

- The default [settings.py](../config/settings.py) created by django-admin startproject already contains all the settings required to enable message functionality

### Adding messages

- To use the message, import it to [views.py](../users/views.py) first

  ```py
  from django.contrib import messages

  ....

  messages.error(request, e)
  ```

- Some shortcut methods provide a [standard way](https://docs.djangoproject.com/en/3.0/ref/contrib/messages/#adding-a-message) to add messages with commonly used tags (which are usually represented as HTML classes for the message)

### Django get_absolute_url()

- When it comes to web development you really want to avoid hard coding paths in your templates

- This method enables admin panel to work "View on site" link

  ![airbnb login page for cloning](_img/admin_viewOnSite.png)

  [Example of absolute url](../templates/partials/nav.html):

  ```HTML
  <!-- hard coding url -->
  <li class="nav_link"><a href="{{% url "users:profile" user.pk %}}">Profile</a></li>

  <!-- absolute url -->
  <li class="nav_link"><a href="{{user.get_absolute_url}}">Profile</a></li>
  ```

### [Adding messages in class-based views](https://docs.djangoproject.com/en/3.0/ref/contrib/messages/#adding-messages-in-class-based-views)

- Adds a success message attribute to FormView based classes

  Example [views.py](../users/views.py):

  ```py
  from django.contrib.messages.views import SuccessMessageMixin

  ...

  class LoginView(mixins.LoggedOutOnlyView, FormView):
  ```

- You can also use customizing messages through [mixins](https://docs.djangoproject.com/en/3.0/topics/auth/default/#django.contrib.auth.mixins.UserPassesTestMixin)
  - You can use this when you want to send a different kind of message instead of a success message
  - Example: [mixins.py](../users/mixins.py)

### Mixins

- This can prevent users from accessing the wrong page through url manipulation

  Example [mixins.py](../users/mixins.py):

  ```py
  from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin

  ...

  class EmailLoginOnlyView(UserPassesTestMixin):
  ```

## 22 Room Detail

### [Pluralize](https://docs.djangoproject.com/en/3.0/ref/templates/builtins/#pluralize)

- Returns a plural suffix if the value is not 1, '1', or an object of length 1. By default, this suffix is 's'

  Example [room_detail.py](../templates/rooms/room_detail.html):

  ```HTML
  <span class="mr-5 font-light">{{room.beds}} bed{{room.beds|pluralize}}</span>
  ```

## 23 Update Room, Create Room, Room Photos

### [The login_required decorator](https://docs.djangoproject.com/en/3.0/topics/auth/default/#the-login-required-decorator)

- If the user is logged in, execute the view normally. The view code is free to assume the user is logged in

- If the user isn’t logged in, redirect to settings.LOGIN_URL, passing the current absolute path in the query string

  - I added LOGIN_URL to [settings.py](../config/settings.py)

  Example [views.py](../rooms/views.py):

  ```py
  from django.contrib.auth.decorators import login_required
  ...

  @login_required
  def delete_photo(request, room_pk, photo_pk):
  ```

## 24 Reservations and Reviews

### [Calendar](https://docs.python.org/3/library/calendar.html#module-calendar)

- This module allows you to output calendars like the Unix cal program, and provides additional useful functions related to the calendar

- In this project, two calendar object (this month, next month) are required
  - These objects are sent from [cal.py](../cal.py) to [models.py](../rooms/models.py)

### [Custom template tags and filters](https://docs.djangoproject.com/en/3.0/howto/custom-template-tags/)

- You may find yourself needing functionality that is not covered by the core set of template primitives

- You can extend the template engine by defining custom [tags](https://docs.djangoproject.com/en/3.0/ref/templates/builtins/#built-in-tag-reference) and [filters](https://docs.djangoproject.com/en/3.0/ref/templates/builtins/#filter) using Python, and then make them available to your templates using the {% load %} tag

- Your custom tags and filters will live in a module inside the [templatetags](../rooms/templatetags) directory

  Example of the directory:

  ```
  rooms/
      __init__.py
      models.py
      templatetags/
          __init__.py
          is_booked.py
      views.py
  ```

## [Validators](https://docs.djangoproject.com/en/3.0/ref/validators/)

- A validator is a callable that takes a value and raises a ValidationError if it doesn’t meet some criteria. Validators can be useful for re-using validation logic between different types of fields

  You can add this to a model field via the field’s validators argument:

  ```py
  from django.db import models

  class MyModel(models.Model):
    even_field = models.IntegerField(validators=[validate_even])
  ```

### 25 Translations, Lists and Messages

## [Translation](https://docs.djangoproject.com/en/3.0/topics/i18n/translation/)
