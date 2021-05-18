from django.contrib.auth import get_user_model
from django.db import models
from articleapp.models import Article

User = get_user_model()


class Comment(models.Model):
    article = models.ForeignKey(
        Article, on_delete=models.SET_NULL, null=True, related_name="comments"
    )
    writer = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="comments"
    )
    content = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
