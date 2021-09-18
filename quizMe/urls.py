from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('quiz/',include('quiz_App.urls')),
    path('',include('login_App.urls')),
    path('admin/', admin.site.urls),
]
