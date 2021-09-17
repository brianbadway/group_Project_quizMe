from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('',include,('quiz_App.urls')),
    path('admin/', admin.site.urls),
]
