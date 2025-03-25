from django.urls import path
from . import views

app_name = 'questions'

urlpatterns = [
    # C
    path('create/', views.create, name='create'),
     
    # R
    path('', views.index, name='index'),
    path('<int:id>/', views.detail, name='detail'),

    # Comment C
    path('<int:article_id>/comments/create/', views.comment_create, name='comment_create'),

    # random
    path('random/', views.random_page, name='random_page')
]