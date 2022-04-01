from django.shortcuts import render
from django.core.files.storage import default_storage
from rest_framework.decorators import api_view
from rest_framework.response import Response
from upload.serializers import UploadModelSerializer
from .models import UploadModel


@api_view(['POST'])
def savefile(request):
    file = request.FILES['file']
    file_name = default_storage.save(file.name, file)
    uploadModel = UploadModel()
    uploadModel.name = file_name
    uploadModel.image = file_name
    serializer = UploadModelSerializer(uploadModel, many=False)
    return Response(serializer.data)
