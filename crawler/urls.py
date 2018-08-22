from django.conf.urls import url
from crawler.views import crawler

urlpatterns = [
    url(r'^$', crawler, name='crawler'),
]