from django.conf.urls import url
from .views import AlbumViewSet


album_list = AlbumViewSet.as_view({
    'get' : 'list',
})
album_detail = AlbumViewSet.as_view({
    'get' : 'retrieve',
})

urlpatterns = [
    url(r'^album', album_list, name='album_list_api'),
    url(r'^adetail/(?P<pk>[0-9]+)', album_detail, name='album_detail_api')
]