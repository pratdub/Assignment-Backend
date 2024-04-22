from django.urls import path
from account.views import Resgisteruser,LoginAPI
urlpatterns = [
    path('register/', Resgisteruser.as_view()),
    path('login/', LoginAPI.as_view())
]