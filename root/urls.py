from django.urls import path

from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("/searchresults",views.search_results,name="new"),

]
