from django.urls import path

from photobook.views import index

urlpatterns = [
    path('', index, name='index')
]
