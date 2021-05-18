from django.forms import ModelForm
from .models import Article


class ArticleCreationForm(ModelForm):
    class Meta:
        model = Article
        fields = ["project", "title", "image", "content"]
