from django.contrib import admin
from rest_framework import routers
from rest_framework.authtoken import views
from django.urls import path, include
from users.views import RegisterUserView, VerifyEmailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('books.urls')),
    path('api-token-auth/', views.obtain_auth_token),
    path('register/', RegisterUserView.as_view()),
    path('verify-email/<str:token>/', VerifyEmailView.as_view()),
]