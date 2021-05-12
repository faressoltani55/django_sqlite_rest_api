# Create your views here.
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from .serializers import *


@api_view(['GET', 'POST'])
def ProfessorViewForGetAndPost(request):
    if request.method == 'GET':
        queryset = Professor.objects.all()
        serializer_class = ProfessorSerializer(queryset, many=True)
        return JsonResponse(serializer_class.data, safe=False)
    elif request.method == 'POST':
        queryset = JSONParser().parse(request)
        serializer_class = ProfessorSerializer(data=queryset)
        if serializer_class.is_valid():
            serializer_class.save()
            return JsonResponse(serializer_class.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def ProfessorViewForPutAndDelete(request, _id):
    professor = Professor.objects.get(id=_id)
    if request.method == 'GET':
        serializer_class = ProfessorSerializer(professor)
        return JsonResponse(serializer_class.data, safe=False)
    elif request.method == 'PUT':
        queryset = JSONParser().parse(request)
        serializer_class = ProfessorSerializer(professor, data=queryset)
        if serializer_class.is_valid():
            serializer_class.save()
            return JsonResponse(serializer_class.data)
        return JsonResponse(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        professor.delete()
        return JsonResponse({'message': 'Professor was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def StudentViewForGetAndPost(request):
    if request.method == 'GET':
        queryset = Student.objects.all()
        serializer_class = StudentSerializer(queryset, many=True)
        return JsonResponse(serializer_class.data, safe=False)
    elif request.method == 'POST':
        queryset = JSONParser().parse(request)
        serializer_class = StudentSerializer(data=queryset)
        if serializer_class.is_valid():
            serializer_class.save()
            return JsonResponse(serializer_class.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def StudentViewForPutAndDelete(request, _id):
    student = Student.objects.get(id=_id)
    if request.method == 'GET':
        serializer_class = StudentSerializer(student)
        return JsonResponse(serializer_class.data, safe=False)
    elif request.method == 'PUT':
        queryset = JSONParser().parse(request)
        serializer_class = StudentSerializer(student, data=queryset)
        if serializer_class.is_valid():
            serializer_class.save()
            return JsonResponse(serializer_class.data)
        return JsonResponse(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        student.delete()
        return JsonResponse({'message': 'Student was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def ClassViewForGetAndPost(request):
    if request.method == 'GET':
        queryset = Class.objects.all()
        serializer_class = ClassSerializer(queryset, many=True)
        return JsonResponse(serializer_class.data, safe=False)
    elif request.method == 'POST':
        queryset = JSONParser().parse(request)
        serializer_class = ClassSerializer(data=queryset)
        if serializer_class.is_valid():
            serializer_class.save()
            return JsonResponse(serializer_class.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def ClassViewForPutAndDelete(request, _id):
    classe = Class.objects.get(id=_id)
    if request.method == 'GET':
        serializer_class = ClassSerializer(classe)
        return JsonResponse(serializer_class.data, safe=False)
    elif request.method == 'PUT':
        queryset = JSONParser().parse(request)
        serializer_class = ClassSerializer(classe, data=queryset)
        if serializer_class.is_valid():
            serializer_class.save()
            return JsonResponse(serializer_class.data)
        return JsonResponse(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        classe.delete()
        return JsonResponse({'message': 'Class was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def SubjectViewForGetAndPost(request):
    if request.method == 'GET':
        queryset = Subject.objects.all()
        serializer_class = SubjectSerializer(queryset, many=True)
        return JsonResponse(serializer_class.data, safe=False)
    elif request.method == 'POST':
        queryset = JSONParser().parse(request)
        serializer_class = SubjectSerializer(data=queryset)
        if serializer_class.is_valid():
            serializer_class.save()
            return JsonResponse(serializer_class.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def SubjectViewForPutAndDelete(request, _id):
    subject = Subject.objects.get(id=_id)
    if request.method == 'GET':
        serializer_class = SubjectSerializer(subject)
        return JsonResponse(serializer_class.data, safe=False)
    elif request.method == 'PUT':
        queryset = JSONParser().parse(request)
        serializer_class = SubjectSerializer(subject, data=queryset)
        if serializer_class.is_valid():
            serializer_class.save()
            return JsonResponse(serializer_class.data)
        return JsonResponse(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        subject.delete()
        return JsonResponse({'message': 'Subject was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def NoteViewForGetAndPost(request):
    if request.method == 'GET':
        queryset = Note.objects.all()
        serializer_class = NoteSerializer(queryset, many=True)
        return JsonResponse(serializer_class.data, safe=False)
    elif request.method == 'POST':
        queryset = JSONParser().parse(request)
        serializer_class = NoteSerializer(data=queryset)
        if serializer_class.is_valid():
            serializer_class.save()
            return JsonResponse(serializer_class.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def NoteViewForPutAndDelete(request, _id):
    note = Note.objects.get(id=_id)
    if request.method == 'GET':
        serializer_class = NoteSerializer(note)
        return JsonResponse(serializer_class.data, safe=False)
    elif request.method == 'PUT':
        queryset = JSONParser().parse(request)
        serializer_class = NoteSerializer(note, data=queryset)
        if serializer_class.is_valid():
            serializer_class.save()
            return JsonResponse(serializer_class.data)
        return JsonResponse(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        note.delete()
        return JsonResponse({'message': 'Note was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
