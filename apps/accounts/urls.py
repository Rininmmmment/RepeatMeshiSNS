from django.urls import path
from django.views.generic import RedirectView
from . import views

app_name ='accounts'

urlpatterns =[
    path('', RedirectView.as_view(url='/login/')),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('registration/', views.AccountRegistration.as_view(), name='registation'),
]
      
