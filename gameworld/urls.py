from django.urls import path

from .views import *

urlpatterns = [
    path("", HomeView.as_view(), name='home'),
    path("create/", GameAddView.as_view(), name='create')

]