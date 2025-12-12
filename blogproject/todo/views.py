from django.shortcuts import render

# Create your views here.
# todo/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ToDo
from .serializers import ToDoSerializer

from rest_framework import viewsets
from rest_framework.decorators import action


class ToDoAPIView(APIView):

    def get(self, request):
        todos = ToDo.objects.all()
        serializer = ToDoSerializer(todos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ToDoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        try:
            todo = ToDo.objects.get(pk=pk)
        except ToDo.DoesNotExist:
            return Response({"error": "ToDo not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ToDoSerializer(todo, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            todo = ToDo.objects.get(pk=pk)
        except ToDo.DoesNotExist:
            return Response({"error": "ToDo not found"}, status=status.HTTP_404_NOT_FOUND)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# todo/views.py (add below APIView)

class ToDoViewSet(viewsets.ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        todo = self.get_object()
        user = request.user
        if user in todo.likes.all():
            todo.likes.remove(user)
            return Response({"status": "unliked"})
        else:
            todo.likes.add(user)
            return Response({"status": "liked"})
