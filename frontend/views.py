import requests
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings


def index(request):
    return render(request, 'index.html')


@csrf_exempt
def upload_photo(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Only POST method is allowed'}, status=405)

    if not request.FILES.get('photo'):
        return JsonResponse({'error': 'No photo file provided'}, status=400)

    try:
        # Get the photo from the request
        photo = request.FILES['photo']

        # Forward the request to the backend API
        files = {'photo': (photo.name, photo.read(), photo.content_type)}
        backend_url = settings.PHOTO_ENHANCER_API_URL.rstrip('/') + '/upload_photo'
        response = requests.post(backend_url, files=files)

        # Return the API response
        return JsonResponse(response.json(), status=response.status_code)

    except requests.RequestException as e:
        return JsonResponse({'error': f'API request failed: {str(e)}'}, status=500)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


@csrf_exempt
def enhance_photo(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Only POST method is allowed'}, status=405)

    session_id = request.POST.get('session_id')
    if not session_id:
        return JsonResponse({'error': 'No session_id provided'}, status=400)

    try:
        # Forward the request to the backend API
        data = {'session_id': session_id}
        backend_url = settings.PHOTO_ENHANCER_API_URL.rstrip('/') + '/enhance_photo'
        response = requests.post(backend_url, data=data)

        # Return the API response
        return JsonResponse(response.json(), status=response.status_code)

    except requests.RequestException as e:
        return JsonResponse({'error': f'API request failed: {str(e)}'}, status=500)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
