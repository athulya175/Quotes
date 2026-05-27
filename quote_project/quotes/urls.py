from django.urls import path
from .views import RandomQuoteView,QuoteListView,SearchQuoteView

urlpatterns = [
    path('random/', RandomQuoteView.as_view()),
    path('',QuoteListView.as_view()),
    path('search/', SearchQuoteView.as_view()),
]