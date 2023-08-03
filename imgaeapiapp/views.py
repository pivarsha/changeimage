from django.shortcuts import render
from . models import *
from .serializers import *
from rest_framework.views import APIView
import random
from rest_framework.response import Response

class ImageApi(APIView):
    def get(self,request):
        images = Image.objects.all()
        if images:
            image = random.choice(images)
            image_url = image.img.url
        else:
            image_url = "IMG-20230801-WA0006.jpg"
        return Response({"image":image_url})
    



