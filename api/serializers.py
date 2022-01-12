from rest_framework import serializers
from .models import *







class Universityserializer(serializers.ModelSerializer):


    class Meta:
        fields = ['title']
        model = University


class Studentserializer(serializers.ModelSerializer):
    university =   Universityserializer()

    class Meta:
        fields = ['id', 'name','university']
        model = Student


    def create(self, validated_data):
        university = validated_data.pop('university')
        pro = University.objects.get_or_create(**university)     
        stud_obj = Student.objects.create(university=pro[0],**validated_data)
        return stud_obj


    def update(self, instance,validated_data):

        university = validated_data.pop('university')
        pro = University.objects.get_or_create(**university) 
        instance.university=pro[0]
        instance.name=validated_data.pop('name')
        instance.save()
        return instance



class Univstudentserializer(serializers.ModelSerializer):

    class Meta:
        fields = ['name']
        model = Student



        