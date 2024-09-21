from django.urls import path
from .views import SignupView, SigninView, LogoutView
urlpatterns = [

    path('signup/', SignupView.as_view(), name="signup"),
    path('signin/', SigninView.as_view(), name="siginin"),
    path('logout/', LogoutView.as_view(), name="logout"),
]