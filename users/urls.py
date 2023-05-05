from django.urls import path
from apps.views import Index
from users.views import login_view
from users.views import RegisterView, forgot_view

urlpatterns = [
    path('index', Index.as_view(), name='index'),
    path('login', login_view, name='login_view'),
    path('register', RegisterView.as_view(), name='register_view'),
    path('forgot', forgot_view, name='forgot_view')
]
