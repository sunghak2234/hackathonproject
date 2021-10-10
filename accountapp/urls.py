from django.urls import path
from accountapp.views import start, test, upload
from django.conf import settings
from django.conf.urls.static import static

app_name = 'hello_world'

urlpatterns = [
    path('start/', start, name='start'),
    path('test/', test, name='test'),
    path('upload/', upload, name='upload'),
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)