# search/urls.py
from django.urls import path
from .views import UserSearchView

urlpatterns = [
    path("api/search/", UserSearchView.as_view(), name="user_search"),
]
