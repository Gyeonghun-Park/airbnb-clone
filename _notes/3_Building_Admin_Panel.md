# [6. Room Admin Panel & Site](../rooms/admin.py)

- Making representative tables on webpage
- Making Search fileds
- Creating Filter

# [7 Django Queryset](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#django.db.models.query.QuerySet)

- ```shell
  <QuerySet [<User: myam>]>
  ```

  1. Querysets are list.

  2. Objects are either manytomany, or foreignkey(=onetomany). In the example above, <User: myam> is foreignkey.

## How to look up querysets

- Run manage.py shell

  ```shell
  pipenv shell
  python manage.py shell
  ```

- vars to look up simple information, dir to look up specific information in database

  ```python
  from users.models import User
  vars(User)
  dir(User)
  ```

### Getting foreignkeys & manytomany Queryset

- [In this case, users is poining at reviews with foreignkey.](../reviews/models.py)

  ```python
  user = models.ForeignKey(
          "users.User", related_name="reviews", on_delete=models.CASCADE
      )
  ```

  Thus, we can get querysets for reviews.

  ```python
  myam = User.objects.get(username="myam")
  vars(myam)
  dir(myam)
  myam.reviews.all()
  ```

- To get all users,

  ```python
  from users.models import User
  User.objects.all()
  ```

* [In this case, rooms is pointing reviews with foreignkey](.reviews/models.py)

  ```python
  # pointing rooms tables with reviews database
  room = models.ForeignKey(
    "rooms.Room", related_name="reviews", on_delete=models.CASCADE
  )
  ```

  Thus, we can get querysets for reviews and amenities

  ```python
  from rooms.models import Room
  room = Room.objects.get(id=1)
  room
  room.reviews.all()
  ```

* [In this case, many to many relationship is established between amenities and rooms.](../rooms/models.py)

  ```python
  amenities = models.ManyToManyField("Amenity", related_name="rooms", blank=True)
  ```

  Thus, we can get querysets for amenities.

  ```python
  room.amenities.all()
  ```

  Or, we can get queryset with the following method also.

  ```python
  from rooms.models import Amenity
  Amenity.objects.all()
  a = Amenity.objects.get(id=1)
  a.rooms.all()
  ```

* In order to get queryset, instead of this,

  ```shell
   room.review_set -> WRONG
  ```

  Do this to get queryset (from reviews).

  ```python
  room.reviews.all()
  ```

* **You should use related_names field in models.py in order to get queryset.**

* **related_names is for the target.** [Next example is when users table points rooms table with foreignkey](../rooms/models.py), but didn't set related_name inside of field.

```python
  host = models.ForeignKey(
          "users.User", on_delete=models.CASCADE
      )
```

In this case. At Manage.py Shell, when you look up queryset of users received from rooms, You'll have following error.

```python
  myam.rooms.all()
  ------------------------------------
  "AttributeError: 'myam' object has no attribute 'rooms'"
```

따라서 [rooms의 models.py에서](../rooms/models.py) users로 pointing한다. users과 rooms을 연결하는 foreignkey 부분에 related_name을 추가함으로서, users에 "rooms"라는 queryset을 보낸다.

```python
host = models.ForeignKey(
      "users.User", related_name="rooms", on_delete=models.CASCADE
    )
```

[이에 대한 관련 내용은 Foreignkey에서 related_name으로 query를 짜는 법 문서를 참조하라.](https://docs.djangoproject.com/en/3.0/topics/db/queries/)

Filtering queryset: get queryset with specified options

- filtering

  ```python
  from users.models import User
  all_user = User.objects.all()
  all_user.filter(superhost=True)
  ```

- ```python
  startswith = User.objects.filter(username__startswith="noo")
  print(startswith)
  ```

  if you run this, you will get noopy.

# 8. Adding Fields to Admin Panels

- [User Admin panel](../users/admin.py) doesn't refer to [models.py](/users/models.py), but rather refers to [Django's default UserAdmin class.](/Users/noopy/.local/share/virtualenvs/django-airbnb-clone-AcLC9Tzu/lib/python3.8/site-packages/django/contrib/auth/admin.py)

- Until now, [we have been making custom function on admin.py, for example, rooms' admin panel](../rooms/admin.py). But now, [we are making user rating average function at the reviews models.py](../reviews/models.py), and [deploying it on reviews Admin panel](../reviews/admin.py).

- We've switched between rooms app and reviews app. Average reviews ratings of a room was reflected on room admin panel. We also used queryset to get functions on the other app. [Check commit log to see details.](https://github.com/Gyeonghun-Park/airbnb-clone/commit/58e65295d430d82e0142fe77ab985f39a1f592c4)

- list_display to display models.py fields on admin panel

- timezone utility from django, which translates timezones of users

  ```python
  from django.utils import timezone
  ```

- Project directory, URL router at [../config/settings.py](../config/settings.py)

```python
# yields /Users/noopy/django-airbnb-clone/uploads
os.path.join(BASE_DIR, "uploads")

# storing photos in ./uploads
MEDIA_ROOT = os.path.join(BASE_DIR, "uploads")

# When I am on production level (when server is live), I set DEBUG in settings.py False
DEBUG = True

# previously, link to image was http://127.0.0.1:8000/admin/rooms/photo/9/change/room_photos/photoname.png
# now, changing the link to image as http://127.0.0.1:8000/media/photoname.png
MEDIA_URL = "/media/"  # "/media" slash / in fronth means absolute
```

- You cannot change function name "urlpatterns" at [config/urls.py](../config/urls.py)

- Django doesn't render scripts (or html code), if it is not marked safe.

  ```python
  # marking safe for inputted scripts to Django
  from django.utils.html import mark_safe

  def get_thumbnail(self, obj):
  	return mark_safe(f'<img width="300px" src="{obj.file.url}"')
  ```

- raw_ids to look up

- inline models

### !Super is super important!

- [save() methods is controlling models](../rooms/models.py)

  ```python
  def save(self, *args, **kwargs):
          # print(self.city)
      		# you can add send_emails here, to notify whenever objects were saved in admin panels
          self.city = str.capitalize(self.city)
          # call the real save() method from Django
          super().save(*args, **kwargs)
  ```

- [save_model is controlling admin](../rooms/admin.py)

  ```python
  def save_model(self, request, obj, form, change):
          #print the html: show object,show whether did it change, show form
          print(obj, change, form)
          super().save_model(request, obj, form, change)
  ```

- like sending emails whenever admin panel is saved
