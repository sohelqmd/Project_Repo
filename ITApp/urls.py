from django.urls import path
from . import views

urlpatterns = [
  path('getpostIT/',views.GetPostITAPI.as_view()),
  path('putfetchdeleteIT/<int:pk>/',views.PutFetchDeleteITAPI.as_view()),
  path('getpostITcontact/',views.GetPostITContactAPI.as_view()),
  path('putfetchdeleteITConatct/<int:pk>/',views.PutFetchDeleteITContactAPI.as_view()),
]