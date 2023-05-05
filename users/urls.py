from django.urls import path
from apps.views import Index
from users.views import login_view
from users.views import RegisterView, forgot_view
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView

urlpatterns = [
    path('index', Index.as_view(), name='index'),
    path('login', login_view, name='login_view'),
    path('register', RegisterView.as_view(), name='register_view'),
    path('forgot', forgot_view, name='forgot_view'),

    # password forgot-password
    path('reset_password/', PasswordResetView.as_view(), name='reset_password'),
    path('reset_password_sent/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]

"""
 1 - Submit email from                         ---->             PasswordResetView
 2 - Email sent success message                ---->             PasswordResetDoneView
 3 - Link to password rest from in email       ---->             PasswordResetConfirmView
 4 - Password successfully change message      ---->             PasswordResetCompleteView   

"""

# Uzbek comment

"""
  1 - elektron pochta manzilini yuboring
  2 - E-pochta muvaffaqiyatli xabar yuborildi
  3 - E-pochtadagi qolgan parolga havola
  4 - Parolni muvaffaqiyatli o'zgartirish xabari
  
"""