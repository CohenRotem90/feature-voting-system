#!/bin/bash

# Wait for MySQL to be ready
until mysqladmin ping -h"db" -uroot -prootpass --silent; do
  echo "Waiting for MySQL..."
  sleep 2
done

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create or update the superuser with known password
python manage.py shell << END
from django.contrib.auth.models import User
username = "admin"
password = "Admin1234!"
email = "admin@example.com"
user, created = User.objects.get_or_create(username=username, defaults={"email": email})
if not created:
    user.email = email
user.is_staff = True
user.is_superuser = True
user.set_password(password)
user.save()
print(f"Superuser '{username}' ready.")
END

# Start Gunicorn
exec gunicorn feature_voting_project.wsgi:application --bind 0.0.0.0:8000
