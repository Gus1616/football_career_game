from django.urls import path
from .views import LoadJsonView

urlpatterns = [
    path('load-json/', LoadJsonView.as_view(), name='load-json'),
]