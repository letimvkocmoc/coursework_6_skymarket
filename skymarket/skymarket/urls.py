from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

# TODO здесь необходимо подклюючит нужные нам urls к проекту
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from ads import views

urlpatterns = [
    path("api/admin/", admin.site.urls),
    path("api/redoc-tasks/", include("redoc.urls")),
    path("api/", include('ads.urls')),
    path("api/", include('users.urls')),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
