from django.conf.urls import url
from views.handlers import HomePage
from jupiter.settings import MEDIA_ROOT, STATIC_ROOT

urlpatterns = [
    url(r'^home-page/', HomePage.as_view(), name='home_page'),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': MEDIA_ROOT}),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',{'document_root': STATIC_ROOT}),
]