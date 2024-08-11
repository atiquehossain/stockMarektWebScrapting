# financeApp/views.py
from django.http import JsonResponse
from .tasks import fetch_and_store_data

from django.http import JsonResponse
from .tasks import fetch_and_store_data

def apple(request):
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




