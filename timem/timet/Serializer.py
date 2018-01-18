from rest_framework import serializers
from teacher.models import Teacher,Department
from location.models import ClassRoom,Lab
from semclass.models import Sec,Sem
from timet.models import Teacher_final,Master_final,Room_final,Lab_final

class Teacher_finalSerializer(serializers.ModelSerializer):
    class Meta:
        model=Teacher_final
        fields= '__all__'

class Master_finalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Master_final
        fields = '__all__'


class Room_finalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room_final
        fields = '__all__'


class Lab_finalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lab_final
        fields = '__all__'

class SecSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sec
        fields = '__all__'

class SemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sem
        fields = '__all__'

class ClassRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassRoom
        fields = ('block','room_no','dept','alt_name')

class LabSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lab
        fields = ('block','lab_no','dept','alt_name')

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('teacher_name','teacher_initials')

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'