from django.contrib.auth import get_user_model
from django.db import models
from projectapp.models import Project

User = get_user_model()


class Article(models.Model):
    writer = models.ForeignKey(
        User, on_delete=models.SET_NULL, related_name="articles", null=True
    )
    project = models.ForeignKey(
        Project,
        on_delete=models.SET_NULL,
        null=True,
        related_name="articles",
    )
    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to="articles/", null=False)
    content = models.TextField(null=True)

    created_at = models.DateField(auto_now_add=True, auto_created=True)

    class Meta:
        ordering = [
            "pk",
        ]
