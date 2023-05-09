from django.urls import path, include
from apps.views import Index, Detail

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('detail<uuid:pk>/', Detail.as_view(), name='detail'),
]
