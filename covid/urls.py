from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from covid import views
from django.views.generic.base import RedirectView

urlpatterns = [
# Normal pages
    path('home/', views.HomeView.as_view()),
    path('tips/', views.TipsViews.as_view()),
    path('info/', views.InfoView.as_view()),
    path('dashboard', views.DashboardView.as_view()),
# Choose State URL
    path('chose_state', views.chose_state, name='chose_state'),
# Orginisations Profiles
    path('profile/edit/<int:pk>', views.MyProfileUpdateView.as_view(success_url="/covid/home")),
    path('myprofile/', views.MyProfileListView.as_view()),
    path('myprofile/<int:pk>', views.MyProfileDetailView.as_view()),
# Work/Post URL
    path('mypost/create/', views.MyPostCreate.as_view(success_url="/covid/mypost")),
    path('mypost/delete/<int:pk>', views.MyPostDeleteView.as_view(success_url="/covid/mypost")),
    path('mypost/', views.MyPostListView.as_view()),
    path('mypost/<int:pk>', views.MyPostDetailView.as_view()),
    path('mypost/edit/<int:pk>', views.MyPostUpdateView.as_view(success_url="/covid/mypost")),
# Orginizations Bank Account Details URL
    path('mypayment/create/', views.MyPaymentCreate.as_view(success_url="/covid/myprofile")),
    path('mypayment/edit/<int:pk>', views.MyPaymentUpdateView.as_view(success_url="/covid/myprofile")),
# FakeCheck URL
    path('fakecheck/', views.FakecheckListView.as_view()),
# Root URL
    path('', RedirectView.as_view(url="home/")), 
]