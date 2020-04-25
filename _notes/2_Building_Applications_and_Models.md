# 3. Building Users Applications: /users directory

### Creating Apps

```shell
 django-admin startapp [appname]
```

- since app contains multiple functions, appname should be in plural form
- names of .py files in application folder is not optional. You can't change names
- for example, users app has create password, update password

### How to make Users Application

- replacing django user with my user
- Python is object programming language: class can be inherited!
- CMD + click to check Abstractuser class
- Django makes migration by itself, so we don't have to write sql

```shell
python manage.py makemigrations
python manage.py migrate
```

- Django has database fields for everything: email field, text field... Just call for fields.

- installing module on python virtual environment SHOULD NOT BE DONE WITH pip.
  Use pipenv

  ```shell
  pipenv install Pillow
  ```

### models.py: All the fields are translated into database stuff.

Models have fields. For the fields you put in models.py, will make be turned into database table. Django ORM translates python code into SQL Instructions to database.

- **[Refer to models.py fields document on Django](https://docs.djangoproject.com/en/2.2/ref/models/fields/).**
- textfield: yields text field without limit on webpage
- charfield: yields text field with limit of single line webpage
- datefield: yields calendar selection on webpage
- boolean field: true of false checkbox

### admin.py: Admin Panel

- **[Refer to admin.py fields document document on Django](https://docs.djangoproject.com/en/2.2/ref/contrib/admin/)**
- admin.py regards about admin panel of the website.
- you can create filter(like excel) for fields in table: such as currency or superhost

# [4. Building Rooms Applications](../rooms)

## [Refer to cloning webpage. Rooms App's functions are: ](*https://www.airbnb.com/rooms/22320269?location=Seoul&source_impression_id=p3_1581697502_PpMPhvPC73I2KD%2BU*)

- room register
- room photo upload
- describing room's specifications(price, option, type...)

## [Making Core Application](../core)

- This is application that is not visible to users.

  - The purpose of this app is to simplify repetetive calling onto certain model: such as timestamp
    - [In this app's models.py, we made TimeStamped class](../core/models.py) as subject for the call up
    - [TimeStamped class](../core/models.py) will be used in all the other apps.
    - [On the other hand, Users app imported AbstractUser class from Django default models only](../users/models.py).

- All the other application names should be plural, except for this kind of application.

- In other apps' models.py, you can import Core Application's models along with default django models

  ```python
  #importing django default models as class
  from django.db import models

  #importing Core Application's models as class
  from core import models as core_models #"as" is like "import pandas as pd"
  ```

## WorkFlow when creating Rooms app

### 1. [At project's settings.py](../settings.py), install apps that I built. This is to let Django project know which are apps.py to use for the project.

```python
# Letting Django know my established Project apps by stating here.
# Importing apps.py in each apps: core, users, rooms, reviews ...
PROJECT_APPS = [
    "core.apps.CoreConfig",
    "users.apps.UsersConfig",
    "rooms.apps.RoomsConfig",
]

# Put users auth at the end
AUTH_USER_MODEL = "users.User"
```

### 2. [At individual application's models.py,](../rooms/models.py) shape database & connect between tables of other application's models.py

- **Write packages / modules in order**

```py
# first django
from django.db import models

# second third party apps
from django_countries.fields import CountryField

# third my applications
from core import models as core_models
```

- **[Foreign Key (one to multiple) in models.py](https://docs.djangoproject.com/en/3.0/ref/models/fields/)**

  - foreign key is connecting one model to the many other. source of the connection is user, and it connects to multiple rooms.
  - Foreign Key(FK:USER) calls data from another database(or sheet), which is user table.
  - For example, many instagram posts per user or many youtube posts per google user.

- **[Many to Many Relationship in models.py](https://docs.djangoproject.com/en/3.0/ref/models/fields/)**
  - models.ManyToManyField(<>)
- All of other classes above are inherited in Room class

```python
# Shaping Database(or table) of rooms
# All of classes above are inherited here.
class Room(core_models.TimeStampedModel):

    """ Room Model Definition """

    # when requiring fill up, don't put blank=True
    # Below are different types of fields that we can utilize

    #Charfield and textfield
    name = models.CharField(max_length=140)
    city = models.CharField(max_length=80)
    description = models.TextField()

    #country field is inhereted from third party
    country = CountryField()


    #integerfield example
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    guests = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()

    #timefield example
    check_in = models.TimeField()
    check_out = models.TimeField()

    #booleanfield(checkbox) example
    instant_book = models.BooleanField(default=False)

    # foreignkey field
    host = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room_type = models.ForeignKey("RoomType", on_delete=models.SET_NULL, null=True)


```

### 3. [At individual application's admin.py](../rooms/admin.py), register table models that you built previously.

```python
from django.contrib import admin
from . import models  # from the same folder, import the application's models

# refer to ./models.py for which models to register
# registering multiple models at once
@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    """ Item Admin Definition """

    pass
```

### 4. Since we shaped tables in models.py & reflected change of database on admin panel, makemigrations and migrate

```shell
python manage.py makemigrations
python manage.py migrate
```

### 5. At the webpage, check Admin panel.

### 6. [At individual application's models.py,](../rooms/models.py) setup verbose name to forcefully designate names that is displayed on Admin webpage.

# [5. Other Applications](../reservations)

### - Reviews application

### - Reservations application

### - Lists application

### - Conversations application
