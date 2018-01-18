from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Teacher_final,Master_final,Lab_final,Room_final
from teacher.models import Teacher,Department
from location.models import ClassRoom,Lab
from semclass.models import Sec,Sem
from .Serializer import Teacher_finalSerializer,Master_finalSerializer,Room_finalSerializer,Lab_finalSerializer,SecSerializer,SemSerializer,TeacherSerializer,DepartmentSerializer,ClassRoomSerializer,LabSerializer

class tfapi(APIView):
    def get(self, request: object) -> object:
        tf = Teacher_final.objects.all()
        serial = Teacher_finalSerializer(tf, many=True)
        return Response(serial.data)

    def post(self):
        pass

class mfapi(APIView):
    def get(self, request: object) -> object:
        mf = Master_final.objects.all()
        serial = Master_finalSerializer(mf,many=True)
        return Response(serial.data)

    def post(self):
        pass

class lfapi(APIView):
    def get(self, request: object) -> object:
        lf = Lab_final.objects.all()
        serial = Lab_finalSerializer(lf, many=True)
        return Response(serial.data)

    def post(self):
        pass

class rfapi(APIView):
    def get(self, request: object) -> object:
        rf = Room_final.objects.all()
        serial = Room_finalSerializer(rf, many=True)
        return Response(serial.data)

    def post(self):
        pass

class crapi(APIView):
    def get(self, request: object) -> object:
        cr = ClassRoom.objects.all()
        serial = ClassRoomSerializer(cr, many=True)
        return Response(serial.data)

    def post(self):
        pass

class lbapi(APIView):
    def get(self, request: object) -> object:
        lb = Lab.objects.all()
        serial = LabSerializer(lb, many = True)
        return Response(serial.data)

    def post(self):
        pass

class secapi(APIView):
    def get(self, request: object) -> object:
        sec = Sec.objects.all()
        serial = SecSerializer(sec, many=True)
        return Response(serial.data)

    def post(self):
        pass

class semapi(APIView):
    def get(self, request: object) -> object:
        sem = Sem.objects.all()
        serial = SemSerializer(sem, many=True)
        return Response(serial.data)
    def post(self):
        pass

class teacherapi(APIView):
    def get(self, request: object) -> object:
        teacher = Teacher.objects.all()
        serial =  TeacherSerializer(teacher,many=True)
        return Response(serial.data)
    def post(self):
        pass

class deptapi(APIView):
    def get(self, request: object) -> object:
        dept = Department.objects.all()
        serial = DepartmentSerializer(dept, many=True)
        return Response(serial.data)
    def post(self):
        pass