from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import Client, Project
from .serializers import ClientSerializer, ProjectSerializer
from django.contrib.auth.models import User

class ClientViewSet(viewsets.ModelViewSet):
    """
    Handles:
    - GET /clients/
    - POST /clients/
    - GET /clients/:id/
    - PUT/PATCH /clients/:id/
    - DELETE /clients/:id/
    """
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class ProjectViewSet(viewsets.ViewSet):
    """
    Handles:
    - GET /projects/ (list of projects assigned to logged-in user)
    - POST /clients/:client_id/projects/ (create project for a client)
    """

    permission_classes = [IsAuthenticated]

    def list(self, request):
        projects = Project.objects.filter(users=request.user)
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    def create(self, request, **kwargs):
        # Retrieve client_id from the URL: /clients/:id/projects/
        client_id = self.kwargs.get('client_pk') or self.kwargs.get('client_id')
        client = get_object_or_404(Client, id=client_id)

        project_name = request.data.get('project_name')
        user_data = request.data.get('users', [])

        if not project_name or not isinstance(user_data, list):
            return Response(
                {"error": "Invalid input, 'project_name' and 'users' list required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Create the project
        project = Project.objects.create(
            project_name=project_name,
            client=client,
            created_by=request.user,
        )

        # Assign users to the project
        for user in user_data:
            user_obj = get_object_or_404(User, id=user['id'])
            project.users.add(user_obj)

        project.save()
        serializer = ProjectSerializer(project)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

