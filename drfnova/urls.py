from django.contrib import admin
from django.urls import path

from dispatch.views import DocumentAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/document/', DocumentAPIView.as_view()),
]
