from django.urls import path

from .views import QRCodeGeneratorView

urlpatterns = [
    path('generate/', QRCodeGeneratorView.as_view(), name='generate-qr'),
]
