from django.db import models


# Create your models here.
class Professor(models.Model):
    firstName = models.CharField("First name", max_length=255, blank=True, null=True)
    lastName = models.CharField("Last name", max_length=255, blank=True, null=True)
    email = models.EmailField()

    def __str__(self):
        return self.firstName + " " + self.lastName


class Student(models.Model):
    firstName = models.CharField("First name", max_length=255, blank=True, null=True)
    lastName = models.CharField("Last name", max_length=255, blank=True, null=True)
    email = models.EmailField()

    def __str__(self):
        return self.firstName + " " + self.lastName


class Class(models.Model):
    name = models.CharField("First name", max_length=255, blank=True, null=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField("First name", max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class Note(models.Model):
    note = models.FloatField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.note