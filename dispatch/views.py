from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from .googledrive import create_file
from .serializers import DocumentSerializer


class DocumentAPIView(CreateAPIView):
    '''Контроллер POST запроса'''
    serializer_class = DocumentSerializer

    def create(self, request, *args, **kwargs) -> Response:
        data = request.data if request.data else request.query_params
        serializer = self.get_serializer(data=data)

        if serializer.is_valid(raise_exception=True):
            result, status = create_file(data['name'], data['data'])
            return Response(data=result, status=status)
