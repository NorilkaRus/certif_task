from django.shortcuts import render
from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListAPIView
from rest_framework.filters import BaseFilterBackend, SearchFilter
from .models import *
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import SellerSerializer, SellerUpdateSerializer
from .permissions import IsActive
# Create your views here.

class SellerCreateApiView(CreateAPIView):
    serializer_class = SellerSerializer
    permission_classes = [IsActive]


class SellerRetrieveApiView(RetrieveAPIView):
    serializer_class = SellerSerializer
    permission_classes = [IsActive]
    queryset = Seller.objects.all()


class SellerUpdateApiView(UpdateAPIView):
    serializer_class = SellerUpdateSerializer
    permission_classes = [IsActive]
    queryset = Seller.objects.all()


class SellerDestroyApiView(DestroyAPIView):
    serializer_class = SellerSerializer
    permission_classes = [IsActive]
    queryset = Seller.objects.all()


class SellerListApiView(ListAPIView):
    serializer_class = SellerSerializer
    permission_classes = [IsActive]
    queryset = Seller.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['contact__country',]
    filterset_fields = ['contact__country',]
