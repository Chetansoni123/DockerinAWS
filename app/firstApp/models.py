from django.db import models

class UserModel(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    mobile = models.CharField(max_length=15)

    def __str__(self):
        return self.email
