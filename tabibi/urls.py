from django.urls import re_path
from. import views

#------------------ set up url for login, signup anf test_token --------------------------------------
urlpatterns = [
    re_path('login', views.login),
    re_path('signup', views.signup),
    re_path('test_token', views.test_token),
]
