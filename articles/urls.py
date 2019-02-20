from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.ArticleListView.as_view(), name='home'),
    path('post/<int:pk>',views.ArticleDetailView.as_view(), name='article_page'),
    path('about/',views.About, name='about'),
    path('contact/',views.Contact, name='contact'),
]
