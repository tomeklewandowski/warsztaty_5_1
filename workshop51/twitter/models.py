from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField(default=None)
    user_name = models.CharField(max_length=30, unique=True)

    @property
    def name(self):
        return "{}".format(self.user_name)

    def __str__(self):
        return self.user_name


class Post(models.Model):
    post = models.TextField(max_length=140)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

