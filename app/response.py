from rest_framework.response import Response


class ApiResponse:
    @staticmethod
    def success(data, message="Success", code=200):
        final_response = {
            "data": data,
            "message": message,
            code: code
        }
        return Response(final_response, status=code)

    @staticmethod
    def failure(data=None, message="Failure", code=500):
        final_response = {
            "data": data,
            "message": message,
            code: code
        }
        return Response(final_response, status=code)
