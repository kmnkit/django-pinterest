from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import AccountUpdateForm

User = get_user_model()


def hello_world(request):
    if request.method == "POST":
        return render(
            request, "accountapp/hello_world.html", context={"text": "POST METHOD!!"}
        )
    else:
        return render(
            request, "accountapp/hello_world.html", context={"text": "GET METHOD!!"}
        )


class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy("accountapp:hello_world")
    template_name = "accountapp/create.html"


class AccountDetailView(DetailView):
    model = User
    context_object_name = "target_user"
    template_name = "accountapp/detail.html"


class AccountUpdateView(UpdateView):
    model = User
    context_object_name = "target_user"
    form_class = AccountUpdateForm
    success_url = reverse_lazy("accountapp:hello_world")
    template_name = "accountapp/update.html"


class AccountDeleteView(DeleteView):
    model = User
    template_name = "accountapp/delete.html"
