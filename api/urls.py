from django.urls import path,include
from .views import studentsView,studentDetailView,EmployeeViewset
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('employees', EmployeeViewset,basename="employee")

urlpatterns = [
    path("students", studentsView),
    path("students/<int:pk>", studentDetailView),


    # path("employees/", Employees.as_view()),
    # path("employees/<int:pk>",EmployeeDetail.as_view())
    path("",include(router.urls))
]