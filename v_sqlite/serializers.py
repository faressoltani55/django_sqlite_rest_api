from rest_framework import serializers

from .models import *


class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = ('id', 'firstName', 'lastName', 'email')


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'firstName', 'lastName', 'email')


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ('id', 'name', 'student')


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('id', 'name')


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('id','note', 'subject', 'student')