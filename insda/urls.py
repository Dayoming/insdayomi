from django.conf.urls import url
from insda.views import index
from insda.views import upload
from insda.views import detail
from insda.views import delete
from insda.views import update
from insda.views import like
from insda.views import board

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^board/', board, name='board'),
    url(r'^upload/', upload, name='upload'),
    url(r'^delete/(?P<pk>[0-9]+)/$', delete, name='delete'),
    url(r'^detail/(?P<pk>[0-9]+)/$', detail, name='detail'),
    url(r'^update/(?P<pk>[0-9]+)/$', update, name='update'),
    url(r'^like/', like, name='like'),
]