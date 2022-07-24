from django.urls import path
from .views import StudentList, StudentDetail, VacStatusReport, VacStatusDashReport

urlpatterns = [
    path('students/', StudentList.as_view()),
    path('student/<slug:pk>/', StudentDetail.as_view()),
    path('vacreport/', VacStatusReport.as_view()),
    path('dashreport/', VacStatusDashReport.as_view()),

]
