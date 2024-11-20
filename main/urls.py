from django.urls import path
from main.views import PortfolioMainView

urlpatterns = [
    path('', PortfolioMainView.as_view(), name='main'),
]
