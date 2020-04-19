# 9. Making Python Manage.py commands to seed data at each apps

- Making commands (like messages that pops up when you type on consoles)
- Feeding (using pyton) data to database without using admin page
  - user data
  - room data
  - list data
- Following two python scripts are the same

```python
#simple import form
from users.models import User
all_user = User.objects.all()
```

```python
#specific import form: when differentiating with other models are needed
from users import models as user_models
all_user = user_models.User.objects.all()
```

- inputting variables at string sentence with f"{variable}"

  ```python
  def add_arguments(self, parser):
          parser.add_argument(
              "--number",
              default=1,
              type=int,
          )

  number = options.get("number")
  self.stdout.write(self.style.SUCCESS(f"{number} rooms created"))
  ```

- lists foreignkey rooms

  ```python
  # executing seeder
  created = seeder.execute()

  # allocating random rooms to list
  cleaned = flatten(list(created.values()))
  for pk in cleaned:
    # getting list class item with primary key
    list_model = list_models.List.objects.get(pk=pk)
    # list of rooms from random number to random number
    random_int1 = random.randint(0, 5)
    random_int2 = random.randint(6, 30)
    to_add = all_rooms[random_int1:random_int2]
    # below is "rooms" field at lists.models class List
    list_model.rooms.add(*to_add)
  ```

- add entities to seeder packet

  ```python
  all_users = user_models.User.objects.all()

  seeder.add_entity(
              list_models.List,
              number,
              # foreignkey field wrapped as queryset
              {"user": lambda x: random.choice(all_users)},
          )
  ```

- inject seeder packet to the database

  ```python
  seeder.execute()
  ```

- Console log is printed through "stand out"

  ```python
  self.stdout.write(self.style.SUCCESS(f"{number} {NAME} created"))
  ```

- Run the following command on shell

  ```shell
  python manage.py seed_users --number 50
  ```

#
