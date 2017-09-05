from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from .serializers import AlbumSerializer, AlbumDetailSerializer
from .models import Album


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all().order_by('-id')
    pagination_class = StandardResultsSetPagination
    serializer_class = AlbumSerializer

    def retrieve(self, request, pk):
        queryset = Album.objects.all()
        album = get_object_or_404(queryset, pk=pk)
        album_detail = AlbumDetailSerializer(album)
        return Response(album_detail.data)