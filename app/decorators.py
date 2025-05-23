from functools import wraps

from django.http import JsonResponse

from app.jwt import verify_token
from app.response import ApiResponse


def jwt_required(view_func):
    @wraps(view_func)
    def wrapped_view(self,request, *args, **kwargs):
        auth_header = request.META.get('HTTP_AUTHORIZATION')
        if not auth_header or not auth_header.startswith('Bearer '):
            return ApiResponse.failure(None, "Unauthenticated", code=401)
        token = auth_header.split(' ')[1]
        payload = verify_token(token)
        if not payload:
            return ApiResponse.failure(None,"Unauthenticated", code=401)

        request.jwt_token = payload
        return view_func(self,request, *args, **kwargs)
    return wrapped_view
