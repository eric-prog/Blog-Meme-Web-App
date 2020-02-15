from django.contrib import admin
from django.urls import path, include 
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from memez import views as meme_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('memez/', include('memez.urls')),
    path('accounts/', include('accounts.urls')),
    path('', meme_views.meme_list, name="home"),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
