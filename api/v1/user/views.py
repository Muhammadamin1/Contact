from django.db.models import Q
from rest_framework.generics import *
from .serializers import *


class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer

    def get_queryset(self):
        queryset = User.objects.all()
        query = self.request.query_params.get('search')
        if query is not None:
            queryset = User.objects.filter(Q(full_name__icontains=query) |
                                           Q(phone_number__icontains=query) |
                                           Q(email__icontains=query) |
                                           Q(relative__full_name__icontains=query) |
                                           Q(relative__phone_number__icontains=query) |
                                           Q(relative__email__icontains=query))
        return queryset


class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
