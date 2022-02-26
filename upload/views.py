from django.shortcuts import render
from rest_framework.decorators import api_view
from django.core.files.storage import default_storage


@api_view(['POST'])
def savefile(request):
    file=request.FILES['file']
    file_name=default_storage.save(file.name, file)
    return Response(file.name)
