from django.contrib.auth.models import AbstractUser

# from django.db import models

# For more information on this, see:
# https://docs.djangoproject.com/en/4.0/topics/auth/customizing/#specifying-a-custom-user-model

# To do extra things like normalize email addresses as lowercase and adding
# extra fields, see this example:
# https://docs.djangoproject.com/en/4.0/topics/auth/customizing/#a-full-example


class User(AbstractUser):
    # bio = models.TextField(blank=True, null=True)
    # USERNAME_FIELD = "email"
    # REQUIRED_FIELDS: List[str] = []
    pass
