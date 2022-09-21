up & running
===

Create virtualenv
---
```shell
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Prepare database
---

Apply migrations :

```shell
./manage.py migrate
```

Create superuser :

```shell
./manage.py createsuperuser
```

Compile translations
---

```shell
./manage.py compilemessages -l fr
```

Runserver
---

```shell
./manage.py runserver
```

Create some data
---
Next thing to do is to create some task using the admin on localhost:8000/admin
