from . import views
from django.urls import path

urlpatterns = [
    path('', views.TickerSearch.as_view(), name="tickersearch"),
    path('tickersymbol/analysis', views.Analysis, name="tickersymbolanalysis"),
]