from django.conf.urls import url
from views.handlers import HomePage

urlpatterns = [
    url(r'^home-page/', HomePage.as_view(), name='home_page'),
]