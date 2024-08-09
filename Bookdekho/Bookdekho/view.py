# books/views.py
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .utils import fetch_books

@api_view(['GET'])
def search_books(request):
    query = request.GET.get('query', '')
    books_data = fetch_books(query)
    return Response(books_data)
