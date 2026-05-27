from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Quote
from .serializers import QuoteSerializer
import random,requests
from rest_framework.generics import ListAPIView

class RandomQuoteView(APIView):
    def get(self, request):
        url = "https://zenquotes.io/api/random"

        response = requests.get(url)
        data = response.json()

        return Response({
            "text": data[0]["q"],
            "author": data[0]["a"]
        })



class QuoteListView(ListAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer

from rest_framework.generics import ListAPIView

class SearchQuoteView(ListAPIView):
    serializer_class = QuoteSerializer

    def get_queryset(self):
        keyword = self.request.query_params.get('search')
        return Quote.objects.filter(text__icontains=keyword)
    