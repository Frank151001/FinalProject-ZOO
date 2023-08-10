from django.urls import path
from .views import HomePageView,AboutPageView,AnimalsPageView,TicketsPageView
urlpatterns = [
    
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("animals/",AnimalsPageView.as_view(),name="animals"),
    path("tickets/",TicketsPageView.as_view(),name="tickets")
]