from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accountapp.urls")),
    path("articles/", include("articleapp.urls")),
    path("profiles/", include("profileapp.urls")),
    path("comments/", include("commentapp.urls")),
    path("projects/", include("projectapp.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
