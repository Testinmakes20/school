from .import views
from django.urls import path,include
app_name='credential'

urlpatterns=[
       path('', views.demo, name='demo'),
       path('register',views.register,name="register"),
       path('Login',views.Login,name="Login"),
       path('catalog',views.catalog,name="catalog"),
       # path('logout',views.logout,name='logout'),
]