from django.urls import path, include

from main import views

app_name = 'main'

urlpatterns = [
    path('project/',views.project,name = 'project'),
    path('language/',views.language,name = 'language'),
    path('',views.index,name = 'index')
]