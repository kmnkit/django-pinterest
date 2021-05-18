from django.contrib.auth import get_user_model
from django.http import HttpResponseForbidden

User = get_user_model()


def account_ownership_required(func):
    def decorated(request, *args, **kwargs):
        user = User.objects.get(pk=kwargs["pk"])
        if user != request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)

    return decorated
