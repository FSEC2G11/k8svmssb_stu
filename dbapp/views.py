from .models import VacDoseStatus, Student
from .serializers import StudentSerializer, VacReportSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404, JsonResponse, HttpResponse
import datetime, json

# Create your views here.
class StudentList(APIView):

    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentDetail(APIView):

    def get_object(self, pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        student = self.get_object(pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def put(self, request, pk):
        student = self.get_object(pk)
        serializer = StudentSerializer(student, data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        student = self.get_object(pk)
        student.delete()
        return Response(status=status.HTTP_200_OK)


class VacStatusReport(APIView):
    def get(self, request):
        report = Student.objects.all()
        serializer = VacReportSerializer(report, many=True)
        return Response(serializer.data)


class VacStatusDashReport(APIView):
    def get(self, request):
        regStuCount = Student.objects.count()

        vacstatus = VacDoseStatus.objects.all()
        partialCount = vacstatus.filter(vacDateD1__isnull=False, vacDateD2__isnull=True).count()
        fullCount = vacstatus.filter(vacDateD1__isnull=False, vacDateD2__isnull=False).count()

        data = {"totalStu": 50,
                "regStu": regStuCount,
                "partial": partialCount,
                "full": fullCount,
                }
        dump = json.dumps(data)

        return HttpResponse(dump, content_type='application/json')


