from django.http import JsonResponse


def home(request):
    return JsonResponse({
        'Application': "Bill Splitter",
        "Version": "1.0",
        "Developer Right": "Aniket Gautam"
    })
