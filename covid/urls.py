from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('chose_state', views.chose_state, name='chose_state'),
    path('tips', views.tips, name='tips'),
    path('info', views.info, name='info'),
    path('fake', views.fake, name='fake')
]