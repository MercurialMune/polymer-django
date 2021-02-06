from django.urls import path
from django.views.generic import TemplateView
from Counties import views as views

urlpatterns = [
    path('', TemplateView.as_view(template_name="home.html"), name='home'),
    path('search_results/', views.search_results, name='search_results'),
]
