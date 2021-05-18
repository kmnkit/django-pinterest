from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Project(models.Model):
    title = models.CharField(null=False, max_length=20)
    description = models.TextField(null=True, max_length=200)
    image = models.ImageField(upload_to="project/", null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
