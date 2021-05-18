from commentapp.forms import CommentCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormMixin
from .decorators import article_ownership_required
from .forms import ArticleCreationForm
from .models import Article


@method_decorator(login_required, "get")
@method_decorator(login_required, "post")
class ArticleCreationView(CreateView):
    model = Article

    form_class = ArticleCreationForm
    template_name = "articleapp/create.html"

    def form_valid(self, form):
        temp_article = form.save(commit=False)
        temp_article.writer = self.request.user
        temp_article.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("articleapp:detail", kwargs={"pk": self.object.pk})


class ArticleDetailView(DetailView, FormMixin):
    model = Article
    form_class = CommentCreationForm
    context_object_name = "target_article"
    template_name = "articleapp/detail.html"


@method_decorator(article_ownership_required, "get")
@method_decorator(article_ownership_required, "post")
class ArticleUpdateView(UpdateView):
    model = Article
    context_object_name = "target_article"
    form_class = ArticleCreationForm
    template_name = "articleapp/update.html"

    def get_success_url(self):
        return reverse_lazy("articleapp:detail", kwargs={"pk": self.object.pk})


@method_decorator(article_ownership_required, "get")
@method_decorator(article_ownership_required, "post")
class ArticleDeleteView(DeleteView):
    model = Article
    context_object_name = "target_article"
    template_name = "articleapp/delete.html"
    success_url = reverse_lazy("articleapp:list")


class ArticleListView(ListView):
    model = Article
    context_object_name = "article_list"
    template_name = "articleapp/list.html"
    paginate_by = 5
