from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from core import views
urlpatterns = [
    
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('signup/', views.register, name="signup"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('profile/', views.profile, name="profile"),
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('store.urls')),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


