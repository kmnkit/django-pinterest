from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.constraints import UniqueConstraint
from projectapp.models import Project

User = get_user_model()


class Subscription(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="subscriptions"
    )
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="subscriptions"
    )

    class Meta:
        constraints = [
            UniqueConstraint(fields=["user", "project"], name="unique_subscriptions")
        ]
