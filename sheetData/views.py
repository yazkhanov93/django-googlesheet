from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Order
from .serializers import OrderSerializer


class OrderListView(APIView):
    """ Order List """
    def get(self, request):
        try:
            orders = Order.objects.all()
            serializer = OrderSerializer(orders, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)


class OrderUpload(APIView):
    """ Upload data from GoogleSheet to Database """
    def post(self, request):
        for order in request.data:
            serializer = OrderSerializer(data=order)
            if serializer.is_valid():
                serializer.save()
            else:
                return Response(serializer.errors)
        return Response(status=status.HTTP_200_OK)
