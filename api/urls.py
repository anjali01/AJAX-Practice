from django.conf.urls import url
from api import views

urlpatterns = [
    url(r'^countries/$', views.CountryList.as_view()),
    url(r'^countries/(?P<country_code>\w+)/states/$', views.StateList.as_view())
]
