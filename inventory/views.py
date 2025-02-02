from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import SparePart
from .serializers import SparePartSerializer

@api_view(['GET', 'POST'])
def spare_part_list(request):
    if request.method == 'GET':
        model = request.GET.get('model', None)
        min_price = request.GET.get('min_price', None)
        max_price = request.GET.get('max_price', None)
        
        spare_parts = SparePart.objects.all()

        if model:
            spare_parts = spare_parts.filter(compatible_models__icontains=model)
        if min_price:
            spare_parts = spare_parts.filter(price__gte=min_price)
        if max_price:
            spare_parts = spare_parts.filter(price__lte=max_price)

        serializer = SparePartSerializer(spare_parts, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SparePartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def spare_part_detail(request, pk):
    spare_part = get_object_or_404(SparePart, pk=pk)

    if request.method == 'GET':
        serializer = SparePartSerializer(spare_part)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = SparePartSerializer(spare_part, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        spare_part.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
