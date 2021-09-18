from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('<int:quiz_id>/', views.quiz_info, name='quiz_info'),
    path('create_score/<int:quiz_id>', views.create_score),
    path('result', views.result),
]