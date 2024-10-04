from django.urls import path,include
from .views import Employees,EmployeeDetail,studentsView,studentDetailView


urlpatterns = [
    path("students", studentsView),
    path("students/<int:pk>", studentDetailView),

    path("employees/", Employees.as_view()),
    path("employees/<int:pk>",EmployeeDetail.as_view())
]