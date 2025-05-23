from django.http import JsonResponse

from app.jwt import verify_token


def jwt_required(view_func):
    def wrapped_view(request, *args, **kwargs):
        auth_header = request.META.get('HTTP_AUTHORIZATION')
        if not auth_header or not auth_header.startswith('Bearer '):
            return JsonResponse({"error": "Unauthenticated"}, status=401)

        token = auth_header.split(' ')[1]
        payload = verify_token(token)
        if not payload:
            return JsonResponse({"error": "Unauthenticated"}, status=401)

        request.jwt_token = payload
        return view_func(request, *args, **kwargs)
    return wrapped_view
