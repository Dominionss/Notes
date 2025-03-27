from django.urls import path, include
from .views import home, create_note
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', home, name='home'),
    path('create/', create_note, name='create_note'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
