from django.urls import path
from . import views
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.aboutPage, name='about'),
    path('send_email/', views.sendEmail, name="send_email"),
    path('portfolio/', views.projectsPage, name='portfolio')
]
