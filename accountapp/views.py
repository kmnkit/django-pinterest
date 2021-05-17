from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView

# from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from django.urls import reverse_lazy

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
