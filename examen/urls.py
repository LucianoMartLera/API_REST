from django.urls import path
from examen.views import ProjectViews


urlpatterns=[
    path("proyectos/", ProjectViews.as_view()),
]