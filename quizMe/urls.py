from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static

from users.views import register
from . import views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include('quizzes.urls')),
    path('', include('users.urls')),
    
    path('', views.home, name='home'),
    path('quizzes/', include('quizzes.urls')),
    path('register/', register, name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', LoginView.as_view(), name='login'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
