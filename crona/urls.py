from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.views.generic.base import RedirectView
from django.conf.urls.static import static
from crona import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.default.urls')),

    path('covid/', include('covid.urls')),
    path('', RedirectView.as_view(url="covid/")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

