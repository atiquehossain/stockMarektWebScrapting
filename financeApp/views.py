from django.http import JsonResponse
from .tasks import fetch_and_store_data

def home(request):
    try:
        urls = {
            "Apple": "/apple/",
            "Amazon": "/amazon/",
            "Google": "/google/",
            "Microsoft": "/microsoft/"
        }
        response = JsonResponse(urls, safe=False, status=200)
        print(response.content.decode('utf-8'))
        return response
    except Exception as e:
        response = JsonResponse({'status': 'error', 'message': str(e)}, status=500)
        print(response.content.decode('utf-8'))
        return response

def apple(request):
    return fetch_and_respond('AAPL')

def amazon(request):
    return fetch_and_respond('AMZN')

def google(request):
    return fetch_and_respond('GOOGL')

def microsoft(request):
    return fetch_and_respond('MSFT')

def fetch_and_respond(ticker):
    try:
        data_json = fetch_and_store_data(ticker)

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





