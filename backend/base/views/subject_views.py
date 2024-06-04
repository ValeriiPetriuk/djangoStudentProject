from rest_framework import viewsets
from rest_framework.response import Response
from base.models import Subject
from base.serializers.subject_serializers import SubjectModelSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny


class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectModelSerializer

    def get_permissions(self):
        if self.action in ('create', 'update'):
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):

        user = self.request.user
        data = request.data
        if not user.role == "Teacher":
            return Response({"detail": "You are not teacher"}, status=403)
        new_subject = Subject.objects.create(
            teacher=self.request.user,
            name=data['name'],
        )

        new_subject.save()
        serializer = SubjectModelSerializer(new_subject)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        subject = self.get_object()
        data = request.data
        if not self.request.user == subject.teacher:
            return Response({"detail": "You are not allowed to update this subject"}, status=403)
        subject.name = data['name']
        subject.save()
        serializer = SubjectModelSerializer(subject)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        subject = self.get_object()
        if not self.request.user == subject.teacher:
            return Response({"detail": "You are not allowed to detele this subject"}, status=403)
        subject.delete()
        return Response({"detail": "subject delete"}, status=202)
