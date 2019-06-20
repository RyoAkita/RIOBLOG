from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('index/', views.IndexView.as_view(), name='index'),
    path('detail/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('likes/<int:pk>/', views.likefunc, name='likes'),
    path('category/<int:pk>/', views.CategoryView.as_view(), name='category'),
    path('comment/<int:post_pk>/', views.CommentView.as_view(), name='comment'),
    path('about/', views.aboutfunc, name='about'),
    path('contact/', views.contactfunc, name='contact')
]

