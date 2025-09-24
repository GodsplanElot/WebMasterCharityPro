from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(("pages.urls", "pages"), namespace="pages")),
    path("accounts/", include(("accounts.urls", "accounts"), namespace="accounts")),
    path("UserPorile/", include(("UserPorile.urls", "UserPorile"), namespace="UserPorile")),
    path("secured/", include(("secured.urls", "secured"), namespace="secured")),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)