from . import views
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as authentication_views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('hobbies/', views.hobbies, name="hobbies"),
    path('hobbies/<int:hobby_id>', views.hobby_detail, name="hobby_detail"),
    path('portfolio/', views.portfolio, name="portfolio"),
    path('portfolio/<int:project_id>', views.portfolio_detail, name="portfolio_detail"),
    path('contact/', views.contact, name="contact"),
    path('contact_form/', views.contact_form, name="contact_form"),
    path('portfolio_form/', views.portfolio_form, name="portfolio_form"),
    path('update/<int:id>', views.update_portfolio, name="update_portfolio"),
    path('delete/<int:id>', views.delete_portfolio, name="delete_portfolio"),
    path('login/', authentication_views.LoginView.as_view(template_name='portfolio/login.html'), name='login'),
    path('logout/', authentication_views.LogoutView.as_view(template_name='portfolio/logout.html'), name='logout'),



]