from django.urls import path

from e_tender_api import views

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
]