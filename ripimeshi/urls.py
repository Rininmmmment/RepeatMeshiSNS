from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView
from django.conf.urls.static import static
from django.conf import settings       

urlpatterns = [
    path('main/', include('main.urls')),
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    # path('', RedirectView.as_view(url='/main/')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)