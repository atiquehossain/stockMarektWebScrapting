# myproject/urls.py
from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include
from django.http import HttpResponse

from financeApp.models import HistoricalData
from financeApp.tasks import fetch_and_store_data
from django.http import JsonResponse

from financeApp.views import apple, apple


# Define a simple view for the root URL
def home(request):
    try:
        # Fetch the real-time data
        data_json = fetch_and_store_data()

        if data_json:
            response = JsonResponse(data_json, safe=False, status=200)
        else:
            response = JsonResponse({'status': 'error', 'message': 'Failed to fetch data.'}, status=500)

        print(response.content.decode('utf-8'))  # Print the response data to the console
        return response
    except Exception as e:
        response = JsonResponse({'status': 'error', 'message': str(e)}, status=500)
        print(response.content.decode('utf-8'))  # Print the error response data to the console
        return response

urlpatterns = [
    path('admin/', admin.site.urls),
    path('apple/', apple, name='apple'),
    path('', home),  # Handle the root URL
]
