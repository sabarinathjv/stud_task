from django.db import models




class University(models.Model):

    title = models.CharField(max_length=200)


class Student(models.Model):

    name = models.CharField(max_length=200)
    university = models.ForeignKey(University, related_name="university", on_delete=models.CASCADE)
