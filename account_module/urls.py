from  django.urls import path
from .views import RegisterUserGenericApiView,Login_UserSerializerGenericApiView

urlpatterns=[
    path('register_api/',RegisterUserGenericApiView.as_view(),name='register_page_api'),
    path('login_api/',Login_UserSerializerGenericApiView.as_view(),name='login_page_api')
    ]