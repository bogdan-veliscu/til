from django.urls import path,url

from .views import(
    LoginAPIView, RegistrationAPIView, UserRetrieveUpdateAPIView
)

app_name = 'authentication'
urlpatterns = [
    path('user', UserRetrieveUpdateAPIView.as_view()),
    path('users/', RegistrationAPIView.as_view()),
    url(r'users/login/?$', LoginAPIView.as_view())
]
