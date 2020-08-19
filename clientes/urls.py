from django.urls import path
from .views import SignUp, login_user,login_submit


urlpatterns = [
    path('register/',SignUp.as_view(),name='signup'),
    path('login/',login_user,name='login'),
    path('login/submit',login_submit,name='loginsubmit')
]