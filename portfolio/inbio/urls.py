from django.urls import path 
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('index/', views.index, name ="index"),
    path('about/', views.about, name='about'),
    path('skills/',views.skills_view,name='skills'),
    path("projects/", views.projects_view, name="projects"),
    path('contact/', views.contact, name='contact'),

]
