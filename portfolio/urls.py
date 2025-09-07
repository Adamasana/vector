from django.urls import path
from . import views
from .views import home, contact, portfolio, actualite, profilactualite, profilprojet
from django.views.generic import TemplateView

urlpatterns = [
    path('', home, name="acceuil"),
    path('contact', contact, name="message"),
    path('portfolio', portfolio, name ='portfolio'),
    path('actualites', actualite, name ='actualites'),
    path('profilactualites/<int:actualite_id>/', profilactualite, name='profilactualites'),
    path('profilprojet/<int:projet_id>/', profilprojet, name='profilprojet'),
    #path('', TemplateView.as_view(template_name='blog/index.html'), name='home'),
]